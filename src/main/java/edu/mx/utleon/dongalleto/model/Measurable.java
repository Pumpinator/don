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

    public double convert() {
        if (this.measure.getName().equals(Measures.Kilogramo.name())) {
            return this.quantity * 1000;
        }
        if (this.measure.getName().equals(Measures.Litro.name())) {
            return this.quantity * 1000;
        }
        if (this.measure.getName().equals(Measures.Gramo.name())) {
            return this.quantity / 1000;
        }
        if (this.measure.getName().equals(Measures.Mililitro.name())) {
            return this.quantity / 1000;
        }
        return this.quantity;
    }

}