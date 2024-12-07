package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.RawMaterialInventoryItemDto;
import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.model.RawMaterialInventory;
import edu.mx.utleon.dongalleto.model.Supplier;
import edu.mx.utleon.dongalleto.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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

    public RawMaterialInventoryItemDto saveInventory(RawMaterialInventoryItemDto item) {
        if (item.getId() != null) {
            RawMaterialInventory rawMaterialInventory = rawMaterialInventoryRepository.findById(item.getId()).orElseThrow();
            rawMaterialInventory.setQuantity(item.getQuantity());
            rawMaterialInventory.setCost(item.getTotalPrice());
            rawMaterialInventory.setExpirationDate(item.getExpirationDate());
            rawMaterialInventory.setMeasure(measureRepository.findByName(item.getMeasureName()).orElseThrow());
            return toDto(rawMaterialInventoryRepository.save(rawMaterialInventory));
        }
        if (item.getSupplierId() != null) {
            return toDto(rawMaterialInventoryRepository.save(RawMaterialInventory.builder()
                    .rawMaterial(rawMaterialRepository.findById(item.getRawMaterialId()).orElse(null))
                    .supplier(supplierRepository.findById(item.getSupplierId()).orElse(null))
                    .quantity(item.getQuantity())
                    .cost(item.getTotalPrice())
                    .expirationDate(item.getExpirationDate())
                    .measure(measureRepository.findByName(item.getMeasureName()).orElseThrow())
                    .build()));
        } else {
            return toDto(rawMaterialInventoryRepository.save(RawMaterialInventory.builder()
                    .rawMaterial(rawMaterialRepository.findById(item.getRawMaterialId()).orElse(null))
                    .quantity(item.getQuantity())
                    .cost(item.getTotalPrice())
                    .expirationDate(item.getExpirationDate())
                    .measure(measureRepository.findByName(item.getMeasureName()).orElseThrow())
                    .build()));
        }
    }

    public RawMaterialInventoryItemDto getInventory(Integer id) {
        return toDto(rawMaterialInventoryRepository.findById(id).orElseThrow());
    }

    private RawMaterialInventoryItemDto toDto(RawMaterialInventory rawMaterialInventory) {
        System.out.println(rawMaterialInventory.getExpirationDate());
        return RawMaterialInventoryItemDto.builder()
                .id(rawMaterialInventory.getId())
                .rawMaterialId(rawMaterialInventory.getRawMaterial().getId())
                .supplierId(rawMaterialInventory.getSupplier() != null ? rawMaterialInventory.getSupplier().getId() : null)
                .quantity(rawMaterialInventory.getQuantity())
                .totalPrice(rawMaterialInventory.getCost())
                .expirationDate(rawMaterialInventory.getExpirationDate())
                .measureName(rawMaterialInventory.getMeasure().getName())
                .measureSymbol(rawMaterialInventory.getMeasure().getSymbol())
                .build();
    }

}
