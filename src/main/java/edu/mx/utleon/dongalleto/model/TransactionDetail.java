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
public abstract class TransactionDetail extends Measurable {

    @Column(length = 150)
    private double unitPrice;

    @Column(length = 150)
    private double totalPrice;

    public double getSubtotal() {
        return this.getQuantity() * this.getUnitPrice();
    }

}