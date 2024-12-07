package edu.mx.utleon.dongalleto.dto;

import lombok.*;
import lombok.experimental.SuperBuilder;

import java.util.Collection;

@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class RawMaterialInventoryDto extends MeasurableDto {

        private Integer rawMaterialId;
        private Collection<RawMaterialInventoryItemDto> items;

        public double getQuantity() {
            return items.stream().mapToDouble(RawMaterialInventoryItemDto::getQuantity).sum();
        }
}
