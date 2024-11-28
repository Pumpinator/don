package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@MappedSuperclass
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public abstract class TransactionDetail {

    @Column(length = 150, nullable = false)
    private double price;

    @Column(length = 150, nullable = false)
    private int quantity;

    @Column(length = 150, nullable = false)
    private double subtotal;

    public double getSubtotal() {
        return this.quantity * this.price;
    }

}