package edu.mx.utleon.dongalleto.component;

import edu.mx.utleon.dongalleto.model.RawMaterial;
import edu.mx.utleon.dongalleto.repository.MeasureRepository;
import edu.mx.utleon.dongalleto.repository.RawMaterialRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class DataComponent {

    private final MeasureRepository measureRepository;
    private final RawMaterialRepository rawMaterialRepository;


    @EventListener
    public void createData(ApplicationReadyEvent event) {

    }

}
