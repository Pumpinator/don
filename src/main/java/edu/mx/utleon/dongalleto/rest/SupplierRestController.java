package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/proveedores")
public class SupplierRestController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @GetMapping
    @RequestMapping("/proveedores/{supplierId}/materiaprima")
    public ResponseEntity<?> viewSuppliers(@PathVariable Integer supplierId) {
        return ResponseEntity.ok(rawMaterialService.listBySupplierId(supplierId));
    }

    @GetMapping
    @RequestMapping("/materiaprima/{rawMaterialId}/proveedores")
    public ResponseEntity<?> listSuppliersByRawMaterialId(@PathVariable Integer rawMaterialId) {
        RawMaterial rawMaterial = rawMaterialService.getRawMaterialWithSuppliers(rawMaterialId);
        return ResponseEntity.ok(rawMaterial.getSuppliers());
    }


}

