package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.dto.CookieDto;
import edu.mx.utleon.dongalleto.model.Cookie;
import edu.mx.utleon.dongalleto.model.Measure;
import edu.mx.utleon.dongalleto.repository.CookieRepository;
import edu.mx.utleon.dongalleto.repository.MeasureRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CookieService {

    @Autowired
    private CookieRepository cookieRepository;

    @Autowired
    private MeasureRepository measureRepository;

    public Iterable<CookieDto> search(String searchParam) {
        return ((List<Cookie>) cookieRepository.findAllByNameContaining(searchParam)).stream().map(this::toDto).toList();
    }

    private CookieDto toDto(Cookie cookie) {
        return CookieDto.builder()
                .id(cookie.getId())
                .name(cookie.getName())
                .price(cookie.getPrice())
                .build();
    }

    public Iterable<Measure> getMeasures() {
        return measureRepository.findAll();
    }

}
