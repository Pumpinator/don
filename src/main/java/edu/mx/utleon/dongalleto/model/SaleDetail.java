package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class SaleDetail extends TransactionDetail {

    @EmbeddedId
    private SaleDetailId id;

    @ManyToOne
    @MapsId("cookie")
    @JoinColumn(name = "cookie_id")
    private Cookie cookie;

    @ManyToOne
    @MapsId("sale")
    @JoinColumn(name = "sale_id")
    private Sale sale;

    @Embeddable
    @NoArgsConstructor
    @AllArgsConstructor
    @Getter
    @Setter
    @EqualsAndHashCode
    @ToString
    public static class SaleDetailId {

        @Column(name = "cookie_id")
        private Integer cookie;

        @Column(name = "sale_id")
        private Integer sale;

    }
}