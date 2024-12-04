package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

import java.util.Collection;
import java.util.HashSet;
import java.util.List;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class RawMaterial {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50, nullable = false)
    private String name;

    @ManyToMany(mappedBy = "rawMaterial")
    private Collection<Supplier> suppliers = new HashSet<>(); // Initialize the collection

    public List<Supplier> getSuppliers() {
        return (List<Supplier>) suppliers;
    }
}
