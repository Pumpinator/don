package edu.mx.utleon.dongalleto.dto;

import jakarta.persistence.Column;
import jakarta.persistence.MappedSuperclass;
import lombok.*;
import lombok.experimental.SuperBuilder;

import java.time.Instant;

@MappedSuperclass
@SuperBuilder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public abstract class TransactionDto {

    private Integer id;
    private Instant date;
    private double total;


}
