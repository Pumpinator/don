USE dongalleto;

SET @margen_ganancia = 1.5;

SET @precio_harina  = 10;
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

SET @peso_galleta = 0.045;

INSERT INTO medidas (nombre) VALUES
                        ('Kilogramo'),
                        ('Litro'),
                        ('Pieza');

INSERT INTO insumos (nombre) VALUES
                        ('Harina'),
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

INSERT INTO galletas (nombre, precio) VALUES
                                          ('Chispas de Chocolate', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_chispas_chocolate)) * @margen_ganancia)),
                                          ('Avena', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_avena)) * @margen_ganancia)),
                                          ('Nuez', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_nuez)) * @margen_ganancia)),
                                          ('Pasas', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_pasas)) * @margen_ganancia)),
                                          ('Fresa', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_fresa)) * @margen_ganancia)),
                                          ('Mantequilla', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla)) * @margen_ganancia)),
                                          ('Chocolate con Avellana', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_chocolate_avellana)) * @margen_ganancia)),
                                          ('Almendra', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_almendra)) * @margen_ganancia)),
                                          ('Cacahuate', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_cacahuate)) * @margen_ganancia)),
                                          ('Coco', FLOOR((@peso_galleta * (@precio_harina + @precio_huevo + @precio_leche + @precio_azucar + @precio_mantequilla + @precio_coco)) * @margen_ganancia));

INSERT INTO proveedores (nombre, contacto) VALUES
                                            ('Harinera Beleño', '477 391 0598'),
                                            ('Huevo San Juan', '477 707 0099'),
                                            ('Leche León', '477 152 2100'),
                                            ('Costco Wholesale', '477 788 1300');

INSERT INTO compras (proveedor_id, fecha) VALUES
                                                (1, '2021-01-01'),
                                                (2, '2021-01-01'),
                                                (3, '2021-01-01'),
                                                (4, '2021-01-01');

INSERT INTO compras_detalles (compra_id, insumo_id, precio_unitario, precio_total, cantidad, medida_id) VALUES
                                                                                                            (1, 1, @precio_harina, @precio_harina * 100, 100, 1),
                                                                                                            (2, 2, @precio_huevo, @precio_huevo * 50, 50, 1),
                                                                                                            (3, 3, @precio_leche, @precio_leche * 200, 200, 2),
                                                                                                            (4, 4, @precio_azucar, @precio_azucar * 50, 50, 1),
                                                                                                            (4, 5, @precio_mantequilla, @precio_mantequilla * 20, 20, 1),
                                                                                                            (4, 6, @precio_chispas_chocolate, @precio_chispas_chocolate * 10, 10, 1),
                                                                                                            (4, 7, @precio_avena, @precio_avena * 30, 30, 1),
                                                                                                            (4, 8, @pÏrecio_nuez, @precio_nuez * 5, 5, 1),
                                                                                                            (4, 9, @precio_pasas, @precio_pasas * 15, 15, 1),
                                                                                                            (4, 10, @precio_fresa, @precio_fresa * 12, 12, 1),
                                                                                                            (4, 11, @precio_chocolate_avellana, @precio_chocolate_avellana * 8, 8, 1),
                                                                                                            (4, 12, @precio_almendra, @precio_almendra * 4, 4, 1),
                                                                                                            (4, 13, @precio_cacahuate, @precio_cacahuate * 25, 25, 1),
                                                                                                            (4, 14, @precio_coco, @precio_coco * 10, 10, 1);


INSERT INTO insumos_inventarios (compra_id, insumo_id, fecha_expiracion, costo, cantidad, medida_id) VALUES