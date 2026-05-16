-- ============================================================
-- UniMatch 2.0 - Índices y optimización
-- Archivo: indices.sql
-- ============================================================

-- USUARIO
CREATE INDEX IF NOT EXISTS idx_usuario_universidad
ON USUARIO(id_universidad);

-- USUARIO_TEMA
CREATE INDEX IF NOT EXISTS idx_usuario_tema_tema
ON USUARIO_TEMA(id_tema);

CREATE INDEX IF NOT EXISTS idx_usuario_tema_filtros
ON USUARIO_TEMA(id_tema, nivel, objetivo);

-- HORARIO_DISPONIBLE
CREATE INDEX IF NOT EXISTS idx_horario_usuario
ON HORARIO_DISPONIBLE(id_usuario);

-- MATCH
CREATE INDEX IF NOT EXISTS idx_match_estado
ON MATCH(estado);

CREATE INDEX IF NOT EXISTS idx_match_tema
ON MATCH(id_tema);

CREATE INDEX IF NOT EXISTS idx_match_fecha
ON MATCH(fecha_match);

-- Índice único parcial para evitar duplicados de match activo por par+tema
-- Se considera activo a: pendiente o aceptado
CREATE UNIQUE INDEX IF NOT EXISTS uq_match_activo_par_tema
ON MATCH(LEAST(id_usuario1, id_usuario2), GREATEST(id_usuario1, id_usuario2), id_tema)
WHERE estado IN ('pendiente','aceptado');

-- MENSAJE
CREATE INDEX IF NOT EXISTS idx_mensaje_match
ON MENSAJE(id_match);

CREATE INDEX IF NOT EXISTS idx_mensaje_fecha
ON MENSAJE(fecha_hora);
