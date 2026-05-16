# 10 — Arquitectura General del Sistema

## Enfoque arquitectónico
UniMatch 2.0 adopta una arquitectura en capas:

- Capa de presentación (no incluida en este repositorio)
- API / Controladores (carpeta `api/`)
- Servicios de negocio (carpeta `src/services/`)
- Capa DAO (carpeta `src/dao/`)
- Persistencia (PostgreSQL, Redis, Neo4j)

## Componentes principales

### 1. API REST (futuro)
Responsable de exponer endpoints para:

- registro/login
- búsqueda de temas
- solicitud de matching
- mensajería

### 2. Servicio de Matching
Implementa el algoritmo de compatibilidad y coordina el acceso a las tres bases de datos.

### 3. DAO PostgreSQL
Maneja:
- persistencia de entidades
- transacciones
- constraints
- consultas complejas

### 4. DAO Redis
Maneja:
- sesiones activas
- caché de recomendaciones
- ranking de temas

### 5. DAO Neo4j
Maneja:
- creación de nodos y relaciones
- consultas de proximidad
- recomendaciones indirectas

---

## Flujo general de datos

1. Usuario se registra → PostgreSQL
2. Usuario inicia sesión → Redis crea sesión activa
3. Usuario agrega tema → PostgreSQL + Neo4j (relación STUDIES)
4. Usuario solicita recomendaciones → Servicio Matching
5. Servicio Matching:
   - consulta PostgreSQL para candidatos
   - consulta Neo4j para proximidad
   - guarda caché en Redis
6. Usuario acepta match → PostgreSQL inserta MATCH y Neo4j registra relación
7. Mensajes → PostgreSQL (persistencia) + Redis opcional (no obligatorio)

---

## Consideraciones de diseño
- PostgreSQL mantiene consistencia e integridad.
- Redis reduce latencia y evita recalcular recomendaciones.
- Neo4j permite recomendaciones más ricas sin joins complejos.

---

## Escalabilidad (teórica)
- PostgreSQL: partición de tablas grandes (mensajes/matches).
- Redis: clustering y replicación.
- Neo4j: replicación y sharding (en ediciones avanzadas).

---

## Observación académica
La arquitectura está diseñada para demostrar un caso realista donde una única base de datos no es suficiente para cubrir rendimiento y complejidad de consultas.
