-- ============================================================
-- UniMatch 2.0 - Consultas útiles para Matching
-- Archivo: queries_matching.sql
-- ============================================================

-- 1) Buscar candidatos por tema específico (sin incluir al usuario actual)
-- Parámetros:
--   :userId  -> id_usuario actual
--   :topicId -> id_tema
SELECT u.id_usuario, u.nombre, u.pais, u.idioma
FROM USUARIO u
JOIN USUARIO_TEMA ut ON ut.id_usuario = u.id_usuario
WHERE ut.id_tema = 1
  AND u.id_usuario <> 1;

-- 2) Obtener nivel y objetivo del usuario para un tema
SELECT nivel, objetivo
FROM USUARIO_TEMA
WHERE id_usuario = 1 AND id_tema = 1;

-- 3) Verificar si existe match activo duplicado (pendiente o aceptado)
SELECT *
FROM MATCH
WHERE (
    (id_usuario1 = 1 AND id_usuario2 = 2)
 OR (id_usuario1 = 2 AND id_usuario2 = 1)
)
AND id_tema = 1
AND estado IN ('pendiente','aceptado');

-- 4) Obtener mensajes de un match ordenados cronológicamente
SELECT m.id_mensaje, m.contenido, m.fecha_hora, m.leido, u.nombre AS emisor
FROM MENSAJE m
JOIN USUARIO u ON u.id_usuario = m.id_emisor
WHERE m.id_match = 1
ORDER BY m.fecha_hora ASC;

-- 5) Consultar matches aceptados de un usuario
SELECT *
FROM MATCH
WHERE (id_usuario1 = 1 OR id_usuario2 = 1)
AND estado = 'aceptado'
ORDER BY fecha_match DESC;

-- 6) Consultar disponibilidad horaria de un usuario
SELECT dia, hora_inicio, hora_fin, zona_horaria
FROM HORARIO_DISPONIBLE
WHERE id_usuario = 1;

-- 7) Candidatos con mismo idioma y mismo tema (filtro rápido)
SELECT u.id_usuario, u.nombre
FROM USUARIO u
JOIN USUARIO_TEMA ut ON ut.id_usuario = u.id_usuario
WHERE ut.id_tema = 1
  AND u.id_usuario <> 1
  AND u.idioma = (SELECT idioma FROM USUARIO WHERE id_usuario = 1);

-- 8) Estadística: temas más estudiados
SELECT t.nombre_estandar, COUNT(*) AS cantidad_estudiantes
FROM USUARIO_TEMA ut
JOIN TEMA t ON t.id_tema = ut.id_tema
GROUP BY t.nombre_estandar
ORDER BY cantidad_estudiantes DESC;
