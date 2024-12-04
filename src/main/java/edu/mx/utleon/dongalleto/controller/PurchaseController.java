package edu.mx.utleon.dongalleto.controller;

import edu.mx.utleon.dongalleto.service.MeasureService;
import edu.mx.utleon.dongalleto.service.PurchaseService;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import edu.mx.utleon.dongalleto.service.SupplierService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/compras")
public class PurchaseController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @Autowired
    private MeasureService measureService;

    @Autowired
    private SupplierService supplierService;
    @Autowired
    private PurchaseService purchaseService;

    @GetMapping
    public String viewPurchases(Model model) {
        model.addAttribute("purchases", purchaseService.list());
        return "purchase/buy";
    }

    @GetMapping("/comprar")
    public String viewBuyA(Model model,
                          @RequestParam(value = "supplier", required = false) String supplier
                          ) {
        if(supplier != null) {
            model.addAttribute("supplier", supplierService.get(supplier));
        }
        model.addAttribute("rawMaterial", rawMaterialService.list());
        model.addAttribute("measures", measureService.list());
        model.addAttribute("suppliers", supplierService.list());
        return "purchase/buya";
    }

    @GetMapping("/comprar/b")
    public String viewBuyB(Model model) {
        model.addAttribute("rawMaterial", rawMaterialService.list());
        model.addAttribute("measures", measureService.list());
        return "purchase/buyb";
    }

}
