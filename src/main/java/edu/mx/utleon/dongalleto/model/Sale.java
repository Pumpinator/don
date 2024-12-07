package edu.mx.utleon.dongalleto.model;

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
public class Sale extends Transaction {

    @OneToMany(mappedBy = "sale")
    private Collection<SaleDetail> saleDetails;



}