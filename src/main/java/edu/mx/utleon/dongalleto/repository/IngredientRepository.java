package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Ingredient;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Collection;

@Repository
public interface IngredientRepository extends CrudRepository<Ingredient, Ingredient.IngredientId> {
    Collection<Ingredient> findAllByRecipeId(Integer recipeId);
}
