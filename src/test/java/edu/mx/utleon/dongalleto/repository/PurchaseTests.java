package edu.mx.utleon.dongalleto.repository;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import edu.mx.utleon.dongalleto.model.*;
import jakarta.transaction.Transactional;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.annotation.Rollback;

import java.time.Instant;
import java.util.List;
import java.util.Map;

@DataJpaTest(showSql = false)
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Rollback(false)
public class PurchaseTests {

    @Autowired
    IngredientRepository ingredientRepository;

    @Autowired
    RecipeRepository recipeRepository;

    @Autowired
    PurchaseRepository purchaseRepository;

    @Autowired
    PurchaseDetailRepository purchaseDetailRepository;

    @Autowired
    ProductionRepository productionRepository;

    @Autowired
    RawMaterialRepository rawMaterialRepository;

    @Autowired
    RawMaterialInventoryRepository rawMaterialInventoryRepository;

    @Autowired
    MeasureRepository measureRepository;

    @Autowired
    SupplierRepository supplierRepository;

    @Test
    @Transactional
    void testPurchase() {
        Iterable<RawMaterial> rawMaterial = rawMaterialRepository.findAll();
        Measure kilogram = measureRepository.findByName(Measures.Kilogramo.name()).orElse(Measure.builder().name(Measures.Kilogramo.name()).symbol("kg").build());
        RawMaterial flour = rawMaterial.iterator().next();
        Supplier costco = supplierRepository.findByName("Costco").orElse(Supplier.builder().name("Costco").build());
        List<PurchaseDetail> purchaseDetails = List.of(
                PurchaseDetail.builder().rawMaterial(flour).quantity(10).measure(kilogram).totalPrice(880).supplier(costco).build()
        );

        double total = purchaseDetails.stream().mapToDouble(PurchaseDetail::getSubtotal).sum();

        Purchase purchase = Purchase.builder()
                .date(Instant.now())
                .purchaseDetails(purchaseDetails)
                .total(total)
                .build();

        Integer purchaseId = 1; // purchaseRepository.save(purchase).getId();
        purchase.setId(purchaseId);

        purchaseDetails = (List<PurchaseDetail>) purchase.getPurchaseDetails();
        purchaseDetails.forEach(purchaseDetail -> {
                    RawMaterialInventory rawMaterialInventory = rawMaterialInventoryRepository.findByRawMaterialId(purchaseDetail
                                    .getRawMaterial().getId())
                            .orElse(RawMaterialInventory.builder().id(1).quantity(0).rawMaterial(purchaseDetail.getRawMaterial()).build());
                    double newQuantity = rawMaterialInventory.getQuantity() - purchaseDetail.getQuantity();
                    if (newQuantity > rawMaterialInventory.getQuantity()) throw new RuntimeException("Insufficient inventory");
                    purchaseDetail.setId(PurchaseDetail.PurchaseDetailId.builder().purchase(purchaseId).rawMaterial(purchaseDetail.getRawMaterial().getId()).build());
                }
        );

        purchase.setPurchaseDetails(purchaseDetails);

        System.out.println(purchase);
    }

}

