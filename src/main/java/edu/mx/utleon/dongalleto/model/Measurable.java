package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;

@MappedSuperclass
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public abstract class Measurable {

    @Column(length = 150, nullable = false)
    private double quantity;

    @ManyToOne
    @JoinColumn(name = "measure_id", nullable = false)
    private Measure measure;

    public String getQuantity() {
        return this.quantity == (int) this.quantity ? String.valueOf((int) this.quantity) : String.valueOf(this.quantity);
    }

    public Measure getMeasure() {
        if (this.measure.getSymbol().equals("$"))
            return Measure.builder().id(this.measure.getId()).name(this.measure.getName() + "s").symbol(this.measure.getSymbol()).build();
        return this.quantity > 1 ? Measure.builder().id(this.measure.getId()).name(this.measure.getName() + "s").symbol(this.measure.getSymbol() + "s").build() : this.measure;
    }
}