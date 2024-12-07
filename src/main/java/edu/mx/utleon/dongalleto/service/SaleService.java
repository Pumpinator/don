package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.SaleDetailItemDto;
import edu.mx.utleon.dongalleto.dto.SaleDto;
import edu.mx.utleon.dongalleto.model.Cookie;
import edu.mx.utleon.dongalleto.model.CookieInventory;
import edu.mx.utleon.dongalleto.model.Sale;
import edu.mx.utleon.dongalleto.model.SaleDetail;
import edu.mx.utleon.dongalleto.repository.CookieInventoryRepository;
import edu.mx.utleon.dongalleto.repository.CookieRepository;
import edu.mx.utleon.dongalleto.repository.SaleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class SaleService {

    @Autowired
    private SaleRepository saleRepository;
    @Autowired
    private CookieRepository cookieRepository;
    @Autowired
    private CookieInventoryRepository cookieInventoryRepository;

    public SaleDto addSale(SaleDto s) {
        Sale sale = Sale.builder().date(Instant.now()).build();
        sale = saleRepository.save(sale);
        for (SaleDetailItemDto saleDetailItemDto : s.getItems()) {
            Cookie cookie = cookieRepository.findById(saleDetailItemDto.getCookieId()).orElseThrow();
            CookieInventory cookieInventory = cookieInventoryRepository.findByCookieId(cookie.getId()).orElseThrow();
            if (cookieInventory.getQuantity() < saleDetailItemDto.getQuantity()) {
                throw new RuntimeException("Not enough inventory for cookie " + cookie.getName());
            }
            cookieInventory.setQuantity(cookieInventory.getQuantity() - saleDetailItemDto.getQuantity());
            cookieInventoryRepository.save(cookieInventory);
            SaleDetail saleDetailEntity = SaleDetail.builder()
                    .cookie(cookie)
                    .sale(sale)
                    .id(SaleDetail.SaleDetailId.builder()
                            .cookie(cookie.getId())
                            .sale(sale.getId())
                            .build())
                    .build();
            sale.addSaleDetail(saleDetailEntity);
        }
        sale = saleRepository.save(sale);
        return SaleDto.builder()
                .id(sale.getId())
                .date(sale.getDate())
                .total(sale.getTotal())
                .items(sale.getSaleDetails().stream()
                        .map(saleDetail -> SaleDetailItemDto.builder()
                                .cookieId(saleDetail.getCookie().getId())
                                .saleId(saleDetail.getSale().getId())
                                .quantity(saleDetail.getQuantity())
                                .build())
                        .collect(Collectors.toList()))
                .build();
    }
}