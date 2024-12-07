package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

import java.util.Collection;

@Entity
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString(callSuper = true)
public class Recipe extends Measurable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50, nullable = false)
    private String name;

    @Column(length = 1000, nullable = false)
    private String instructions;

    @ManyToOne
    @JoinColumn(name = "cookie_id")
    private Cookie cookie;

    @OneToMany(mappedBy = "recipe", fetch = FetchType.EAGER) // Fetch ingredients eagerly
    private Collection<Ingredient> ingredients;

}