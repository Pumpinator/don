package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

import java.util.Collection;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class Recipe extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50, nullable = false)
    private String name;

    @Column(length = 150, nullable = false)
    private double cost;

    @Column(length = 150, nullable = false)
    private String instructions;

    @ManyToOne
    @JoinColumn(name = "cookie_id")
    private Cookie cookie;

    @OneToMany(mappedBy = "recipe")
    private Collection<Ingredient> ingredients;

}
