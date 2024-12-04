package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.PurchaseItemDto;
import edu.mx.utleon.dongalleto.model.*;
import edu.mx.utleon.dongalleto.repository.*;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class PurchaseService {

    @Autowired
    RawMaterialRepository rawMaterialRepository;

    @Autowired
    RawMaterialInventoryRepository rawMaterialInventoryRepository;

    @Autowired
    MeasureRepository measureRepository;

    @Autowired
    SupplierRepository supplierRepository;

    @Autowired
    PurchaseRepository purchaseRepository;
    @Autowired
    private PurchaseDetailRepository purchaseDetailRepository;

    @Transactional
    public Purchase add(Collection<PurchaseItemDto> purchaseItems) {
        Purchase purchase = purchaseRepository.save(Purchase.builder()
                .date(Instant.now())
                .build());

        List<PurchaseDetail> purchaseDetails = purchaseItems.stream().map(item -> {
            RawMaterial rawMaterial = rawMaterialRepository.findById(item.getRawMaterialId())
                    .orElseThrow(() -> new RuntimeException("Raw material not found"));

            Measure measure = measureRepository.findByName(item.getMeasureName())
                    .orElseThrow(() -> new RuntimeException("Measure not found"));

            Supplier supplier = supplierRepository.findById(item.getSupplierId())
                    .orElseThrow(() -> new RuntimeException("Supplier not found"));

            double unitPrice = item.getUnitPrice() == 0 ? item.getTotalPrice() / item.getQuantity() : item.getUnitPrice();
            double totalPrice = item.getTotalPrice() == 0 ? unitPrice * item.getQuantity() : item.getTotalPrice();
            double quantity = item.getQuantity();

            rawMaterialInventoryRepository.save(RawMaterialInventory.builder()
                    .purchase(purchase)
                    .rawMaterial(rawMaterial)
                    .quantity(quantity)
                    .measure(measure)
                    .cost(totalPrice)
                    .expirationDate(item.getExpirationDate())
                    .build());


            return purchaseDetailRepository.save(PurchaseDetail.builder()
                    .id(PurchaseDetail.PurchaseDetailId.builder().rawMaterial(rawMaterial.getId()).purchase(purchase.getId()).build())
                    .rawMaterial(rawMaterial)
                    .quantity(quantity)
                    .unitPrice(unitPrice)
                    .totalPrice(totalPrice)
                    .measure(measure)
                    .supplier(supplier)
                    .purchase(purchase)
                    .build());
        }).collect(Collectors.toList());

        double total = purchaseDetails.stream().mapToDouble(PurchaseDetail::getTotalPrice).sum();
        purchase.setTotal(total);
        purchase.setPurchaseDetails(purchaseDetails);
        return purchaseRepository.save(purchase);
    }

    public Iterable<Purchase> list() {
        return purchaseRepository.findAll();
    }

}
