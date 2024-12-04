package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

@SuperBuilder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class TransactionDto {

    private Integer id;
    private double unitPrice;
    private double totalPrice;
    private double quantity;
    private Integer measureId;

}
