package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

import java.util.Collection;

@SuperBuilder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class PurchaseDto extends TransactionDto {

    private Integer supplierId;
    private Integer rawMaterialId;
    private Collection<PurchaseItemDto> items;

}
