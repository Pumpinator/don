package edu.mx.utleon.dongalleto.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/ventas")
public class SaleController {

public String sale() {

    return "sales/index";
}



}
