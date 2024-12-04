package edu.mx.utleon.dongalleto.model;

import jakarta.persistence.Entity;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.*;
import lombok.experimental.SuperBuilder;

@Entity
@SuperBuilder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class CookieInventory extends Inventory {

    @ManyToOne
    @JoinColumn(name = "cookie_id", nullable = false)
    private Cookie cookie;

    @ManyToOne
    @JoinColumn(name = "production_id", nullable = false)
    private Production production;

}
