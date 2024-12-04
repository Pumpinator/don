INSERT INTO dongalleto.measure (name, symbol)
VALUES ('Gramo', 'gr'),
       ('Kilogramo', 'kg'),
       ('Mililitro', 'Ml'),
       ('Litro', 'Lt'),
       ('Pieza', 'pz'),
       ('Peso', '$');

INSERT INTO dongalleto.raw_material (name)
VALUES ('Harina'),
       ('Azúcar'),
       ('Mantequilla'),
       ('Huevos'),
       ('Leche'),
       ('Leche condensada'),
       ('Polvo para hornear'),
       ('Vainilla'),
       ('Sal'),
       ('Avena'),
       ('Pasas'),
       ('Nueces'),
       ('Chispas de Chocolate'),
       ('Chispas de Colores');

INSERT INTO dongalleto.supplier (contact, name, type)
VALUES ('contacto1@proveedor.com', 'Proveedor Harinas SA', 'Empresa'),
       ('contacto2@proveedor.com', 'Lácteos del Centro', 'Empresa'),
       ('contacto3@proveedor.com', 'Distribuidora Dulces SA', 'Empresa'),
       ('4777881300', 'Costco Wholesale', 'Mercado'),
       ('https://www.mercadolibre.com.mx/ayuda', 'Mercado Libre', 'Mercado');

INSERT INTO dongalleto.raw_material_supplier (raw_material_id, supplier_id)
VALUES (1, 1),  -- Harina de Proveedor Harinas SA
       (2, 1),  -- Azúcar de Proveedor Harinas SA
       (3, 1),  -- Mantequilla
       (4, 1),  -- Huevos
       (5, 2),  -- Leche
       (6, 2),  -- Leche condensada
       (7, 3),  -- Polvo para hornear
       (8, 3),  -- Vainilla
       (9, 3),  -- Sal
       (10, 1), -- Avena
       (11, 1), -- Pasas
       (12, 1), -- Nueces
       (13, 3), -- Chispas de Chocolate
       (14, 3), -- Chispas de Colores
       (1, 4),  -- Harina de Costco Wholesale
       (2, 4),  -- Azúcar de Costco Wholesale
       (3, 4),  -- Mantequilla de Costco Wholesale
       (4, 4),  -- Huevos de Costco Wholesale
       (5, 4),  -- Leche de Costco Wholesale
       (6, 4),  -- Leche condensada de Costco Wholesale
       (7, 4),  -- Polvo para hornear de Costco Wholesale
       (8, 4),  -- Vainilla de Costco Wholesale
       (9, 4),  -- Sal de Costco Wholesale
       (10, 4), -- Avena de Costco Wholesale
       (11, 4), -- Pasas de Costco Wholesale
       (12, 4), -- Nueces de Costco Wholesale
       (13, 4), -- Chispas de Chocolate de Costco Wholesale
       (14, 4); -- Chispas de Colores de Costco Wholesale

INSERT INTO dongalleto.purchase (date, total)
VALUES ('2021-01-01 10:00:00', 0),
       ('2021-01-02 10:00:00', 0),
       ('2021-01-03 10:00:00', 0),
       ('2021-01-04 10:00:00', 0);

INSERT INTO dongalleto.purchase_detail (purchase_id, raw_material_id, measure_id, quantity, total_price, unit_price,
                                        supplier_id)
VALUES (1, 1, 2, 1000, 1000, 1, 1), -- 1 kg de Harina de Proveedor Harinas SA
       (1, 2, 2, 500, 500, 1, 1),   -- 500 gr de Azúcar de Proveedor Harinas SA
       (1, 3, 2, 250, 250, 1, 1),   -- 250 gr de Mantequilla de Proveedor Harinas SA
       (1, 4, 1, 12, 12, 1, 1),     -- 12 Huevos de Proveedor Harinas SA
       (1, 5, 2, 500, 500, 1, 2),   -- 500 gr de Leche de Lácteos del Centro
       (1, 6, 2, 500, 500, 1, 2),   -- 500 gr de Leche condensada de Lácteos del Centro
       (1, 7, 2, 50, 50, 1, 3),     -- 50 gr de Polvo para hornear de Distribuidora Dulces SA
       (1, 8, 2, 25, 25, 1, 3),     -- 25 gr de Vainilla de Distribuidora Dulces SA
       (1, 9, 2, 25, 25, 1, 3),     -- 25 gr de Sal de Distribuidora Dulces SA
       (1, 10, 2, 500, 500, 1, 1),  -- 500 gr de Avena de Proveedor Harinas SA
       (1, 11, 2, 250, 250, 1, 1),  -- 250 gr de Pasas de Proveedor Harinas SA
       (1, 12, 2, 250, 250, 1, 1),  -- 250 gr de Nueces de Proveedor Harinas SA
       (1, 13, 2, 100, 100, 1, 3),  -- 100 gr de Chispas de Chocolate de Distribuidora Dulces SA
       (1, 14, 2, 100, 100, 1, 3),  -- 100 gr de Chispas de Colores de Distribuidora Dulces SA
       (2, 1, 2, 1000, 1000, 1, 4), -- 1 kg de Harina de Costco Wholesale
       (2, 2, 2, 500, 500, 1, 4),   -- 500 gr de Azúcar de Costco Wholesale
       (2, 3, 2, 250, 250, 1, 4),   -- 250 gr de Mantequilla de Costco Wholesale
       (2, 4, 1, 12, 12, 1, 4),     -- 12 Huevos de Costco Wholesale
       (2, 5, 2, 500, 500, 1, 4),   -- 500 gr de Leche de Costco Wholesale
       (2, 6, 2, 500, 500, 1, 4),   -- 500 gr de Leche condensada de Costco Wholesale
       (2, 7, 2, 50, 50, 1, 4),     -- 50 gr de Polvo para hornear de Costco Wholesale
       (2, 8, 2, 25, 25, 1, 4),     -- 25 gr de Vainilla de Costco Wholesale
       (2, 9, 2, 25, 25, 1, 4),     -- 25 gr de Sal de Costco Wholesale
       (2, 10, 2, 500, 500, 1, 4),  -- 500 gr de Avena de Costco Wholesale
       (2, 11, 2, 250, 250, 1, 4),  -- 250 gr de Pasas de Costco Wholesale
       (2, 12, 2, 250, 250, 1, 4),  -- 250 gr de Nueces de Costco Wholesale
       (2, 13, 2, 100, 100, 1, 4),  -- 100 gr de Chispas de Chocolate de Costco Wholesale
       (2, 14, 2, 100, 100, 1, 4),  -- 100 gr de Chispas de Colores de Costco Wholesale
       (3, 1, 2, 1000, 1000, 1, 1), -- 1 kg de Harina de Proveedor Harinas SA
       (3, 2, 2, 500, 500, 1, 1),   -- 500 gr de Azúcar de Proveedor Harinas SA
       (3, 3, 2, 250, 250, 1, 1),   -- 250 gr de Mantequilla de Proveedor Harinas SA
       (3, 4, 1, 12, 12, 1, 1),     -- 12 Huevos de Proveedor Harinas SA
       (3, 5, 2, 500, 500, 1, 2),   -- 500 gr de Leche de Lácteos del Centro
       (3, 6, 2, 500, 500, 1, 2),   -- 500 gr de Leche condensada de Lácteos del Centro
       (3, 7, 2, 50, 50, 1, 3),     -- 50 gr de Polvo para hornear de Distribuidora Dulces SA
       (3, 8, 2, 25, 25, 1, 3),     -- 25 gr de Vainilla de Distribuidora Dulces SA
       (3, 9, 2, 25, 25, 1, 3),     -- 25 gr de Sal de Distribuidora Dulces SA
       (3, 10, 2, 500, 500, 1, 1),  -- 500 gr de Avena de Proveedor Harinas SA
       (3, 11, 2, 250, 250, 1, 1),  -- 250 gr de Pasas de Proveedor Harinas SA
       (3, 12, 2, 250, 250, 1, 1),  -- 250 gr de Nueces de Proveedor Harinas SA
       (3, 13, 2, 100, 100, 1, 3),  -- 100 gr de Chispas de Chocolate de Distribuidora Dulces SA
       (3, 14, 2, 100, 100, 1, 3),  -- 100 gr de Chispas de Colores de Distribuidora Dulces SA
       (4, 1, 2, 1000, 1000, 1, 4), -- 1 kg de Harina de Costco Wholesale
       (4, 2, 2, 500, 500, 1, 4),   -- 500 gr de Azúcar de Costco Wholesale
       (4, 3, 2, 250, 250, 1, 4),   -- 250 gr de Mantequilla de Costco Wholesale
       (4, 4, 1, 12, 12, 1, 4),     -- 12 Huevos de Costco Wholesale
       (4, 5, 2, 500, 500, 1, 4),   -- 500 gr de Leche de Costco Wholesale
       (4, 6, 2, 500, 500, 1, 4),   -- 500 gr de Leche condensada de Costco Wholesale
       (4, 7, 2, 50, 50, 1, 4),     -- 50 gr de Polvo para hornear de Costco Wholesale
       (4, 8, 2, 25, 25, 1, 4),     -- 25 gr de Vainilla de Costco Wholesale
       (4, 9, 2, 25, 25, 1, 4),     -- 25 gr de Sal de Costco Wholesale
       (4, 10, 2, 500, 500, 1, 4),  -- 500 gr de Avena de Costco Wholesale
       (4, 11, 2, 250, 250, 1, 4),  -- 250 gr de Pasas de Costco Wholesale
       (4, 12, 2, 250, 250, 1, 4); -- 250 gr de Nueces de Costco Wholesale


INSERT INTO dongalleto.raw_material_inventory (quantity, cost, expiration_date, measure_id, purchase_id, raw_material_id, supplier_id)
VALUES
    (1000, 1000, '2025-01-01', 2, 1, 1, 1), -- 1 kg of Harina from purchase 1
    (500, 500, '2025-01-01', 2, 1, 2, 1),   -- 500 gr of Azúcar from purchase 1
    (250, 250, '2025-01-01', 2, 1, 3, 1),   -- 250 gr of Mantequilla from purchase 1
    (12, 12, '2025-01-01', 1, 1, 4, 1),     -- 12 Huevos from purchase 1
    (500, 500, '2025-01-01', 2, 1, 5, 2),   -- 500 gr of Leche from purchase 1
    (500, 500, '2025-01-01', 2, 1, 6, 2),   -- 500 gr of Leche condensada from purchase 1
    (50, 50, '2025-01-01', 2, 1, 7, 3),     -- 50 gr of Polvo para hornear from purchase 1
    (25, 25, '2025-01-01', 2, 1, 8, 3),     -- 25 gr of Vainilla from purchase 1
    (25, 25, '2025-01-01', 2, 1, 9, 3),     -- 25 gr of Sal from purchase 1
    (500, 500, '2025-01-01', 2, 1, 10, 1),  -- 500 gr of Avena from purchase 1
    (250, 250, '2025-01-01', 2, 1, 11, 1),  -- 250 gr of Pasas from purchase 1
    (250, 250, '2025-01-01', 2, 1, 12, 1),  -- 250 gr of Nueces from purchase 1
    (100, 100, '2025-01-01', 2, 1, 13, 3),  -- 100 gr of Chispas de Chocolate from purchase 1
    (100, 100, '2025-01-01', 2, 1, 14, 3),  -- 100 gr of Chispas de Colores from purchase 1
    (1000, 1000, '2025-01-02', 2, 2, 1, 4), -- 1 kg of Harina from purchase 2
    (500, 500, '2025-01-02', 2, 2, 2, 4),   -- 500 gr of Azúcar from purchase 2
    (250, 250, '2025-01-02', 2, 2, 3, 4),   -- 250 gr of Mantequilla from purchase 2
    (12, 12, '2025-01-02', 1, 2, 4, 4),     -- 12 Huevos from purchase 2
    (500, 500, '2025-01-02', 2, 2, 5, 4),   -- 500 gr of Leche from purchase 2
    (500, 500, '2025-01-02', 2, 2, 6, 4),   -- 500 gr of Leche condensada from purchase 2
    (50, 50, '2025-01-02', 2, 2, 7, 4),     -- 50 gr of Polvo para hornear from purchase 2
    (25, 25, '2025-01-02', 2, 2, 8, 4),     -- 25 gr of Vainilla from purchase 2
    (25, 25, '2025-01-02', 2, 2, 9, 4),     -- 25 gr of Sal from purchase 2
    (500, 500, '2025-01-02', 2, 2, 10, 4),  -- 500 gr of Avena from purchase 2
    (250, 250, '2025-01-02', 2, 2, 11, 4),  -- 250 gr of Pasas from purchase 2
    (250, 250, '2025-01-02', 2, 2, 12, 4),  -- 250 gr of Nueces from purchase 2
    (100, 100, '2025-01-02', 2, 2, 13, 4),  -- 100 gr of Chispas de Chocolate from purchase 2
    (100, 100, '2025-01-02', 2, 2, 14, 4),  -- 100 gr of Chispas de Colores from purchase 2
    (1000, 1000, '2025-01-03', 2, 3, 1, 1), -- 1 kg of Harina from purchase 3
    (500, 500, '2025-01-03', 2, 3, 2, 1),   -- 500 gr of Azúcar from purchase 3
    (250, 250, '2025-01-03', 2, 3, 3, 1),   -- 250 gr of Mantequilla from purchase 3
    (12, 12, '2025-01-03', 1, 3, 4, 1),     -- 12 Huevos from purchase 3
    (500, 500, '2025-01-03', 2, 3, 5, 2),   -- 500 gr of Leche from purchase 3
    (500, 500, '2025-01-03', 2, 3, 6, 2),   -- 500 gr of Leche condensada from purchase 3
    (50, 50, '2025-01-03', 2, 3, 7, 3),     -- 50 gr of Polvo para hornear from purchase 3
    (25, 25, '2025-01-03', 2, 3, 8, 3),     -- 25 gr of Vainilla from purchase 3
    (25, 25, '2025-01-03', 2, 3, 9, 3),     -- 25 gr of Sal from purchase 3
    (500, 500, '2025-01-03', 2, 3, 10, 1),  -- 500 gr of Avena from purchase 3
    (250, 250, '2025-01-03', 2, 3, 11, 1),  -- 250 gr of Pasas from purchase 3
    (250, 250, '2025-01-03', 2, 3, 12, 1),  -- 250 gr of Nueces from purchase 3
    (100, 100, '2025-01-03', 2, 3, 13, 3),  -- 100 gr of Chispas de Chocolate from purchase 3
    (100, 100, '2025-01-03', 2, 3, 14, 3),  -- 100 gr of Chispas de Colores from purchase 3
    (1000, 1000, '2025-01-04', 2, 4, 1, 4), -- 1 kg of Harina from purchase 4
    (500, 500, '2025-01-04', 2, 4, 2, 4),   -- 500 gr of Azúcar from purchase 4
    (250, 250, '2025-01-04', 2, 4, 3, 4),   -- 250 gr of Mantequilla from purchase 4
    (12, 12, '2025-01-04', 1, 4, 4, 4),     -- 12 Huevos from purchase 4
    (500, 500, '2025-01-04', 2, 4, 5, 4),   -- 500 gr of Leche from purchase 4
    (500, 500, '2025-01-04', 2, 4, 6, 4),   -- 500 gr of Leche condensada from purchase 4
    (50, 50, '2025-01-04', 2, 4, 7, 4),     -- 50 gr of Polvo para hornear from purchase 4
    (25, 25, '2025-01-04', 2, 4, 8, 4),     -- 25 gr of Vainilla from purchase 4
    (25, 25, '2025-01-04', 2, 4, 9, 4),     -- 25 gr of Sal from purchase 4
    (500, 500, '2025-01-04', 2, 4, 10, 4),  -- 500 gr of Avena from purchase 4
    (250, 250, '2025-01-04', 2, 4, 11, 4),  -- 250 gr of Pasas from purchase 4
    (250, 250, '2025-01-04', 2, 4, 12, 4);  -- 250 gr of Nueces from purchase 4

INSERT INTO dongalleto.cookie (name, price)
VALUES ('Chispas de Chocolate', 10.50),
       ('Avena y Pasas', 8.75),
       ('Mantequilla', 7.20),
       ('Vainilla', 6.90),
       ('Nuez', 6.90),
       ('Especial', 6.90);

INSERT INTO dongalleto.recipe (cost, name, quantity, cookie_id, instructions, measure_id)
VALUES (15.00, 'Chispas de Chocolate', 1, 1, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2),
       (12.00, 'Avena y Pasas', 1.5, 2, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2),
       (10.00, 'Mantequilla', 1, 3, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2),
       (8.50, 'Vainilla', 1, 4, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2),
       (8.50, 'Nuez', 1, 5, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2),
       (8.50, 'Especial', 1, 6, 'Mezclar todos los ingredientes y hornear a 180°C por 15 minutos.', 2);

INSERT INTO dongalleto.ingredient (quantity, measure_id, raw_material_id, recipe_id)
VALUES (200, 2, 1, 1),  -- Harina para Chispas de Chocolate
       (100, 2, 2, 1),  -- Azúcar para Chispas de Chocolate
       (50, 2, 3, 1),   -- Mantequilla para Chispas de Chocolate
       (2, 1, 4, 1),    -- Huevos para Chispas de Chocolate
       (100, 2, 5, 1),  -- Leche para Chispas de Chocolate
       (100, 2, 6, 1),  -- Leche condensada para Chispas de Chocolate
       (10, 2, 7, 1),   -- Polvo para hornear para Chispas de Chocolate
       (5, 2, 8, 1),    -- Vainilla para Chispas de Chocolate
       (5, 2, 9, 1),    -- Sal para Chispas de Chocolate
       (30, 1, 13, 1),  -- Chispas de Chocolate para Chispas de Chocolate
       (30, 1, 14, 1),  -- Chispas de Colores para Chispas de Chocolate
       (150, 2, 1, 2),  -- Harina para Avena y Pasas
       (100, 2, 2, 2),  -- Azúcar para Avena y Pasas
       (50, 2, 3, 2),   -- Mantequilla para Avena y Pasas
       (2, 1, 4, 2),    -- Huevos para Avena y Pasas
       (100, 2, 5, 2),  -- Leche para Avena y Pasas
       (100, 2, 6, 2),  -- Leche condensada para Avena y Pasas
       (10, 2, 7, 2),   -- Polvo para hornear para Avena y Pasas
       (5, 2, 8, 2),    -- Vainilla para Avena y Pasas
       (5, 2, 9, 2),    -- Sal para Avena y Pasas
       (150, 2, 10, 2), -- Avena para Avena y Pasas
       (50, 2, 11, 2),  -- Pasas para Avena y Pasas
       (150, 2, 1, 3),  -- Harina para Mantequilla
       (100, 2, 2, 3),  -- Azúcar para Mantequilla
       (50, 2, 3, 3),   -- Mantequilla para Mantequilla
       (2, 1, 4, 3),    -- Huevos para Mantequilla
       (100, 2, 5, 3),  -- Leche para Mantequilla
       (100, 2, 6, 3),  -- Leche condensada para Mantequilla
       (10, 2, 7, 3),   -- Polvo para hornear para Mantequilla
       (5, 2, 8, 3),    -- Vainilla para Mantequilla
       (5, 2, 9, 3),    -- Sal para Mantequilla
       (150, 2, 1, 4),  -- Harina para Vainilla
       (100, 2, 2, 4),  -- Azúcar para Vainilla
       (50, 2, 3, 4),   -- Mantequilla para Vainilla
       (2, 1, 4, 4),    -- Huevos para Vainilla
       (100, 2, 5, 4),  -- Leche para Vainilla
       (100, 2, 6, 4),  -- Leche condensada para Vainilla
       (10, 2, 7, 4),   -- Polvo para hornear para Vainilla
       (5, 2, 8, 4),    -- Vainilla para Vainilla
       (5, 2, 9, 4),    -- Sal para Vainilla
       (150, 2, 1, 5),  -- Harina para Nuez
       (100, 2, 2, 5),  -- Azúcar para Nuez
       (50, 2, 3, 5),   -- Mantequilla para Nuez
       (2, 1, 4, 5),    -- Huevos para Nuez
       (100, 2, 5, 5),  -- Leche para Nuez
       (100, 2, 6, 5),  -- Leche condensada para Nuez
       (10, 2, 7, 5),   -- Polvo para hornear para Nuez
       (5, 2, 8, 5),    -- Vainilla para Nuez
       (5, 2, 9, 5),    -- Sal para Nuez
       (150, 2, 1, 6),  -- Harina para Especial
       (100, 2, 2, 6),  -- Azúcar para Especial
       (50, 2, 3, 6),   -- Mantquilla para Especial
       (2, 1, 4, 6),    -- Huevos para Especial
       (100, 2, 5, 6),  -- Leche para Especial
       (100, 2, 6, 6),  -- Leche condensada para Especial
       (10, 2, 7, 6),   -- Polvo para hornear para Especial
       (5, 2, 8, 6),    -- Vainilla para Especial
       (5, 2, 9, 6); -- Sal para Especial
