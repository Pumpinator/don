package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.model.Supplier;
import edu.mx.utleon.dongalleto.repository.SupplierRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SupplierService {

    @Autowired
    private SupplierRepository supplierRepository;

    public Iterable<Supplier> list() {
        return supplierRepository.findAll();
    }

    public Supplier get(String name) {
        return supplierRepository.findByName(name).orElseThrow(() -> new RuntimeException(String.format("Supplier %s not found", name)));
    }

}
