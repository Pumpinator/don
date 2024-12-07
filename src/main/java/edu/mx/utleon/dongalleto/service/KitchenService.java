package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.model.Ingredient;
import edu.mx.utleon.dongalleto.model.Measure;
import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.model.Recipe;
import edu.mx.utleon.dongalleto.repository.IngredientRepository;
import edu.mx.utleon.dongalleto.repository.MeasureRepository;
import edu.mx.utleon.dongalleto.repository.RawMaterialRepository;
import edu.mx.utleon.dongalleto.repository.RecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class KitchenService {

    @Autowired
    private RecipeRepository recipeRepository;

    @Autowired
    private RawMaterialRepository rawMaterialRepository;

    @Autowired
    private IngredientRepository ingredientRepository;

    @Autowired
    private MeasureRepository measureRepository;

    public Iterable<Recipe> getRecipes() {
        return recipeRepository.findAll();
    }

    public Iterable<RawMaterial> getRawMaterial() {
        return rawMaterialRepository.findAll();
    }

    public Iterable<Ingredient> getIngredients() {
        return ingredientRepository.findAll();
    }

    public Iterable<Measure> getMeasures() {
        return measureRepository.findAll();
    }

}
