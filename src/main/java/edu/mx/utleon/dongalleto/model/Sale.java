package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.SuperBuilder;

import java.util.Collection;

@Entity
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class Sale extends Transaction {

    @OneToMany(mappedBy = "sale")
    private Collection<SaleDetail> saleDetails;


    public void addSaleDetail(SaleDetail saleDetailEntity) {
        this.saleDetails.add(saleDetailEntity);
        saleDetailEntity.setSale(this);
    }
}