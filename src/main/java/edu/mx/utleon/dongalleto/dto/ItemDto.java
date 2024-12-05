package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

import java.time.LocalDate;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public abstract class ItemDto {

    private double unitPrice;
    private double totalPrice;
    private double quantity;
    private String measureName;
    private LocalDate expirationDate;

}
