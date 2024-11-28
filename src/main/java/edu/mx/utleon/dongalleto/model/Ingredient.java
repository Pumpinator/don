package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class Ingredient {

    @EmbeddedId
    private IngredientId id;

    @Column(length = 150, nullable = false)
    private double quantity;

    @ManyToOne
    @JoinColumn(name = "measure_id", nullable = false)
    private Measure measure;

    @ManyToOne
    @MapsId("rawMaterial")
    @JoinColumn(name = "raw_material_id")
    private RawMaterial rawMaterial;

    @ManyToOne
    @MapsId("recipe")
    @JoinColumn(name = "recipe_id")
    private Recipe recipe;

    @Embeddable
    @NoArgsConstructor
    @AllArgsConstructor
    @Getter
    @Setter
    @EqualsAndHashCode
    @ToString
    public static class IngredientId {

        @Column(name = "raw_material_id")
        private Integer rawMaterial;

        @Column(name = "recipe_id")
        private Integer recipe;

    }
}