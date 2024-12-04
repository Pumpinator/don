package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.SaleDetail;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SaleDetailRepository extends CrudRepository<SaleDetail, Integer> {
}
