package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.dto.RawMaterialInventoryItemDto;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/inventario")
public class InventoryRestController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @GetMapping
    @RequestMapping("/materiaprima/{searchParam}")
    public ResponseEntity<?> searchRawMaterialInventory(@PathVariable String searchParam) {
        return ResponseEntity.ok(rawMaterialService.searchInventory(searchParam));
    }

    @PostMapping
    @RequestMapping("/materiaprima")
    public ResponseEntity<?> addRawMaterialInventory(@RequestBody RawMaterialInventoryItemDto item) {
        return ResponseEntity.ok(rawMaterialService.addInventory(item));
    }


}
