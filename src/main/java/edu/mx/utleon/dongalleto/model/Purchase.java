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
public class Purchase extends Transaction {

    @OneToMany(mappedBy = "purchase")
    private Collection<PurchaseDetail> purchaseDetails;

}
