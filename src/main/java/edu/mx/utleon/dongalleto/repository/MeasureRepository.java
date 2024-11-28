package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Measure;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MeasureRepository extends CrudRepository<Measure, Integer> {
}
