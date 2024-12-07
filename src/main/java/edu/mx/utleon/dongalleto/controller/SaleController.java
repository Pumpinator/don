package edu.mx.utleon.dongalleto.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/ventas")
public class SaleController {

    @GetMapping
    public String viewSale() {

        return "sales/index";
    }

}
