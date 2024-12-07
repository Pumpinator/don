package edu.mx.utleon.dongalleto.component;

import edu.mx.utleon.dongalleto.model.*;
import edu.mx.utleon.dongalleto.repository.*;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.Collection;
import java.util.List;

@Component
@RequiredArgsConstructor
public class DataComponent {

    private final MeasureRepository measureRepository;
    private final RawMaterialRepository rawMaterialRepository;
    private final SupplierRepository supplierRepository;
    private final RawMaterialInventoryRepository rawMaterialInventoryRepository;
    private final CookieRepository cookieRepository;
    private final RecipeRepository recipeRepository;
    private final IngredientRepository ingredientRepository;
    private static final Logger logger = LoggerFactory.getLogger(DataComponent.class);
    private final ProductionRepository productionRepository;
    private final CookieInventoryRepository cookieInventoryRepository;

    @EventListener
    public void createData(ApplicationReadyEvent event) {
        logger.info("Looking and creating initial data... ⚙️");

        Measure gram = createMeasure(Measure.builder().name(Measures.Gramo.name()).symbol(Symbols.gr.name()).build());
        Measure kilogram = createMeasure(Measure.builder().name(Measures.Kilogramo.name()).symbol(Symbols.kg.name()).build());
        Measure milliliter = createMeasure(Measure.builder().name(Measures.Mililitro.name()).symbol(Symbols.ml.name()).build());
        Measure liter = createMeasure(Measure.builder().name(Measures.Litro.name()).symbol(Symbols.lt.name()).build());
        Measure cup = createMeasure(Measure.builder().name(Measures.Taza.name()).symbol(Symbols.tza.name()).build());
        Measure piece = createMeasure(Measure.builder().name(Measures.Pieza.name()).symbol(Symbols.pz.name()).build());

        RawMaterial flour = createRawMaterial(RawMaterial.builder().name("Harina").build());
        RawMaterial sugar = createRawMaterial(RawMaterial.builder().name("Azúcar").build());
        RawMaterial butter = createRawMaterial(RawMaterial.builder().name("Mantequilla").build());
        RawMaterial eggs = createRawMaterial(RawMaterial.builder().name("Huevos").build());
        RawMaterial milk = createRawMaterial(RawMaterial.builder().name("Leche").build());
        RawMaterial condensedMilk = createRawMaterial(RawMaterial.builder().name("Leche condensada").build());
        RawMaterial bakingPowder = createRawMaterial(RawMaterial.builder().name("Polvo para hornear").build());
        RawMaterial vanilla = createRawMaterial(RawMaterial.builder().name("Vainilla").build());
        RawMaterial salt = createRawMaterial(RawMaterial.builder().name("Sal").build());
        RawMaterial oat = createRawMaterial(RawMaterial.builder().name("Avena").build());
        RawMaterial raisins = createRawMaterial(RawMaterial.builder().name("Pasas").build());
        RawMaterial nuts = createRawMaterial(RawMaterial.builder().name("Nueces").build());
        RawMaterial chocolateChips = createRawMaterial(RawMaterial.builder().name("Chispas de Chocolate").build());
        RawMaterial coloredChips = createRawMaterial(RawMaterial.builder().name("Chispas de Colores").build());

        Supplier proveedorHarinas = createSupplier(Supplier.builder().name("Proveedor de Harinas S. A. de C. V.").contact("4771234567").type("Empresa").rawMaterial(
                List.of(flour, oat, salt)
        ).build());
        Supplier proveedorDulces = createSupplier(Supplier.builder().name("Proveedor de Dulces S. A. de C. V.").contact("4777654321").type("Empresa").rawMaterial(
                List.of(sugar, bakingPowder, vanilla, raisins, nuts, chocolateChips, coloredChips)
        ).build());
        Supplier proveedorLacteos = createSupplier(Supplier.builder().name("Proveedor de Lácteos S. A. de C. V.").contact("4777654321").type("Empresa").rawMaterial(
                List.of(butter, eggs, milk, condensedMilk)
        ).build());
        Supplier costco = createSupplier(Supplier.builder().name("Costco Wholesale").contact("4777654321").type("Mercado").rawMaterial(
                List.of(flour, sugar, butter, eggs, milk, condensedMilk, bakingPowder, vanilla, salt, oat, raisins, nuts, chocolateChips, coloredChips)
        ).build());
        Supplier walmart = createSupplier(Supplier.builder().name("Walmart").contact("4777654321").type("Mercado").rawMaterial(
                List.of(flour, sugar, butter, eggs, milk, condensedMilk, bakingPowder, vanilla, salt, oat, raisins, nuts, chocolateChips, coloredChips)
        ).build());

        RawMaterialInventory flourInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(flour).quantity(10000).measure(gram).cost(160).supplier(proveedorHarinas).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory sugarInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(sugar).quantity(10000).measure(gram).cost(360).supplier(proveedorDulces).build());
        RawMaterialInventory butterInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(butter).quantity(10000).measure(gram).cost(2400).supplier(proveedorLacteos).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory eggsInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(eggs).quantity(180).measure(piece).cost(560).supplier(proveedorLacteos).expirationDate(LocalDate.now().plusMonths(1)).build());
        RawMaterialInventory milkInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(milk).quantity(10).measure(liter).cost(250).supplier(proveedorLacteos).expirationDate(LocalDate.now().plusMonths(1)).build());
        RawMaterialInventory condensedMilkInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(condensedMilk).quantity(10).measure(liter).cost(650).supplier(proveedorLacteos).expirationDate(LocalDate.now().plusMonths(1)).build());
        RawMaterialInventory bakingPowderInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(bakingPowder).quantity(10000).measure(gram).cost(2000).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory vanillaInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(vanilla).quantity(1000).measure(gram).cost(1000).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory saltInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(salt).quantity(10000).measure(gram).cost(600).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory oatInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(oat).quantity(10000).measure(gram).cost(650).supplier(proveedorHarinas).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory raisinsInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(raisins).quantity(10000).measure(gram).cost(650).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory nutsInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(nuts).quantity(10000).measure(gram).cost(6000).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory chocolateChipsInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(chocolateChips).quantity(10000).measure(gram).cost(650).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());
        RawMaterialInventory coloredChipsInventory = createRawMaterialInventory(RawMaterialInventory.builder().rawMaterial(coloredChips).quantity(10000).measure(gram).cost(650).supplier(proveedorDulces).expirationDate(LocalDate.now().plusMonths(6)).build());

        Cookie chocolateCookie = createCookie(Cookie.builder().name("Chispas de Chocolate").build());
        Cookie oatmealAndRaisinsCookie = createCookie(Cookie.builder().name("Avena y Pasas").build());
        Cookie nutsCookie = createCookie(Cookie.builder().name("Nueces").build());
        Cookie specialCookie = createCookie(Cookie.builder().name("Especial").build());

        Recipe nutsCookieRecipe = createRecipe(Recipe.builder()
                .name("Nueces")
                .cookie(nutsCookie)
                .quantity(750)
                .measure(piece)
                .instructions(
                        "1) Precalienta el horno a 180°C (350°F).\n" +
                                "2) Tamiza la harina, el polvo para hornear y la sal en un tazón grande.\n" +
                                "4) Bate la mantequilla y el azúcar en otro tazón hasta obtener una mezcla cremosa.\n" +
                                "4) Añade la esencia de vainilla y continúa batiendo.\n" +
                                "5) Incorpora la mezcla de harina poco a poco, alternando con la leche, hasta que se forme una masa uniforme.\n" +
                                "6) Añade las nueces troceadas y mezcla bien.\n" +
                                "7) Forma bolitas de masa del tamaño deseado (aproximadamente de 30 a 40 gramos cada una.\n" +
                                "8) Coloca las bolitas en una bandeja para hornear, dejando espacio entre ellas para que se expandan durante el horneado.\n" +
                                "9) Hornea las galletas durante 12-15 minutos o hasta que estén doradas en los bordes.\n" +
                                "10) Deja enfriar las galletas en una rejilla antes de servir."
                )
                .build()
        );

        nutsCookieRecipe.setIngredients(createIngredients(List.of(
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(flour.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(flour).measure(kilogram).quantity(5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(butter.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(butter).measure(kilogram).quantity(2.5).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(sugar.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(sugar).measure(kilogram).quantity(2.5).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(nuts.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(nuts).measure(kilogram).quantity(1.5).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(milk.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(milk).measure(liter).quantity(1).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(flour.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(flour).measure(gram).quantity(50).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(bakingPowder.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).rawMaterial(bakingPowder).measure(gram).quantity(50).recipe(nutsCookieRecipe).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(vanilla.getId()).recipe(nutsCookieRecipe.getId()).build()).recipe(nutsCookieRecipe).measure(gram).rawMaterial(vanilla).quantity(20).recipe(nutsCookieRecipe).build()
        )));

        Recipe oatmealAndRaisinsRecipe = createRecipe(Recipe.builder()
                .name("Avena y Pasas")
                .cookie(oatmealAndRaisinsCookie)
                .quantity(750) // 30 kg de galletas
                .measure(piece)
                .instructions(
                        "1) Precalienta el horno a 180°C (350°F).\n" +
                                "2) Tamiza la harina, el polvo para hornear y la sal en un tazón grande.\n" +
                                "3) Mezcla la mantequilla y el azúcar hasta que quede cremosa.\n" +
                                "4) Añade los huevos y la vainilla, y mezcla bien.\n" +
                                "5) Añade la avena, las pasas y mezcla bien.\n" +
                                "6) Forma bolitas y colócalas en la bandeja.\n" +
                                "7) Hornea 12-15 minutos o hasta que estén doradas.\n" +
                                "8) Deja enfriar antes de servir."
                )
                .build()
        );

        oatmealAndRaisinsRecipe.setIngredients(createIngredients(List.of(
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(flour.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(flour).measure(kilogram).quantity(5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(butter.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(butter).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(sugar.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(sugar).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(oat.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(oat).measure(kilogram).quantity(1.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(raisins.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(raisins).measure(kilogram).quantity(1.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(milk.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(milk).measure(liter).quantity(1).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(bakingPowder.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(bakingPowder).measure(gram).quantity(50).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(vanilla.getId()).recipe(oatmealAndRaisinsRecipe.getId()).build()).recipe(oatmealAndRaisinsRecipe).rawMaterial(vanilla).measure(gram).quantity(20).build()
        )));

        Recipe chocolateCookieRecipe = createRecipe(Recipe.builder()
                .name("Chispas de Chocolate")
                .cookie(chocolateCookie)
                .quantity(750) // 30 kg de galletas
                .measure(piece)
                .instructions(
                        "1) Precalienta el horno a 180°C (350°F).\n" +
                                "2) Tamiza la harina, el polvo para hornear y la sal en un tazón grande.\n" +
                                "3) Bate la mantequilla y el azúcar hasta obtener una mezcla cremosa.\n" +
                                "4) Añade los huevos y la esencia de vainilla y bate hasta integrar.\n" +
                                "5) Incorpora la mezcla de harina poco a poco hasta formar una masa uniforme.\n" +
                                "6) Añade las chispas de chocolate y mezcla bien.\n" +
                                "7) Forma bolitas de masa del tamaño deseado y colócalas en una bandeja para hornear.\n" +
                                "8) Hornea las galletas durante 12-15 minutos.\n" +
                                "9) Deja enfriar antes de servir."
                )
                .build()
        );

        chocolateCookieRecipe.setIngredients(createIngredients(List.of(
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(flour.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(flour).measure(kilogram).quantity(5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(butter.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(butter).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(sugar.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(sugar).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(chocolateChips.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(chocolateChips).measure(kilogram).quantity(1.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(milk.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(milk).measure(liter).quantity(1).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(bakingPowder.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(bakingPowder).measure(gram).quantity(50).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(vanilla.getId()).recipe(chocolateCookieRecipe.getId()).build()).recipe(chocolateCookieRecipe).rawMaterial(vanilla).measure(gram).quantity(20).build()
        )));

        Recipe specialCookieRecipe = createRecipe(Recipe.builder()
                .name("Especial - Chispas de Colores")
                .cookie(specialCookie)
                .quantity(750) // 30 kg de galletas
                .measure(piece)
                .instructions(
                        "1) Precalienta el horno a 180°C (350°F).\n" +
                                "2) Tamiza la harina, el polvo para hornear y la sal en un tazón grande.\n" +
                                "3) Bate la mantequilla y el azúcar hasta obtener una mezcla cremosa.\n" +
                                "4) Añade los huevos y la esencia de vainilla y bate hasta integrar.\n" +
                                "5) Incorpora la mezcla de harina poco a poco, alternando con la leche, hasta que se forme una masa uniforme.\n" +
                                "6) Agrega las chispas de colores y mezcla bien.\n" +
                                "7) Forma bolitas de masa del tamaño deseado y colócalas en una bandeja para hornear.\n" +
                                "8) Hornea las galletas durante 12-15 minutos o hasta que estén doradas en los bordes.\n" +
                                "9) Deja enfriar las galletas en una rejilla antes de servir."
                )
                .build()
        );

        specialCookieRecipe.setIngredients(createIngredients(List.of(
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(flour.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(flour).measure(kilogram).quantity(5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(butter.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(butter).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(sugar.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(sugar).measure(kilogram).quantity(2.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(coloredChips.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(coloredChips).measure(kilogram).quantity(1.5).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(milk.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(milk).measure(liter).quantity(1).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(bakingPowder.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(bakingPowder).measure(gram).quantity(50).build(),
                Ingredient.builder().id(Ingredient.IngredientId.builder().rawMaterial(vanilla.getId()).recipe(specialCookieRecipe.getId()).build()).recipe(specialCookieRecipe).rawMaterial(vanilla).measure(gram).quantity(20).build()
        )));

        Production nutsCookieProduction = createProduction(Production.builder().creationDate(LocalDate.now()).recipe(nutsCookieRecipe).build());


        CookieInventory nutsCookieInventory = createCookieInventory(CookieInventory.builder().cookie(nutsCookie).quantity(nutsCookieProduction.getRecipe().getQuantity()).measure(nutsCookieProduction.getRecipe().getMeasure()).cost(nutsCookieProduction.getRecipe().getIngredients().stream().mapToDouble(i -> i.getQuantity() * rawMaterialInventoryRepository.findByRawMaterialId(i.getRawMaterial().getId()).orElseThrow().getCost()).sum()).production(nutsCookieProduction).build());
        nutsCookie.setPrice(nutsCookieInventory.getCost() * 1.2);
        cookieRepository.save(nutsCookie);

        logger.info("Initial data loaded and created ✅");
    }

    private CookieInventory createCookieInventory(CookieInventory build) {
        CookieInventory cookieInventory = cookieInventoryRepository.findByCookieId(build.getCookie().getId()).orElse(null);
        if (cookieInventory == null) {
            cookieInventory = cookieInventoryRepository.save(build);
        }
        return cookieInventory;
    }

    private Production createProduction(Production p) {
        Production production = productionRepository.findByRecipeCookieId(p.getRecipe().getCookie().getId()).orElse(null);
        if (production == null) {
            production = productionRepository.save(p);
        }
        return production;

    }

    private Collection<Ingredient> createIngredients(Collection<Ingredient> ingredients) {
        ingredients.forEach(i -> {
            Ingredient ingredient = ingredientRepository.findById(i.getId()).orElse(null);
            if (ingredient == null) {
                ingredientRepository.save(i);
            }
        });
        return ingredients;
    }

    private Recipe createRecipe(Recipe r) {
        Recipe recipe = recipeRepository.findByCookieId(r.getCookie().getId()).orElse(null);
        if (recipe == null) {
            recipe = recipeRepository.save(r);
        }
        return recipe;
    }

    private Cookie createCookie(Cookie c) {
        Cookie cookie = cookieRepository.findByName(c.getName()).orElse(null);
        if (cookie == null) {
            cookie = cookieRepository.save(c);
        }
        return cookie;
    }

    private RawMaterialInventory createRawMaterialInventory(RawMaterialInventory rmi) {
        RawMaterialInventory rawMaterialInventory = rawMaterialInventoryRepository.findByRawMaterialId(rmi.getRawMaterial().getId()).orElse(null);
        if (rawMaterialInventory == null) {
            rawMaterialInventory = rawMaterialInventoryRepository.save(rmi);
        }
        return rawMaterialInventory;
    }

    private RawMaterial createRawMaterial(RawMaterial rm) {
        RawMaterial rawMaterial = rawMaterialRepository.findByName(rm.getName()).orElse(null);
        if (rawMaterial == null) {
            rawMaterial = rawMaterialRepository.save(rm);
        }
        return rawMaterial;
    }

    private Supplier createSupplier(Supplier s) {
        Supplier supplier = supplierRepository.findByName(s.getName()).orElse(null);
        if (supplier == null) {
            supplier = supplierRepository.save(s);
        }
        return supplier;
    }

    private Measure createMeasure(Measure m) {
        Measure measure = measureRepository.findByName(m.getName()).orElse(null);
        if (measure == null) {
            measure = measureRepository.save(m);
        }
        return measure;
    }

}
