package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class PurchaseDetail extends TransactionDetail {

    @EmbeddedId
    private PurchaseDetailId id;

    @Column(length = 150, nullable = false)
    private double price;

    @Column(length = 150, nullable = false)
    private int quantity;

    @Column(length = 150, nullable = false)
    private double subtotal;

    @ManyToOne
    @JoinColumn(name = "measure_id", nullable = false)
    private Measure measure;

    @ManyToOne
    @JoinColumn(name = "supplier_id", nullable = false)
    private Supplier supplier;

    @ManyToOne
    @MapsId("rawMaterial")
    @JoinColumn(name = "raw_material_id")
    private RawMaterial rawMaterial;

    @ManyToOne
    @MapsId("purchase")
    @JoinColumn(name = "purchase_id")
    private Purchase purchase;

    @Embeddable
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