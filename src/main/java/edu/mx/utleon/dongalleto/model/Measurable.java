package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

@MappedSuperclass
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public abstract class Measurable {

    @Column(length = 150, nullable = false)
    private double quantity;

    @ManyToOne
    @JoinColumn(name = "measure_id", nullable = false)
    private Measure measure;

    public Measure getMeasure() {
        if (this.measure.getSymbol().equals("$"))
            return Measure.builder().id(this.measure.getId()).name(this.measure.getName() + "s").symbol(this.measure.getSymbol()).build();
        return this.quantity > 1 ? Measure.builder().id(this.measure.getId()).name(this.measure.getName() + "s").symbol(this.measure.getSymbol() + "s").build() : this.measure;
    }
}