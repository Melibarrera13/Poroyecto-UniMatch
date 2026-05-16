# 04 — Especificaciones del Producto

## Objetivo funcional
Conectar estudiantes globalmente según coincidencia académica basada en temas específicos.

## Funcionalidades principales

### 1. Registro e inicio de sesión
- Registro con email único.
- Almacenamiento seguro de contraseña mediante hash.
- Sesiones activas gestionadas en Redis.

### 2. Perfil de usuario
El usuario puede indicar:
- país,
- idioma,
- universidad,
- temas de interés,
- nivel y objetivo para cada tema.

### 3. Gestión de temas
- Los temas se registran con nombre estándar y área.
- Se admiten alias por idioma (sinónimos o variaciones).

### 4. Disponibilidad horaria
- El usuario puede registrar bloques horarios.
- Se incluye zona horaria para compatibilizar horarios internacionales.

### 5. Matching
- El sistema calcula un puntaje de compatibilidad.
- Se evita duplicar matches activos por par de usuarios y tema.
- Estados del match:
  - pendiente
  - aceptado
  - rechazado
  - finalizado

### 6. Mensajería
- Cada match habilita un canal de mensajes.
- El sistema guarda mensajes en PostgreSQL.
- Se permite marcar mensajes como leídos.

### 7. Recomendaciones avanzadas
- Redis almacena caché de recomendaciones.
- Neo4j permite recomendaciones indirectas por cercanía en grafo.

### 8. Ranking de temas
- Redis mantiene ranking de temas más consultados.
- Permite análisis de tendencias académicas.

## Requisitos no funcionales
- Consistencia transaccional en PostgreSQL.
- Baja latencia en recomendaciones mediante Redis.
- Escalabilidad de relaciones complejas mediante Neo4j.
- Seguridad: cifrado de contraseñas y tokens.
- Auditoría mínima de eventos críticos.

## Suposiciones de implementación
- API REST (futura implementación).
- Capa DAO desacoplada para facilitar mantenimiento.
- Uso de Docker recomendado (no obligatorio para este trabajo).
