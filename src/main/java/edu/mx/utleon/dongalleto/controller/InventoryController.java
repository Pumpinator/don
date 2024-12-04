package edu.mx.utleon.dongalleto.controller;

import edu.mx.utleon.dongalleto.service.MeasureService;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import edu.mx.utleon.dongalleto.service.SupplierService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.time.LocalDate;

@Controller
@RequestMapping("/inventario")
public class InventoryController {

    @Autowired
    private RawMaterialService rawMaterialService;

    @Autowired
    private MeasureService measureService;

    @Autowired
    private SupplierService supplierService;

    @GetMapping
    public String viewInventory() {
        return "inventory/index";
    }

    @GetMapping("/materiaprima" )
    public String viewRawMaterialInventory() {
        return "inventory/rawmaterial";
    }

    @GetMapping("/materiaprima/a" )
    public String viewRawMaterialInventoryA(Model model) {
        model.addAttribute("rawMaterial", rawMaterialService.list());
        model.addAttribute("measures", measureService.list());
        model.addAttribute("suppliers", supplierService.list());
        model.addAttribute("rawMaterialInventory", rawMaterialService.listInventory());
        return "inventory/rawmateriala";
    }

    @GetMapping("/materiaprima/b" )
    public String viewRawMaterialInventoryB(Model model) {
        int expiringCount = rawMaterialService.countByDates(LocalDate.now(), LocalDate.now().plusDays(7));
        int expiredCount = rawMaterialService.countByDateBefore(LocalDate.now());
        int lowStockCount = rawMaterialService.countLowStockAndExpiredByName(10);
        model.addAttribute("rawMaterialInventory", rawMaterialService.listInventory());
        model.addAttribute("expiringCount", expiringCount);
        model.addAttribute("expiredCount", expiredCount);
        model.addAttribute("lowStockCount", lowStockCount);
        return "inventory/rawmaterialb";
    }

}
