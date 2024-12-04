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
@ToString
public class Cookie {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50, nullable = false)
    private String name;

    @Column(length = 150, nullable = false)
    private double price;

    @OneToMany(mappedBy = "cookie")
    private Collection<Recipe> recipes;

}
