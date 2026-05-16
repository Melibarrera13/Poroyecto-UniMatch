# 06 — Modelo Entidad-Relación (MER)

## Entidades principales (PostgreSQL)

### UNIVERSIDAD
- id_universidad (PK)
- nombre
- pais

### USUARIO
- id_usuario (PK)
- nombre
- email (UNIQUE, NOT NULL)
- contrasena_hash
- pais
- idioma
- id_universidad (FK)

### TEMA
- id_tema (PK)
- nombre_estandar
- area

### ALIAS_TEMA
- id_alias (PK)
- texto_alias
- idioma
- id_tema (FK)

### USUARIO_TEMA (Tabla de relación)
- id_usuario (FK)
- id_tema (FK)
- nivel
- objetivo
PK compuesta: (id_usuario, id_tema)

### HORARIO_DISPONIBLE
- id_horario (PK)
- dia
- hora_inicio
- hora_fin
- zona_horaria
- id_usuario (FK)

### MATCH
- id_match (PK)
- id_usuario1 (FK)
- id_usuario2 (FK)
- id_tema (FK)
- estado
- fecha_match
- puntaje_compatibilidad

### MENSAJE
- id_mensaje (PK)
- id_match (FK)
- id_emisor (FK)
- contenido
- fecha_hora
- leido

---

## Relaciones principales
- UNIVERSIDAD 1 --- N USUARIO
- USUARIO N --- N TEMA (por USUARIO_TEMA)
- TEMA 1 --- N ALIAS_TEMA
- USUARIO 1 --- N HORARIO_DISPONIBLE
- MATCH relaciona 2 USUARIOS y 1 TEMA
- MATCH 1 --- N MENSAJE

---

## Restricciones relevantes
- Email único.
- `id_usuario1 != id_usuario2`.
- Estado de match limitado a valores válidos.
- Evitar duplicar match activo para mismo par+tema.
