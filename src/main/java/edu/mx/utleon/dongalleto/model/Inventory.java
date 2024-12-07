package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

@MappedSuperclass
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString(callSuper = true)
public abstract class Inventory extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 150)
    private LocalDate expirationDate;

    @Column(length = 150, nullable = false)
    private double cost;

    public long getDaysUntilExpiration() {
        LocalDate expirationDate = this.getExpirationDate();
        if (expirationDate == null) {
            return Long.MAX_VALUE; // or any other value that indicates no expiration date
        }
        return ChronoUnit.DAYS.between(LocalDate.now(), expirationDate);
    }


}