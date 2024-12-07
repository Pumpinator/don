package edu.mx.utleon.dongalleto.controller;


import edu.mx.utleon.dongalleto.dto.SaleDto;
import edu.mx.utleon.dongalleto.model.Measurable;
import edu.mx.utleon.dongalleto.service.SaleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/ventas")
public class SaleController {

    @Autowired
    private SaleService saleService;

    @GetMapping
    public String viewSale() {
        return "sales/index";
    }

    @PostMapping
    public String addSale(@RequestBody SaleDto sale) {
        saleService.addSale(sale);
        return "redirect:sales/index";
    }

}
