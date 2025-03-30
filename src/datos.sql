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

SET @peso_galleta = 0.045;

INSERT INTO roles (nombre)
VALUES ('ADMIN'),
       ('TRABAJADOR'),
       ('COMPRADOR');

INSERT INTO medidas (nombre)
VALUES ('Kilogramo'),
       ('Litro'),
       ('Pieza');

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

INSERT INTO galletas (nombre, precio, imagen, medida_id)
VALUES ('Chispas de Chocolate', FLOOR(@peso_galleta * @receta_chispas_chocolate * @margen_ganancia), 'chispas.png', 3),
       ('Avena', FLOOR(@peso_galleta * @receta_avena * @margen_ganancia), 'avena.png', 3),
       ('Nuez', FLOOR(@peso_galleta * @receta_nuez * @margen_ganancia), 'nuez.png', 3),
       ('Pasas', FLOOR(@peso_galleta * @receta_pasas * @margen_ganancia), 'pasas.png', 3),
       ('Fresa', FLOOR(@peso_galleta * @receta_fresa * @margen_ganancia), 'fresa.png', 3),
       ('Mantequilla', FLOOR(@peso_galleta * @receta_mantequilla * @margen_ganancia), 'mantequilla.png', 3),
       ('Chocolate con Avellana', FLOOR(@peso_galleta * @receta_chocolate_avellana * @margen_ganancia), 'avellana.png', 3),
       ('Almendra', FLOOR(@peso_galleta * @receta_almendra * @margen_ganancia), 'almendra.png', 3),
       ('Cacahuate', FLOOR(@peso_galleta * @receta_cacahuate * @margen_ganancia), 'cacahuate.png', 3),
       ('Coco', FLOOR(@peso_galleta * @receta_coco * @margen_ganancia), 'coco.png', 3);

INSERT INTO proveedores (nombre, contacto)
VALUES ('Harinera Beleño', '477 391 0598'),
       ('Huevo San Juan', '477 707 0099'),
       ('Leche León', '477 152 2100'),
       ('Costco Wholesale', '477 788 1300');

INSERT INTO compras (proveedor_id, fecha)
VALUES (1, '2021-01-01'),
       (2, '2021-01-01'),
       (3, '2021-01-01'),
       (4, '2021-01-01');

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
VALUES (1, 1, '2022-01-01', @precio_harina, @inventario_harina, 1),
       (2, 2, '2022-01-01', @precio_huevo, @inventario_huevo, 1),
       (3, 3, '2022-01-01', @precio_leche, @inventario_leche, 2),
       (4, 4, '2022-01-01', @precio_azucar, @inventario_azucar, 1),
       (4, 5, '2022-01-01', @precio_mantequilla, @inventario_mantequilla, 1),
       (4, 6, '2022-01-01', @precio_chispas_chocolate, @inventario_chispas_chocolate, 1),
       (4, 7, '2022-01-01', @precio_avena, @inventario_avena, 1),
       (4, 8, '2022-01-01', @precio_nuez, @inventario_nuez, 1),
       (4, 9, '2022-01-01', @precio_pasas, @inventario_pasas, 1),
       (4, 10, '2022-01-01', @precio_fresa, @inventario_fresa, 1),
       (4, 11, '2022-01-01', @precio_chocolate_avellana, @inventario_chocolate_avellana, 1),
       (4, 12, '2022-01-01', @precio_almendra, @inventario_almendra, 1),
       (4, 13, '2022-01-01', @precio_cacahuate, @inventario_cacahuate, 1),
       (4, 14, '2022-01-01', @precio_coco, @inventario_coco, 1);

INSERT INTO recetas (nombre, galleta_id)
VALUES ('Chispas de Chocolate', 1),
       ('Avena', 2),
       ('Nuez', 3),
       ('Pasas', 4),
       ('Fresa', 5),
       ('Mantequilla', 6),
       ('Chocolate con Avellana', 7),
       ('Almendra', 8),
       ('Cacahuate', 9),
       ('Coco', 10);

INSERT INTO producciones (fecha, costo, receta_id)
VALUES ('2021-01-01', @receta_chispas_chocolate, 1),
       ('2021-01-01', @receta_avena, 2),
       ('2021-01-01', @receta_nuez, 3),
       ('2021-01-01', @receta_pasas, 4),
       ('2021-01-01', @receta_fresa, 5),
       ('2021-01-01', @receta_mantequilla, 6),
       ('2021-01-01', @receta_chocolate_avellana, 7),
       ('2021-01-01', @receta_almendra, 8),
       ('2021-01-01', @receta_cacahuate, 9),
       ('2021-01-01', @receta_coco, 10);

INSERT INTO galletas_inventarios (produccion_id, galleta_id, fecha_expiracion, costo, cantidad, medida_id)
VALUES (1, 1, '2022-01-01', FLOOR(@receta_chispas_chocolate * 100), 100, 3),
       (2, 2, '2022-01-01', FLOOR(@receta_avena * 100), 100, 3),
       (3, 3, '2022-01-01', FLOOR(@receta_nuez * 100), 100, 3),
       (4, 4, '2022-01-01', FLOOR(@receta_pasas * 100), 100, 3),
       (5, 5, '2022-01-01', FLOOR(@receta_fresa * 100), 100, 3),
       (6, 6, '2022-01-01', FLOOR(@receta_mantequilla * 100), 100, 3),
       (7, 7, '2022-01-01', FLOOR(@receta_chocolate_avellana * 100), 100, 3),
       (8, 8, '2022-01-01', FLOOR(@receta_almendra * 100), 100, 3),
       (9, 9, '2022-01-01', FLOOR(@receta_cacahuate * 100), 100, 3),
       (10, 10, '2022-01-01', FLOOR(@receta_coco * 100), 100, 3);

INSERT INTO ingrediente(receta_id, insumo_id, medida_id, cantidad) VALUES 
(1, 3, 1, 20)
, (1, 5, 2, 50)
, (2, 7, 3, 10)
, (2, 2, 1, 30)
, (3, 9, 2, 15)
, (3, 1, 3, 40)
, (4, 4, 1, 25)
, (4, 6, 2, 35)
, (5, 8, 3, 12)
, (5, 10, 1, 22)
, (6, 11, 2, 18)
, (6, 12, 3, 28)
, (7, 13, 1, 32)
, (8, 14, 2, 45)
, (9, 5, 3, 27);



