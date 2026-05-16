-- ============================================================
-- UniMatch 2.0 - PostgreSQL Schema
-- Materia: Bases de Datos II
-- Archivo: schema_postgresql.sql
-- ============================================================

DROP TABLE IF EXISTS MENSAJE CASCADE;
DROP TABLE IF EXISTS MATCH CASCADE;
DROP TABLE IF EXISTS HORARIO_DISPONIBLE CASCADE;
DROP TABLE IF EXISTS USUARIO_TEMA CASCADE;
DROP TABLE IF EXISTS ALIAS_TEMA CASCADE;
DROP TABLE IF EXISTS USUARIO CASCADE;
DROP TABLE IF EXISTS TEMA CASCADE;
DROP TABLE IF EXISTS UNIVERSIDAD CASCADE;

-- ============================================================
-- TABLA: UNIVERSIDAD
-- ============================================================
CREATE TABLE UNIVERSIDAD (
    id_universidad SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    pais VARCHAR(80) NOT NULL
);

-- ============================================================
-- TABLA: USUARIO
-- ============================================================
CREATE TABLE USUARIO (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL,
    pais VARCHAR(80) NOT NULL,
    idioma VARCHAR(40) NOT NULL,
    id_universidad INT NOT NULL,
    CONSTRAINT fk_usuario_universidad
        FOREIGN KEY (id_universidad)
        REFERENCES UNIVERSIDAD(id_universidad)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ============================================================
-- TABLA: TEMA
-- ============================================================
CREATE TABLE TEMA (
    id_tema SERIAL PRIMARY KEY,
    nombre_estandar VARCHAR(200) NOT NULL UNIQUE,
    area VARCHAR(120) NOT NULL
);

-- ============================================================
-- TABLA: ALIAS_TEMA
-- ============================================================
CREATE TABLE ALIAS_TEMA (
    id_alias SERIAL PRIMARY KEY,
    texto_alias VARCHAR(200) NOT NULL,
    idioma VARCHAR(40) NOT NULL,
    id_tema INT NOT NULL,
    CONSTRAINT fk_alias_tema
        FOREIGN KEY (id_tema)
        REFERENCES TEMA(id_tema)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT uq_alias UNIQUE(texto_alias, idioma)
);

-- ============================================================
-- TABLA: USUARIO_TEMA (relación N:N)
-- ============================================================
CREATE TABLE USUARIO_TEMA (
    id_usuario INT NOT NULL,
    id_tema INT NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    objetivo VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_usuario, id_tema),
    CONSTRAINT fk_usuario_tema_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_usuario_tema_tema
        FOREIGN KEY (id_tema)
        REFERENCES TEMA(id_tema)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT chk_nivel CHECK (nivel IN ('basico', 'intermedio', 'avanzado')),
    CONSTRAINT chk_objetivo CHECK (objetivo IN ('aprender', 'practicar', 'repasar', 'explicar'))
);

-- ============================================================
-- TABLA: HORARIO_DISPONIBLE
-- ============================================================
CREATE TABLE HORARIO_DISPONIBLE (
    id_horario SERIAL PRIMARY KEY,
    dia VARCHAR(12) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    zona_horaria VARCHAR(60) NOT NULL,
    id_usuario INT NOT NULL,
    CONSTRAINT fk_horario_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT chk_dia CHECK (dia IN ('Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo')),
    CONSTRAINT chk_horas CHECK (hora_fin > hora_inicio)
);

-- ============================================================
-- TABLA: MATCH
-- ============================================================
CREATE TABLE MATCH (
    id_match SERIAL PRIMARY KEY,
    id_usuario1 INT NOT NULL,
    id_usuario2 INT NOT NULL,
    id_tema INT NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'pendiente',
    fecha_match TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    puntaje_compatibilidad NUMERIC(5,2) NOT NULL,
    CONSTRAINT fk_match_usuario1
        FOREIGN KEY (id_usuario1)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_match_usuario2
        FOREIGN KEY (id_usuario2)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_match_tema
        FOREIGN KEY (id_tema)
        REFERENCES TEMA(id_tema)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT chk_usuarios_distintos CHECK (id_usuario1 <> id_usuario2),
    CONSTRAINT chk_estado_match CHECK (estado IN ('pendiente','aceptado','rechazado','finalizado'))
);

-- Evitar duplicar match activo mismo par+tema (índice único parcial recomendado)
-- Se crea en indices.sql para mayor claridad.

-- ============================================================
-- TABLA: MENSAJE
-- ============================================================
CREATE TABLE MENSAJE (
    id_mensaje SERIAL PRIMARY KEY,
    id_match INT NOT NULL,
    id_emisor INT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    leido BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_mensaje_match
        FOREIGN KEY (id_match)
        REFERENCES MATCH(id_match)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_mensaje_emisor
        FOREIGN KEY (id_emisor)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
