package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

@MappedSuperclass
@SuperBuilder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public abstract class TransactionDetail {

    @Column(length = 150)
    private double unitPrice;

    @Column(length = 150)
    private double totalPrice;

    @Column(length = 150, nullable = false)
    private double quantity;

    @ManyToOne
    @JoinColumn(name = "measure_id", nullable = false)
    private Measure measure;

    public double getSubtotal() {
        return this.quantity * this.unitPrice;
    }

}