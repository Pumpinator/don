package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

import java.util.List;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class SaleDto extends TransactionDto {
    private List<SaleDetailItemDto> items;
}
