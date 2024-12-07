package edu.mx.utleon.dongalleto.rest;

import edu.mx.utleon.dongalleto.service.CookieService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/galletas")
public class CookieRestController {

    @Autowired
    private CookieService cookieService;

    @GetMapping
    @RequestMapping("/{searchParam}")
    public ResponseEntity<?> searchCookie(@PathVariable String searchParam) {
        return ResponseEntity.ok(cookieService.search(searchParam));
    }

    @GetMapping
    @RequestMapping("/medidas")
    public ResponseEntity<?> getMeasures() {
        return ResponseEntity.ok(cookieService.getMeasures());
    }

}
