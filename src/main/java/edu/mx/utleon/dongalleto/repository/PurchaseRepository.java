package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Purchase;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PurchaseRepository extends CrudRepository<Purchase, Integer> {
}
