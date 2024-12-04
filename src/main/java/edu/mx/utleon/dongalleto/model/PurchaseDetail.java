package edu.mx.utleon.dongalleto.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

@Entity
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
@JsonInclude(JsonInclude.Include.NON_NULL)
public class PurchaseDetail extends TransactionDetail {

    @EmbeddedId
    private PurchaseDetailId id;

    @ManyToOne
    @JoinColumn(name = "supplier_id", nullable = false)
    private Supplier supplier;

    @ManyToOne
    @MapsId("rawMaterial")
    @JoinColumn(name = "raw_material_id")
    private RawMaterial rawMaterial;

    @ToString.Exclude
    @JsonIgnore
    @ManyToOne
    @MapsId("purchase")
    @JoinColumn(name = "purchase_id")
    private Purchase purchase;

    @Embeddable
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    @Getter
    @Setter
    @EqualsAndHashCode
    @ToString
    public static class PurchaseDetailId {

        @Column(name = "raw_material_id")
        private Integer rawMaterial;

        @Column(name = "purchase_id")
        private Integer purchase;

    }
}