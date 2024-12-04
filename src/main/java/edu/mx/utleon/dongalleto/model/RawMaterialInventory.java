package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.*;
import lombok.experimental.SuperBuilder;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

@Entity
@SuperBuilder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class RawMaterialInventory extends Inventory {

    @ManyToOne
    @JoinColumn(name = "raw_material_id", nullable = false)
    private RawMaterial rawMaterial;

    @ManyToOne
    @JoinColumn(name = "purchase_id", nullable = false)
    private Purchase purchase;

    @ManyToOne
    @JoinColumn(name = "supplier_id", nullable = false)
    private Supplier supplier;

    public boolean isExpired() {
        return ChronoUnit.DAYS.between(LocalDate.now(), this.getExpirationDate()) < 0;
    }

    public boolean isExpiring() {
        return ChronoUnit.DAYS.between(LocalDate.now(), this.getExpirationDate()) < 7;
    }

}
