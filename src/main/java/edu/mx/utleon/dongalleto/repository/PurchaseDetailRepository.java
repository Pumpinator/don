package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.PurchaseDetail;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PurchaseDetailRepository extends CrudRepository<PurchaseDetail, Integer> {
}
