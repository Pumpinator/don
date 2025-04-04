USE dongalleto;

SET @margen_ganancia = 1.5;

SET @precio_harina = 10;
SET @precio_huevo = 5;
SET @precio_leche = 15;
SET @precio_azucar = 15;
SET @precio_mantequilla = 80;
SET @precio_chispas_chocolate = 100;
SET @precio_avena = 20;
SET @precio_nuez = 200;
SET @precio_pasas = 50;
SET @precio_fresa = 60;
SET @precio_chocolate_avellana = 150;
SET @precio_almendra = 250;
SET @precio_cacahuate = 70;
SET @precio_coco = 80;

SET @inventario_harina = 100;
SET @inventario_huevo = 50;
SET @inventario_leche = 200;
SET @inventario_azucar = 50;
SET @inventario_mantequilla = 20;
SET @inventario_chispas_chocolate = 10;
SET @inventario_avena = 30;
SET @inventario_nuez = 5;
SET @inventario_pasas = 15;
SET @inventario_fresa = 12;
SET @inventario_chocolate_avellana = 8;
SET @inventario_almendra = 4;
SET @inventario_cacahuate = 25;
SET @inventario_coco = 10;

SET @costo_harina = @precio_harina * @inventario_harina;
SET @costo_huevo = @precio_huevo * @inventario_huevo;
SET @costo_leche = @precio_leche * @inventario_leche;
SET @costo_azucar = @precio_azucar * @inventario_azucar;
SET @costo_mantequilla = @precio_mantequilla * @inventario_mantequilla;
SET @costo_chispas_chocolate = @precio_chispas_chocolate * @inventario_chispas_chocolate;
SET @costo_avena = @precio_avena * @inventario_avena;
SET @costo_nuez = @precio_nuez * @inventario_nuez;
SET @costo_pasas = @precio_pasas * @inventario_pasas;
SET @costo_fresa = @precio_fresa * @inventario_fresa;
SET @costo_chocolate_avellana = @precio_chocolate_avellana * @inventario_chocolate_avellana;
SET @costo_almendra = @precio_almendra * @inventario_almendra;
SET @costo_cacahuate = @precio_cacahuate * @inventario_cacahuate;
SET @costo_coco = @precio_coco * @inventario_coco;

SET @peso_galleta = 0.05;

INSERT INTO roles (nombre)
VALUES ('ADMIN'),
       ('TRABAJADOR'),
       ('COMPRADOR');

INSERT INTO medidas (nombre, abreviatura)
VALUES ('Kilogramo', 'kg'),
       ('Litro', 'lt'),
       ('Pieza', 'pz');

INSERT INTO insumos (nombre)
VALUES ('Harina'),
       ('Huevo'),
       ('Leche'),
       ('Azúcar'),
       ('Mantequilla'),
       ('Chispas de Chocolate'),
       ('Avena'),
       ('Nuez'),
       ('Pasas'),
       ('Fresa'),
       ('Chocolate con Avellana'),
       ('Almendra'),
       ('Cacahuate'),
       ('Coco');

SET @receta_chispas_chocolate = @precio_harina +
                                @precio_huevo +
                                @precio_leche +
                                @precio_azucar +
                                @precio_mantequilla +
                                @precio_chispas_chocolate;

SET @receta_avena = @precio_harina +
                    @precio_huevo +
                    @precio_leche +
                    @precio_azucar +
                    @precio_mantequilla +
                    @precio_avena;

SET @receta_nuez = @precio_harina +
                   @precio_huevo +
                   @precio_leche +
                   @precio_azucar +
                   @precio_mantequilla +
                   @precio_nuez;

SET @receta_pasas = @precio_harina +
                    @precio_huevo +
                    @precio_leche +
                    @precio_azucar +
                    @precio_mantequilla +
                    @precio_pasas;
SET @receta_fresa = @precio_harina +
                    @precio_huevo +
                    @precio_leche +
                    @precio_azucar +
                    @precio_mantequilla +
                    @precio_fresa;

SET @receta_chocolate_avellana = @precio_harina +
                                 @precio_huevo +
                                 @precio_leche +
                                 @precio_azucar +
                                 @precio_mantequilla +
                                 @precio_chocolate_avellana;

SET @receta_almendra = @precio_harina +
                       @precio_huevo +
                       @precio_leche +
                       @precio_azucar +
                       @precio_mantequilla +
                       @precio_almendra;

SET @receta_cacahuate = @precio_harina +
                        @precio_huevo +
                        @precio_leche +
                        @precio_azucar +
                        @precio_mantequilla +
                        @precio_cacahuate;

SET @receta_coco = @precio_harina +
                   @precio_huevo +
                   @precio_leche +
                   @precio_azucar +
                   @precio_mantequilla +
                   @precio_coco;

SET @receta_mantequilla = @precio_harina +
                          @precio_huevo +
                          @precio_leche +
                          @precio_azucar +
                          @precio_mantequilla;

SET @fecha_actual = CURDATE();
SET @fecha_expiracion = DATE_ADD(@fecha_actual, INTERVAL 30 DAY);

INSERT INTO galletas (nombre, precio, imagen)
VALUES ('Chispas de Chocolate', FLOOR(@peso_galleta * @receta_chispas_chocolate * @margen_ganancia), 'chispas.png'),
       ('Avena', FLOOR(@peso_galleta * @receta_avena * @margen_ganancia), 'avena.png'),
       ('Nuez', FLOOR(@peso_galleta * @receta_nuez * @margen_ganancia), 'nuez.png'),
       ('Pasas', FLOOR(@peso_galleta * @receta_pasas * @margen_ganancia), 'pasas.png'),
       ('Fresa', FLOOR(@peso_galleta * @receta_fresa * @margen_ganancia), 'fresa.png'),
       ('Mantequilla', FLOOR(@peso_galleta * @receta_mantequilla * @margen_ganancia), 'mantequilla.png'),
       ('Chocolate con Avellana', FLOOR(@peso_galleta * @receta_chocolate_avellana * @margen_ganancia), 'avellana.png'),
       ('Almendra', FLOOR(@peso_galleta * @receta_almendra * @margen_ganancia), 'almendra.png'),
       ('Cacahuate', FLOOR(@peso_galleta * @receta_cacahuate * @margen_ganancia), 'cacahuate.png'),
       ('Coco', FLOOR(@peso_galleta * @receta_coco * @margen_ganancia), 'coco.png');


INSERT INTO proveedores (nombre, contacto)
VALUES ('Harinera Beleño', '477 391 0598'),
       ('Huevo San Juan', '477 707 0099'),
       ('Leche León', '477 152 2100'),
       ('Costco Wholesale', '477 788 1300');


INSERT INTO compras (proveedor_id, fecha, total)
VALUES (1, @fecha_expiracion, @costo_harina),
       (2, @fecha_expiracion, @costo_huevo),
       (3, @fecha_expiracion, @costo_leche),
       (4, @fecha_expiracion, @costo_azucar +
                              @costo_mantequilla +
                              @costo_chispas_chocolate +
                              @costo_avena +
                              @costo_nuez +
                              @costo_pasas +
                              @costo_fresa +
                              @costo_chocolate_avellana +
                              @costo_almendra +
                              @costo_cacahuate +
                              @costo_coco);


INSERT INTO compras_detalles (compra_id, insumo_id, precio_unitario, precio_total, cantidad, medida_id)
VALUES (1, 1, @precio_harina, @costo_harina, @inventario_harina, 1),
       (2, 2, @precio_huevo, @costo_huevo, @inventario_huevo, 1),
       (3, 3, @precio_leche, @costo_leche, @inventario_leche, 2),
       (4, 4, @precio_azucar, @costo_azucar, @inventario_azucar, 1),
       (4, 5, @precio_mantequilla, @costo_mantequilla, @inventario_mantequilla, 1),
       (4, 6, @precio_chispas_chocolate, @costo_chispas_chocolate, @inventario_chispas_chocolate, 1),
       (4, 7, @precio_avena, @costo_avena, @inventario_avena, 1),
       (4, 8, @precio_nuez, @costo_nuez, @inventario_nuez, 1),
       (4, 9, @precio_pasas, @costo_pasas, @inventario_pasas, 1),
       (4, 10, @precio_fresa, @costo_fresa, @inventario_fresa, 1),
       (4, 11, @precio_chocolate_avellana, @costo_chocolate_avellana, @inventario_chocolate_avellana, 1),
       (4, 12, @precio_almendra, @costo_almendra, @inventario_almendra, 1),
       (4, 13, @precio_cacahuate, @costo_cacahuate, @inventario_cacahuate, 1),
       (4, 14, @precio_coco, @costo_coco, @inventario_coco, 1);


INSERT INTO insumos_inventarios (compra_id, insumo_id, fecha_expiracion, costo, cantidad, medida_id)
VALUES (1, 1, @fecha_expiracion, @precio_harina, @inventario_harina, 1),
       (2, 2, @fecha_expiracion, @precio_huevo, @inventario_huevo, 1),
       (3, 3, @fecha_expiracion, @precio_leche, @inventario_leche, 2),
       (4, 4, @fecha_expiracion, @precio_azucar, @inventario_azucar, 1),
       (4, 5, @fecha_expiracion, @precio_mantequilla, @inventario_mantequilla, 1),
       (4, 6, @fecha_expiracion, @precio_chispas_chocolate, @inventario_chispas_chocolate, 1),
       (4, 7, @fecha_expiracion, @precio_avena, @inventario_avena, 1),
       (4, 8, @fecha_expiracion, @precio_nuez, @inventario_nuez, 1),
       (4, 9, @fecha_expiracion, @precio_pasas, @inventario_pasas, 1),
       (4, 10, @fecha_expiracion, @precio_fresa, @inventario_fresa, 1),
       (4, 11, @fecha_expiracion, @precio_chocolate_avellana, @inventario_chocolate_avellana, 1),
       (4, 12, @fecha_expiracion, @precio_almendra, @inventario_almendra, 1),
       (4, 13, @fecha_expiracion, @precio_cacahuate, @inventario_cacahuate, 1),
       (4, 14, @fecha_expiracion, @precio_coco, @inventario_coco, 1);

DELIMITER $$

CREATE PROCEDURE SP_InsertarReceta(
    IN p_nombre VARCHAR(255),
    IN p_galleta_id INT,
    IN p_procedimiento TEXT,
    IN p_insumos TEXT, -- IDs de insumos separados por comas ('1,2,3')
    IN p_cantidades TEXT, -- Cantidades separadas por comas ('200,100,3')
    IN p_medidas TEXT -- IDs de medidas separadas por comas ('1,2,3')
)
BEGIN
    DECLARE v_receta_id INT;
    DECLARE v_insumo_id INT;
    DECLARE v_cantidad FLOAT;
    DECLARE v_medida_id INT;
    DECLARE v_pos_insumo INT;
    DECLARE v_pos_cantidad INT;
    DECLARE v_pos_medida INT;
    
    -- Insertar la receta en la tabla recetas
    INSERT INTO recetas (nombre, galleta_id, procedimiento)
    VALUES (p_nombre, p_galleta_id, p_procedimiento);
    
    -- Obtener el ID de la receta recién insertada
    SET v_receta_id = LAST_INSERT_ID();
    
    -- Bucle para recorrer los insumos, cantidades y medidas
    WHILE LENGTH(p_insumos) > 0 DO
        -- Extraer el primer insumo, cantidad y medida
        SET v_pos_insumo = IF(LOCATE(',', p_insumos) > 0, LOCATE(',', p_insumos), LENGTH(p_insumos) + 1);
        SET v_pos_cantidad = IF(LOCATE(',', p_cantidades) > 0, LOCATE(',', p_cantidades), LENGTH(p_cantidades) + 1);
        SET v_pos_medida = IF(LOCATE(',', p_medidas) > 0, LOCATE(',', p_medidas), LENGTH(p_medidas) + 1);
        
        SET v_insumo_id = CAST(SUBSTRING(p_insumos, 1, v_pos_insumo - 1) AS UNSIGNED);
        SET v_cantidad = CAST(SUBSTRING(p_cantidades, 1, v_pos_cantidad - 1) AS FLOAT);
        SET v_medida_id = CAST(SUBSTRING(p_medidas, 1, v_pos_medida - 1) AS UNSIGNED);
        
        -- Insertar en la tabla ingrediente (singular)
        INSERT INTO ingrediente (cantidad, medida_id, receta_id, insumo_id)
        VALUES (v_cantidad, v_medida_id, v_receta_id, v_insumo_id);
        
        -- Remover el primer insumo, cantidad y medida procesados
        SET p_insumos = IF(v_pos_insumo < LENGTH(p_insumos), SUBSTRING(p_insumos, v_pos_insumo + 1), '');
        SET p_cantidades = IF(v_pos_cantidad < LENGTH(p_cantidades), SUBSTRING(p_cantidades, v_pos_cantidad + 1), '');
        SET p_medidas = IF(v_pos_medida < LENGTH(p_medidas), SUBSTRING(p_medidas, v_pos_medida + 1), '');
    END WHILE;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SP_CrearCompra(
    IN p_proveedor_id INT,
    IN p_fecha DATE,
    IN p_total DECIMAL(10,2),
    IN p_insumos TEXT,  -- Lista de insumos separados por comas ('1,2,3')
    IN p_cantidades TEXT,  -- Cantidades separadas por comas ('10,5,20')
    IN p_precios_unitarios TEXT,  -- Precios unitarios ('50.00,30.00,20.00')
    IN p_medidas TEXT, -- IDs de medidas ('1,2,3')
    IN p_fechas_expiracion TEXT -- Fechas de expiración ('2025-12-01,2026-01-15,2024-10-10')
)
BEGIN
    DECLARE v_compra_id INT;
    DECLARE v_index INT DEFAULT 1;
    DECLARE v_insumo_id INT;
    DECLARE v_cantidad DECIMAL(10,2);
    DECLARE v_precio_unitario DECIMAL(10,2);
    DECLARE v_precio_total DECIMAL(10,2);
    DECLARE v_medida_id INT;
    DECLARE v_fecha_expiracion DATE;
    
    -- Insertar la compra en la tabla principal
    INSERT INTO compras (proveedor_id, fecha, total) 
    VALUES (p_proveedor_id, p_fecha, p_total);
    
    -- Obtener el ID de la compra recién insertada
    SET v_compra_id = LAST_INSERT_ID();

    -- Bucle para insertar cada detalle de compra
    WHILE LOCATE(',', p_insumos) > 0 DO
        -- Extraer el primer insumo y sus datos correspondientes
        SET v_insumo_id = CAST(SUBSTRING_INDEX(p_insumos, ',', 1) AS UNSIGNED);
        SET v_cantidad = CAST(SUBSTRING_INDEX(p_cantidades, ',', 1) AS DECIMAL(10,2));
        SET v_precio_unitario = CAST(SUBSTRING_INDEX(p_precios_unitarios, ',', 1) AS DECIMAL(10,2));
        SET v_medida_id = CAST(SUBSTRING_INDEX(p_medidas, ',', 1) AS UNSIGNED);
        SET v_fecha_expiracion = STR_TO_DATE(SUBSTRING_INDEX(p_fechas_expiracion, ',', 1), '%Y-%m-%d');

        -- Calcular el precio total
        SET v_precio_total = v_precio_unitario * v_cantidad;

        -- Insertar en compras_detalles
        INSERT INTO compras_detalles (compra_id, insumo_id, cantidad, precio_unitario, precio_total, medida_id) 
        VALUES (v_compra_id, v_insumo_id, v_cantidad, v_precio_unitario, v_precio_total, v_medida_id);

        -- Actualizar el inventario de insumos
        INSERT INTO insumos_inventarios (insumo_id, compra_id, cantidad, costo, medida_id, fecha_expiracion)
        VALUES (v_insumo_id, v_compra_id, v_cantidad, v_precio_unitario, v_medida_id, v_fecha_expiracion)
        ON DUPLICATE KEY UPDATE cantidad = cantidad + v_cantidad;

        -- Eliminar el primer valor de las listas
        SET p_insumos = SUBSTRING(p_insumos, LOCATE(',', p_insumos) + 1);
        SET p_cantidades = SUBSTRING(p_cantidades, LOCATE(',', p_cantidades) + 1);
        SET p_precios_unitarios = SUBSTRING(p_precios_unitarios, LOCATE(',', p_precios_unitarios) + 1);
        SET p_medidas = SUBSTRING(p_medidas, LOCATE(',', p_medidas) + 1);
        SET p_fechas_expiracion = SUBSTRING(p_fechas_expiracion, LOCATE(',', p_fechas_expiracion) + 1);
    END WHILE;

    -- Insertar el último insumo (ya que no tiene coma al final)
    INSERT INTO compras_detalles (compra_id, insumo_id, cantidad, precio_unitario, precio_total, medida_id) 
    VALUES (v_compra_id, CAST(p_insumos AS UNSIGNED), CAST(p_cantidades AS DECIMAL(10,2)), 
            CAST(p_precios_unitarios AS DECIMAL(10,2)), 
            CAST(p_precios_unitarios AS DECIMAL(10,2)) * CAST(p_cantidades AS DECIMAL(10,2)), 
            CAST(p_medidas AS UNSIGNED));

    -- Insertar en insumos_inventarios
    INSERT INTO insumos_inventarios (insumo_id, compra_id, cantidad, costo, medida_id, fecha_expiracion)
    VALUES (CAST(p_insumos AS UNSIGNED), v_compra_id, CAST(p_cantidades AS DECIMAL(10,2)), 
            CAST(p_precios_unitarios AS DECIMAL(10,2)), 
            CAST(p_medidas AS UNSIGNED), STR_TO_DATE(p_fechas_expiracion, '%Y-%m-%d'))
    ON DUPLICATE KEY UPDATE cantidad = cantidad + CAST(p_cantidades AS DECIMAL(10,2));

END$$

DELIMITER ;

*/




/*
INSERT INTO presentaciones (cantidad, peso, precio, medida_id, galleta_id)
VALUES (1, @peso_galleta, FLOOR(@peso_galleta * @receta_chispas_chocolate * @margen_ganancia), 3, 1),
        (2, @peso_galleta * 2, FLOOR(@peso_galleta * 2 * @receta_chispas_chocolate * @margen_ganancia), 3, 1),
        (5, @peso_galleta * 5, FLOOR(@peso_galleta * 5 * @receta_chispas_chocolate * @margen_ganancia), 3, 1).
        (0.5, @peso_galleta * 0.5, FLOOR(@peso_galleta * 0.5 * @receta_chispas_chocolate * @margen_ganancia), 3, 1),
        (0.5, @peso_galleta * 0.5, FLOOR(@peso_galleta * 0.5 * @receta_chispas_chocolate * @margen_ganancia), 3, 1),
        (1, 0.001, FLOOR((@peso_galleta * @receta_chispas_chocolate * @margen_ganancia) / (@peso_galleta * 1000)), 1, 1);

¿Deberíamos generar una tabla de presentaciones para cada galleta?

from bd import bd
from modelo.medida import Medida
from modelo.galleta import Galleta

class Presentacion(bd.Model):
    __tablename__ = 'presentaciones'
    
    id = bd.Column(bd.Integer, primary_key=True)
    cantidad = bd.Column(bd.Integer, nullable=False)
    peso = bd.Column(bd.Float, nullable=False)
    precio = bd.Column(bd.Float, nullable=False)
    
    medida_id = bd.Column(bd.Integer, bd.ForeignKey('medidas.id'), nullable=False)
    medida = bd.relationship(Medida, backref='presentaciones')
    
    galleta_id = bd.Column(bd.Integer, bd.ForeignKey('galletas.id'), nullable=False)
    galleta = bd.relationship(Galleta, backref='presentaciones')
*/


DELIMITER $$

CREATE TRIGGER TR_CalcularPrecioGalleta
AFTER INSERT ON recetas
FOR EACH ROW
BEGIN
    DECLARE v_precio_total FLOAT DEFAULT 0;
    DECLARE v_costo_insumo FLOAT;
    DECLARE v_cantidad FLOAT;
    DECLARE v_margen_ganancia FLOAT DEFAULT 1.5;

    -- Cursor para recorrer los ingredientes de la receta recién insertada
    DECLARE cur_ingredientes CURSOR FOR
        SELECT i.cantidad, ins.costo
        FROM ingrediente i
        JOIN insumos_inventarios ins ON i.insumo_id = ins.insumo_id
        WHERE i.receta_id = NEW.id;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_costo_insumo = NULL;

    -- Abrir el cursor
    OPEN cur_ingredientes;

    -- Recorrer los ingredientes y calcular el costo total
    FETCH cur_ingredientes INTO v_cantidad, v_costo_insumo;
    WHILE v_costo_insumo IS NOT NULL DO
        SET v_precio_total = v_precio_total + (v_cantidad * v_costo_insumo);
        FETCH cur_ingredientes INTO v_cantidad, v_costo_insumo;
    END WHILE;

    -- Cerrar el cursor
    CLOSE cur_ingredientes;

    -- Calcular el precio final de la galleta con el margen de ganancia
    SET v_precio_total = FLOOR(v_precio_total * v_margen_ganancia);

    -- Actualizar el precio de la galleta asociada
    UPDATE galletas
    SET precio = v_precio_total
    WHERE id = NEW.galleta_id;
END$$

DELIMITER ;
-- ↑ Trigger pa calcular el precio de la galleta
-- Va a haber una galleta creada, pero sin precio porque se va a esperar a
-- que se inserte la receta para calcular el precio de la galleta en base a sus insumos