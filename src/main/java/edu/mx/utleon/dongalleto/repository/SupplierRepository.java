package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Measure;
import edu.mx.utleon.dongalleto.model.Supplier;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SupplierRepository extends CrudRepository<Supplier, Integer> {
}
