package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.RawMaterialInventory;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.Optional;

@Repository
public interface RawMaterialInventoryRepository extends CrudRepository<RawMaterialInventory, Integer> {
    Optional<RawMaterialInventory> findByRawMaterialId(Integer id);

    Integer countAllByExpirationDateBetween(LocalDate startDate, LocalDate endDate);

    Integer countAllByExpirationDateBefore(LocalDate date);

    int countAllByRawMaterialNameAndQuantityLessThan(String name, double quantity);

    Iterable<RawMaterialInventory> findAllByQuantityLessThanOrExpirationDateBefore(double quantity, LocalDate date);

    Iterable<RawMaterialInventory> findAllByRawMaterialNameContaining(String searchParam);
}