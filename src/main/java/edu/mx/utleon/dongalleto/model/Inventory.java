package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;

@MappedSuperclass
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public abstract class Inventory extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 150, nullable = false)
    private LocalDate expirationDate;

    @Column(length = 150, nullable = false)
    private double cost;

}