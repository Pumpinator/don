package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class Losses extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 150, nullable = false)
    private double total;

    @ManyToOne
    @JoinColumn(name = "production_id")
    private Production production;

    @ManyToOne
    @JoinColumn(name = "raw_material_id")
    private RawMaterial rawMaterial;

    @ManyToOne
    @JoinColumn(name = "product_id")
    private Cookie cookie;


}
