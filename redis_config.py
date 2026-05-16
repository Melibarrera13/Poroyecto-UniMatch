-- ============================================================
-- UniMatch 2.0 - Datos iniciales (Seed)
-- Archivo: seed_data.sql
-- ============================================================

-- UNIVERSIDADES
INSERT INTO UNIVERSIDAD(nombre, pais) VALUES
('Universidad Nacional de La Rioja', 'Argentina'),
('Universidad de Buenos Aires', 'Argentina'),
('Universidad Nacional Autónoma de México', 'México'),
('Universidad Complutense de Madrid', 'España'),
('Independiente', 'Global');

-- TEMAS
INSERT INTO TEMA(nombre_estandar, area) VALUES
('Bases de Datos Relacionales', 'Informática'),
('Normalización', 'Informática'),
('SQL Avanzado', 'Informática'),
('Estructuras de Datos', 'Programación'),
('Álgebra Lineal', 'Matemática'),
('Cálculo Diferencial', 'Matemática'),
('Redes de Computadoras', 'Informática');

-- ALIAS_TEMA
INSERT INTO ALIAS_TEMA(texto_alias, idioma, id_tema) VALUES
('DB Relational', 'Ingles', 1),
('Relational Databases', 'Ingles', 1),
('Normalisation', 'Ingles', 2),
('Normalizacion', 'Espanol', 2),
('Advanced SQL', 'Ingles', 3),
('SQL avanzado', 'Espanol', 3);

-- USUARIOS (hash ficticio para ejemplo académico)
INSERT INTO USUARIO(nombre, email, contrasena_hash, pais, idioma, id_universidad) VALUES
('Ana Rojas', 'ana@unimatch.com', 'HASH_BCRYPT_ANA', 'Argentina', 'Espanol', 1),
('Luis Perez', 'luis@unimatch.com', 'HASH_BCRYPT_LUIS', 'Argentina', 'Espanol', 2),
('Maria Lopez', 'maria@unimatch.com', 'HASH_BCRYPT_MARIA', 'México', 'Espanol', 3),
('John Smith', 'john@unimatch.com', 'HASH_BCRYPT_JOHN', 'Estados Unidos', 'Ingles', 5),
('Carla Diaz', 'carla@unimatch.com', 'HASH_BCRYPT_CARLA', 'España', 'Espanol', 4);

-- USUARIO_TEMA
INSERT INTO USUARIO_TEMA(id_usuario, id_tema, nivel, objetivo) VALUES
(1, 1, 'intermedio', 'practicar'),
(1, 2, 'intermedio', 'repasar'),
(2, 1, 'basico', 'aprender'),
(2, 3, 'basico', 'aprender'),
(3, 1, 'avanzado', 'explicar'),
(3, 2, 'avanzado', 'explicar'),
(4, 1, 'intermedio', 'practicar'),
(4, 3, 'intermedio', 'practicar'),
(5, 1, 'intermedio', 'repasar');

-- HORARIOS
INSERT INTO HORARIO_DISPONIBLE(dia, hora_inicio, hora_fin, zona_horaria, id_usuario) VALUES
('Lunes', '15:00', '18:00', 'America/Argentina/Buenos_Aires', 1),
('Miercoles', '10:00', '12:00', 'America/Argentina/Buenos_Aires', 2),
('Lunes', '16:00', '19:00', 'America/Mexico_City', 3),
('Martes', '09:00', '11:00', 'America/New_York', 4),
('Lunes', '17:00', '20:00', 'Europe/Madrid', 5);

-- MATCHES (ejemplo)
INSERT INTO MATCH(id_usuario1, id_usuario2, id_tema, estado, puntaje_compatibilidad)
VALUES (1, 2, 1, 'pendiente', 92.50);

-- MENSAJES (ejemplo)
INSERT INTO MENSAJE(id_match, id_emisor, contenido)
VALUES (1, 1, 'Hola Luis, ¿querés repasar SQL de joins conmigo?');
