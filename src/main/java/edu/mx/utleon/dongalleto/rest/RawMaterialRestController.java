package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.dto.PurchaseItemDto;
import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.model.RawMaterialInventory;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class RawMaterialRestController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @GetMapping
    @RequestMapping("/materiaprima/{rawMaterialId}/proveedores")
    public ResponseEntity<?> listSuppliersByRawMaterialId(@PathVariable Integer rawMaterialId) {
        RawMaterial rawMaterial = rawMaterialService.getRawMaterialWithSuppliers(rawMaterialId);
        return ResponseEntity.ok(rawMaterial.getSuppliers());
    }

    @GetMapping
    @RequestMapping("/proveedores/{supplierId}/materiaprima")
    public ResponseEntity<?> viewSuppliers(@PathVariable Integer supplierId) {
        return ResponseEntity.ok(rawMaterialService.listBySupplierId(supplierId));
    }

    @GetMapping
    @RequestMapping("/materiaprima/{searchParam}/inventario")
    public ResponseEntity<?> searchRawMaterialInventory(@PathVariable String searchParam) {
        return ResponseEntity.ok(rawMaterialService.searchInventory(searchParam));
    }

    @PostMapping
    @RequestMapping("/materiaprima/inventario")
    public ResponseEntity<?> addRawMaterialInventory(@RequestBody PurchaseItemDto item) {
        return ResponseEntity.ok(rawMaterialService.addInventory(item));
    }

    @GetMapping
    @RequestMapping("/materiaprima/{searchParam}")
    public ResponseEntity<?> searchRawMaterial(@PathVariable String searchParam) {
        return ResponseEntity.ok(rawMaterialService.search(searchParam));
    }

}
