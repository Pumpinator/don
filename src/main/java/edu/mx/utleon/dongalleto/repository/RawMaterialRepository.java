package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.RawMaterial;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface RawMaterialRepository extends CrudRepository<RawMaterial, Integer> {

    Optional<RawMaterial> findByName(String name);

    Iterable<RawMaterial> findAllBySuppliersId(Integer supplierId);

    Iterable<RawMaterial> findAllByNameContaining(String searchParam);
}
