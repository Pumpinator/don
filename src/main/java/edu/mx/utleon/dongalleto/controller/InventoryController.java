package edu.mx.utleon.dongalleto.controller;

import edu.mx.utleon.dongalleto.dto.RawMaterialInventoryItemDto;
import edu.mx.utleon.dongalleto.service.MeasureService;
import edu.mx.utleon.dongalleto.service.RawMaterialService;
import edu.mx.utleon.dongalleto.service.SupplierService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
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

    @GetMapping("/materiaprima")
    public String viewRawMaterialInventory(Model model) {
        int expiringCount = rawMaterialService.countByDates(LocalDate.now(), LocalDate.now().plusDays(7));
        int expiredCount = rawMaterialService.countByDateBefore(LocalDate.now());
        int lowStockCount = rawMaterialService.countLowStockAndExpiredByName(10);
        model.addAttribute("expiringCount", expiringCount);
        model.addAttribute("expiredCount", expiredCount);
        model.addAttribute("lowStockCount", lowStockCount);
        model.addAttribute("rawMaterialInventory", rawMaterialService.listInventory());
        model.addAttribute("rawMaterial", rawMaterialService.list());
        model.addAttribute("measures", measureService.list());
        model.addAttribute("suppliers", supplierService.list());
        model.addAttribute("rawMaterialInventory", rawMaterialService.listInventory());
        model.addAttribute("inventoryItem", new RawMaterialInventoryItemDto());
        return "inventory/rawmaterial";
    }

    @GetMapping("/materiaprima/{id}")
    public String viewRawMaterialInventory(Model model, @PathVariable Integer id) {
        model.addAttribute("rawMaterialInventory", rawMaterialService.getInventory(id));
        model.addAttribute("rawMaterial", rawMaterialService.list());
        model.addAttribute("measures", measureService.list());
        model.addAttribute("suppliers", supplierService.list());
        model.addAttribute("inventoryItem", new RawMaterialInventoryItemDto());
        return "inventory/rawmaterialdetails";
    }

    @PostMapping("/materiaprima")
    public String addRawMaterialInventory(RawMaterialInventoryItemDto item) {
        rawMaterialService.saveInventory(item);
        return "redirect:/inventario/materiaprima";
    }

}
