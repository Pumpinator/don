package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Cookie;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface CookieRepository extends CrudRepository<Cookie, Integer> {
    Iterable<Cookie> findAllByNameContaining(String searchParam);

    Optional<Cookie> findByName(String name);
}
