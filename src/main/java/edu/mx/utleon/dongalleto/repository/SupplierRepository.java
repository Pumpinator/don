package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Supplier;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface SupplierRepository extends CrudRepository<Supplier, Integer> {
    Optional<Supplier> findByName(String name);
    Iterable<Supplier> findAllByRawMaterialId(Integer rawMaterialId);
}
