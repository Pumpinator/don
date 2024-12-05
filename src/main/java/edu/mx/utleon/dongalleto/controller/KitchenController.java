package edu.mx.utleon.dongalleto.controller;


import edu.mx.utleon.dongalleto.service.KitchenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/cocina")
public class KitchenController {

    @Autowired
    private KitchenService kitchenService;

    @GetMapping
    public String kitchen(Model model) {
        model.addAttribute("recipes", kitchenService.getRecipes());
        model.addAttribute("rawMaterials", kitchenService.getRawMaterial());
        model.addAttribute("ingredients", kitchenService.getIngredients());
        model.addAttribute("measures", kitchenService.getMeasures());
        return "kitchen/index";
    }

    @GetMapping
    @RequestMapping("/produccion")
    public String ejemplo(Model model) {
        model.addAttribute("variable", "Soy Brandon y soy gay!!!!!");
        return "kitchen/production";
    }

}
