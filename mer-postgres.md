# API (Diseño Propuesto) — Endpoints UniMatch 2.0

Este archivo define un diseño propuesto de endpoints REST para un futuro backend.

---

## Autenticación

### POST /api/auth/register
Registra un usuario.

**Body**
```json
{
  "nombre": "Ana",
  "email": "ana@mail.com",
  "password": "1234",
  "pais": "Argentina",
  "idioma": "Espanol",
  "idUniversidad": 1
}
```

### POST /api/auth/login
Inicia sesión y crea sesión en Redis.

**Body**
```json
{
  "email": "ana@mail.com",
  "password": "1234"
}
```

**Response**
```json
{
  "token": "jwt_o_token_temporal",
  "userId": 1
}
```

---

## Temas

### GET /api/topics?search=sql
Busca temas.

### POST /api/users/{id}/topics
Asocia un tema a un usuario.

---

## Matching

### GET /api/matching/recommendations?userId=1&topicId=1
Obtiene recomendaciones.

### POST /api/matching/confirm
Confirma un match.

**Body**
```json
{
  "userId1": 1,
  "userId2": 3,
  "topicId": 1,
  "score": 110.5
}
```

---

## Mensajería

### GET /api/matches/{id}/messages
Lista mensajes.

### POST /api/matches/{id}/messages
Envía mensaje.

---

## Observación
El presente repositorio se centra en la capa de datos (Bases de Datos II).
La API queda documentada como extensión natural del diseño.
