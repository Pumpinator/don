package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class SaleDetailItemDto extends ItemDto {
    private Integer cookieId;
    private Integer saleId;
}
