package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Losses;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LossesRepository extends CrudRepository<Losses, Integer> {
}
