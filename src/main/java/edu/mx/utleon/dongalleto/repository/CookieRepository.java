package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.Cookie;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CookieRepository extends CrudRepository<Cookie, Integer> {
}
