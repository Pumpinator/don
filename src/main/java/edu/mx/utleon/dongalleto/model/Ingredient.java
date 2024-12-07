package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

@Entity
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString(callSuper=true)
public class Ingredient extends Measurable {

    @EmbeddedId
    private IngredientId id;

    @ToString.Exclude
    @ManyToOne
    @MapsId("rawMaterial")
    @JoinColumn(name = "raw_material_id")
    private RawMaterial rawMaterial;

    @ToString.Exclude
    @ManyToOne
    @MapsId("recipe")
    @JoinColumn(name = "recipe_id")
    private Recipe recipe;

    @Embeddable
    @Builder
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