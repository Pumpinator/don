package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.repository.SaleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SaleService {

    @Autowired
    private SaleRepository saleRepository;

}