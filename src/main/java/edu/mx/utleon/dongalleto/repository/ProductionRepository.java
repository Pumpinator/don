package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Production;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductionRepository extends CrudRepository<Production, Integer> {
}
