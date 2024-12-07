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
@ToString(callSuper = true)
public class RawMaterialInventory extends Inventory {

    @ManyToOne
    @JoinColumn(name = "raw_material_id", nullable = false)
    private RawMaterial rawMaterial;

    @ManyToOne
    @JoinColumn(name = "supplier_id")
    private Supplier supplier;

    public boolean isExpired() {
        LocalDate expirationDate = this.getExpirationDate();
        if (expirationDate == null) {
            return false;
        }
        return ChronoUnit.DAYS.between(LocalDate.now(), expirationDate) < 0;
    }

    public boolean isExpiring() {
        LocalDate expirationDate = this.getExpirationDate();
        if (expirationDate == null) {
            return false;
        }
        return ChronoUnit.DAYS.between(LocalDate.now(), expirationDate) < 7;
    }

}
