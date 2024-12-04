package edu.mx.utleon.dongalleto.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.*;

import java.util.Collection;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class Supplier {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 50, nullable = false)
    private String name;

    @Column(length = 100, nullable = false)
    private String contact;

    @Column(length = 50, nullable = false)
    private String type;

    @JsonIgnore
    @ManyToMany
    @JoinTable(
            name = "raw_material_supplier",
            joinColumns = @JoinColumn(name = "supplier_id"),
            inverseJoinColumns = @JoinColumn(name = "raw_material_id")
    )
    private Collection<RawMaterial> rawMaterial;

}
