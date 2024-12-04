package edu.mx.utleon.dongalleto.service;

import edu.mx.utleon.dongalleto.model.Measure;
import edu.mx.utleon.dongalleto.repository.MeasureRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MeasureService {

    @Autowired
    private MeasureRepository measureRepository;

    public Iterable<Measure> list() {
        return measureRepository.findAll();
    }

}
