# 05 — Modelo Políglota y Justificación

## Definición
El modelo políglota consiste en utilizar diferentes bases de datos según el tipo de información y los requerimientos de consulta.

UniMatch 2.0 adopta un enfoque políglota debido a que el sistema presenta:

- datos transaccionales estructurados,
- necesidad de caché y almacenamiento temporal,
- relaciones complejas de recomendación.

---

## 1. PostgreSQL (Relacional)

### Justificación
PostgreSQL se utiliza como base principal porque garantiza:

- integridad referencial,
- consistencia ACID,
- constraints y validación,
- soporte de índices avanzados.

### Datos almacenados
- usuarios
- universidades
- temas
- alias de temas
- horarios disponibles
- matches
- mensajes

---

## 2. Redis (Clave-Valor)

### Justificación
Redis se utiliza porque permite:

- lectura y escritura en memoria extremadamente rápida,
- expiración automática de claves (TTL),
- estructuras como hash, list, sorted set,
- implementación eficiente de rankings.

### Datos almacenados
- sesiones activas: `session:{userId}`
- caché de recomendaciones: `cache:matches:{userId}`
- ranking de temas: `ranking:topics`
- tokens temporales: `token:reset:{email}`

---

## 3. Neo4j (Grafo)

### Justificación
Neo4j permite representar relaciones académicas de manera natural, soportando:

- consultas de proximidad,
- búsqueda de comunidades,
- recomendaciones indirectas,
- análisis de relaciones entre temas.

### Datos almacenados
- nodos Usuario
- nodos Tema
- relaciones STUDIES
- relaciones MATCHED_WITH
- relaciones RELATED_TO entre temas

---

## Conclusión
El modelo políglota permite:

- robustez transaccional en PostgreSQL,
- alto rendimiento para datos temporales con Redis,
- recomendaciones inteligentes mediante grafos en Neo4j.
