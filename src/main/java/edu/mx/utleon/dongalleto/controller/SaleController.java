package edu.mx.utleon.dongalleto.controller;


import edu.mx.utleon.dongalleto.model.Measurable;
import edu.mx.utleon.dongalleto.service.SaleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/ventas")
public class SaleController {

    @Autowired
    private SaleService saleService;


    private Measurable measurable;


    @GetMapping
    public String viewSale() {

        return "sales/index";
    }

    @PostMapping("/venta")
    public String addSale() {

        return "redirect:sales/index";
    }


}
