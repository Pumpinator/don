package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.dto.PurchaseItemDto;
import edu.mx.utleon.dongalleto.service.PurchaseService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Collection;

@RestController
@RequestMapping("/purchase")
@RequiredArgsConstructor
public class PurchaseRestController {

    private final PurchaseService purchaseService;

    @PostMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> add(@RequestBody Collection<PurchaseItemDto> purchaseItems) {
        return ResponseEntity.ok(purchaseService.add(purchaseItems));
    }

}
