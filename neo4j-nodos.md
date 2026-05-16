# Diagrama MER PostgreSQL (Texto)

## Entidades y relaciones

UNIVERSIDAD (1) ─────── (N) USUARIO

USUARIO (N) ─────── (N) TEMA
    Relación materializada en: USUARIO_TEMA

TEMA (1) ─────── (N) ALIAS_TEMA

USUARIO (1) ─────── (N) HORARIO_DISPONIBLE

MATCH relaciona:
- USUARIO (id_usuario1)
- USUARIO (id_usuario2)
- TEMA (id_tema)

MATCH (1) ─────── (N) MENSAJE

---

## Notación compacta

UNIVERSIDAD(id_universidad PK) 1..N USUARIO(id_usuario PK, id_universidad FK)

USUARIO(id_usuario PK) N..N TEMA(id_tema PK)
USUARIO_TEMA(id_usuario FK, id_tema FK) PK(id_usuario,id_tema)

TEMA(id_tema PK) 1..N ALIAS_TEMA(id_alias PK, id_tema FK)

USUARIO(id_usuario PK) 1..N HORARIO_DISPONIBLE(id_horario PK, id_usuario FK)

USUARIO(id_usuario PK) 1..N MATCH(id_match PK, id_usuario1 FK)
USUARIO(id_usuario PK) 1..N MATCH(id_match PK, id_usuario2 FK)

TEMA(id_tema PK) 1..N MATCH(id_match PK, id_tema FK)

MATCH(id_match PK) 1..N MENSAJE(id_mensaje PK, id_match FK)
