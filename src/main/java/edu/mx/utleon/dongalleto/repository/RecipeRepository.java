package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Recipe;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface RecipeRepository extends CrudRepository<Recipe, Integer> {
    Optional<Recipe> findByCookieId(Integer cookieId);

    Optional<Recipe> findByName(String name);
}
