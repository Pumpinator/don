package edu.mx.utleon.dongalleto.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class MainController {

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("clave", "valor");
        model.addAttribute("arreglo", new String[] { "a", "b", "c" });
        model.addAttribute("lista", List.of("a", "b", "c"));
        return "index";
    }

}
