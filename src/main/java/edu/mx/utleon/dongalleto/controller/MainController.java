package edu.mx.utleon.dongalleto.controller;

import edu.mx.utleon.dongalleto.model.Product;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class MainController {

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("key", "value"); // Enviar un atributo a la vista
        model.addAttribute("array", new String[] { "a", "b", "c" }); // Enviar un arreglo a la vista
        model.addAttribute("list", List.of("a", "b", "c")); // Enviar una lista a la vista
        model.addAttribute("number", 123); // Enviar un número a la vista
        model.addAttribute("boolean", true); // Enviar un booleano a la vista
        model.addAttribute("product", Product.builder().id(22L).name("Galleta de Nuez").description("Los ingredientes son nuez, harina, huevo y azúcar").build()); // Enviar un objeto a la vista
        return "index";
    }

}

