// src/main/java/edu/mx/utleon/dongalleto/service/CookieService.java

package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.CookieDto;
import edu.mx.utleon.dongalleto.model.*;
import edu.mx.utleon.dongalleto.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CookieService {

    @Autowired
    private CookieRepository cookieRepository;

    @Autowired
    private MeasureRepository measureRepository;

    @Autowired
    private RecipeRepository recipeRepository;

    @Autowired
    private IngredientRepository ingredientRepository;

    @Autowired
    private RawMaterialInventoryRepository rawMaterialInventoryRepository;

    @Autowired
    private ProductionRepository productionRepository;

    public Iterable<CookieDto> search(String searchParam) {
        return ((List<Cookie>) cookieRepository.findAllByNameContaining(searchParam)).stream().map(this::toDto).toList();
    }

    private CookieDto toDto(Cookie cookie) {
        return CookieDto.builder()
                .id(cookie.getId())
                .name(cookie.getName())
                .price(cookie.getPrice())
                .build();
    }

    public Iterable<Measure> getMeasures() {
        return measureRepository.findAll();
    }

    public Recipe getRecipe(Integer cookieId) {
        return recipeRepository.findByCookieId(cookieId).orElseThrow();
    }

    public double getPrice(Integer cookieId) {
        Recipe recipe = recipeRepository.findByCookieId(cookieId).orElseThrow();
        double totalCost = 0.0;
        for (Ingredient ingredient : recipe.getIngredients()) {
            RawMaterialInventory rawMaterialInventory = rawMaterialInventoryRepository.findByRawMaterialId(ingredient.getRawMaterial().getId()).orElseThrow();
            double ingredientQuantity = ingredient.getQuantity();
            double inventoryQuantity = rawMaterialInventory.getQuantity();

            if (!ingredient.getMeasure().getName().equals(rawMaterialInventory.getMeasure().getName())) {
                inventoryQuantity = convertUnits(inventoryQuantity, rawMaterialInventory.getMeasure(), ingredient.getMeasure());
            }

            double costPerUnit = rawMaterialInventory.getCost() / inventoryQuantity;
            double sum = costPerUnit * ingredientQuantity;
            totalCost += sum;
        }
        totalCost += 300;
        double protection = (double) 83 / 50;
        return (totalCost / recipe.getQuantity()) + protection;
    }

    private double convertUnits(double quantity, Measure fromMeasure, Measure toMeasure) {
        if (fromMeasure.getName().equals(Measures.Kilogramo.name()) && toMeasure.getName().equals(Measures.Gramo.name())) {
            return quantity * 1000;
        }
        if (fromMeasure.getName().equals(Measures.Gramo.name()) && toMeasure.getName().equals(Measures.Kilogramo.name())) {
            return quantity / 1000;
        }
        if (fromMeasure.getName().equals(Measures.Litro.name()) && toMeasure.getName().equals(Measures.Mililitro.name())) {
            return quantity * 1000;
        }
        if (fromMeasure.getName().equals(Measures.Mililitro.name()) && toMeasure.getName().equals(Measures.Litro.name())) {
            return quantity / 1000;
        }
        return quantity;
    }
}