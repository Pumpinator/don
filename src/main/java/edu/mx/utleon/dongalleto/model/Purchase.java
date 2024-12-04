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
public class Purchase extends Transaction {

    @OneToMany(mappedBy = "purchase")
    private Collection<PurchaseDetail> purchaseDetails;

}
