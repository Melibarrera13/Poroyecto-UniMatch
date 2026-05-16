# 11 — Índices y Optimización

## Objetivo
Definir índices adecuados para mejorar:

- búsquedas frecuentes de usuarios y temas,
- consultas de matching,
- acceso a mensajes por match,
- validación rápida de duplicados.

---

## Índices recomendados en PostgreSQL

### Tabla USUARIO
- Índice único por email.
- Índice por id_universidad para filtrado institucional.

### Tabla TEMA
- Índice único por nombre_estandar.

### Tabla USUARIO_TEMA
- Índice compuesto (id_tema, nivel, objetivo) para consultas de matching.

### Tabla MATCH
- Índice compuesto (id_usuario1, id_usuario2, id_tema).
- Índice por estado.
- Índice por fecha_match.

### Tabla MENSAJE
- Índice por id_match.
- Índice por fecha_hora para ordenamiento.

---

## Estrategias de optimización del matching

### 1. Pre-filtrado por tema
Antes de evaluar compatibilidad, se filtra por usuarios que compartan el mismo tema.

### 2. Evitar recalcular recomendaciones
Redis almacena caché por usuario para evitar múltiples cálculos en ventanas cortas.

### 3. Consultas por grafo en Neo4j
Se evita realizar joins complejos en PostgreSQL para relaciones indirectas.

---

## Normalización y consistencia
- Modelo en 3FN en PostgreSQL.
- Alias de temas evita duplicación semántica.
- Tabla USUARIO_TEMA representa relación N:N.

---

## Consideraciones de concurrencia
- Inserción de match debe validar duplicados.
- Se recomienda uso de índices únicos parciales para matches activos.

---

## Observación académica
En un sistema real, se mediría performance con EXPLAIN ANALYZE y se ajustarían índices en base a estadísticas.
