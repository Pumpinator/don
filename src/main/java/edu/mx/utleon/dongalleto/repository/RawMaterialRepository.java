package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.RawMaterial;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RawMaterialRepository extends CrudRepository<RawMaterial, Integer> {
}
