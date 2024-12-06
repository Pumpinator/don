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
public abstract class ItemDto extends MeasurableDto {

    private double unitPrice;
    private double totalPrice;
    private LocalDate expirationDate;

}
