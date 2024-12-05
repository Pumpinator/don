package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class RawMaterialInventoryItemDto extends ItemDto {

    private Integer rawMaterialId;
    private Integer supplierId;

}
