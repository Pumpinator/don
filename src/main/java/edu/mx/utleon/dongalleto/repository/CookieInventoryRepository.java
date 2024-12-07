package edu.mx.utleon.dongalleto.repository;

import edu.mx.utleon.dongalleto.model.CookieInventory;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface CookieInventoryRepository extends CrudRepository<CookieInventory, Long> {
    Optional<CookieInventory> findByCookieId(Integer cookieId);
}
