package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.PurchaseItemDto;
import edu.mx.utleon.dongalleto.model.Purchase;
import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.model.RawMaterialInventory;
import edu.mx.utleon.dongalleto.model.Supplier;
import edu.mx.utleon.dongalleto.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDate;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

@Service
public class RawMaterialService {

    @Autowired
    private RawMaterialRepository rawMaterialRepository;

    @Autowired
    private SupplierRepository supplierRepository;

    @Autowired
    private RawMaterialInventoryRepository rawMaterialInventoryRepository;
    @Autowired
    private PurchaseRepository purchaseRepository;
    @Autowired
    private MeasureRepository measureRepository;

    public Iterable<RawMaterialInventory> listInventory() {
        return rawMaterialInventoryRepository.findAll();
    }

    public Iterable<RawMaterial> list() {
        return rawMaterialRepository.findAll();
    }

    public Iterable<RawMaterial> listBySupplierId(Integer supplierId) {
        return rawMaterialRepository.findAllBySuppliersId(supplierId);
    }

    public Iterable<Supplier> listSuppliers(Integer id) {
        return supplierRepository.findAllByRawMaterialId(id);
    }

    public RawMaterial getRawMaterialWithSuppliers(Integer id) {
        RawMaterial rawMaterial = rawMaterialRepository.findById(id).orElseThrow();
        rawMaterial.setSuppliers((Collection<Supplier>) supplierRepository.findAllByRawMaterialId(id));
        return rawMaterial;
    }

    public int countByDates(LocalDate startDate, LocalDate endDate) {
        return rawMaterialInventoryRepository.countAllByExpirationDateBetween(startDate, endDate);
    }

    public int countByDateBefore(LocalDate date) {
        return rawMaterialInventoryRepository.countAllByExpirationDateBefore(date);
    }

    public int countLowStockAndExpiredByName(double quantity) {
        Iterable<RawMaterialInventory> lowStockAndExpired = rawMaterialInventoryRepository.findAllByQuantityLessThanOrExpirationDateBefore(quantity, LocalDate.now());
        Set<String> uniqueRawMaterials = new HashSet<>();
        for (RawMaterialInventory item : lowStockAndExpired) {
            uniqueRawMaterials.add(item.getRawMaterial().getName());
        }
        return uniqueRawMaterials.size();
    }

    public Iterable<RawMaterialInventory> searchInventory(String searchParam) {
        return rawMaterialInventoryRepository.findAllByRawMaterialNameContaining(searchParam);
    }

    public Iterable<RawMaterial> search(String searchParam) {
        return rawMaterialRepository.findAllByNameContaining(searchParam);
    }

    public RawMaterialInventory addInventory(PurchaseItemDto item) {
        if (purchaseRepository.findById(item.getTransactionId()).isEmpty()) {
            Purchase purchase = purchaseRepository.save(
                    Purchase.builder().date(Instant.now()).total(item.getTotalPrice()).build());
            return rawMaterialInventoryRepository.save(RawMaterialInventory.builder()
                    .rawMaterial(rawMaterialRepository.findById(item.getRawMaterialId()).orElseThrow())
                    .quantity(item.getQuantity())
                    .cost(item.getTotalPrice())
                    .expirationDate(item.getExpirationDate())
                    .purchase(purchase)
                    .measure(measureRepository.findByName(item.getMeasureName()).orElseThrow())
                    .build());
        }
        return rawMaterialInventoryRepository.save(RawMaterialInventory.builder()
                .rawMaterial(rawMaterialRepository.findById(item.getRawMaterialId()).orElseThrow())
                .quantity(item.getQuantity())
                .cost(item.getTotalPrice())
                .expirationDate(item.getExpirationDate())
                .purchase(purchaseRepository.findById(item.getTransactionId()).orElseThrow())
                .measure(measureRepository.findByName(item.getMeasureName()).orElseThrow())
                .build());
    }
}
