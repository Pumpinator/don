INSERT INTO dongalleto.measure (name, symbol)
VALUES ('Gramo', 'gr'),
       ('Kilogramo', 'kg'),
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
VALUES ('contacto1@proveedor.com', 'Proveedor Harinas SA', 'Ingredientes'),
       ('contacto2@proveedor.com', 'Lácteos del Centro', 'Lácteos'),
       ('contacto3@proveedor.com', 'Distribuidora Dulces SA', 'Azúcar y Edulcorantes');

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
VALUES (200, 2, 1, 1), -- Harina para Chispas de Chocolate
       (100, 2, 2, 1), -- Azúcar para Chispas de Chocolate
       (50, 2, 3, 1),  -- Mantequilla para Chispas de Chocolate
       (2, 1, 4, 1),   -- Huevos para Chispas de Chocolate
       (100, 2, 5, 1), -- Leche para Chispas de Chocolate
       (100, 2, 6, 1), -- Leche condensada para Chispas de Chocolate
       (10, 2, 7, 1),  -- Polvo para hornear para Chispas de Chocolate
       (5, 2, 8, 1),   -- Vainilla para Chispas de Chocolate
       (5, 2, 9, 1),   -- Sal para Chispas de Chocolate
       (30, 1, 13, 1); -- Chispas de Chocolate para Chispas de Chocolate
