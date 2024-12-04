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
@ToString
public abstract class Inventory extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 150, nullable = false)
    private LocalDate expirationDate;

    @Column(length = 150, nullable = false)
    private double cost;

    public long getDaysUntilExpiration() {
        return ChronoUnit.DAYS.between(LocalDate.now(), this.getExpirationDate());
    }

}