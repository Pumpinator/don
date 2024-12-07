package edu.mx.utleon.dongalleto.service;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class CookieTests {

    @Autowired
    CookieService cookieService;

    @Test
    void testCookie() {
        //int cookieId = 3;
        //double price = cookieService.getPrice(cookieId);
       // System.out.println("Price of cookie " + cookieId + " is " + price);
    }

    @Test
    void testMeasures() {
        System.out.println(cookieService.getRecipe(1));
    }

}
