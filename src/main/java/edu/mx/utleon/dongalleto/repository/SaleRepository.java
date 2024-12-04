package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Sale;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SaleRepository extends CrudRepository<Sale, Integer> {
}
