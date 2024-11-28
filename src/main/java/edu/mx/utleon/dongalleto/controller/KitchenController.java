package edu.mx.utleon.dongalleto.controller;


import edu.mx.utleon.dongalleto.service.KitchenService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/cocina")
@RequiredArgsConstructor
public class KitchenController {

    private final KitchenService kitchenService;

    @GetMapping
    public String kitchen(Model model) {
        model.addAttribute("recipes", kitchenService.getRecipes());
        model.addAttribute("rawMaterials", kitchenService.getRawMaterial());
        model.addAttribute("ingredients", kitchenService.getIngredients());
        model.addAttribute("measures", kitchenService.getMeasures());
        return "kitchen/index";
    }

}
