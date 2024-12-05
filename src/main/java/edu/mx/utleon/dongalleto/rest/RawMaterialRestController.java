package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.service.RawMaterialService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/materiaprima")
public class RawMaterialRestController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @GetMapping
    @RequestMapping("/{searchParam}")
    public ResponseEntity<?> searchRawMaterial(@PathVariable String searchParam) {
        return ResponseEntity.ok(rawMaterialService.search(searchParam));
    }

    @GetMapping
    @RequestMapping("/inventario")
    public ResponseEntity<?> listRawMaterials() {
        return ResponseEntity.ok(rawMaterialService.list());
    }

}
