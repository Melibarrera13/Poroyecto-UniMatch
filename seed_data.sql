# 12 — Seguridad y Privacidad

## Principios generales
UniMatch 2.0 debe respetar estándares mínimos de seguridad informática y protección de datos personales.

---

## Seguridad en PostgreSQL

### Contraseñas
- No se almacenan contraseñas en texto plano.
- Se almacena un hash seguro (por ejemplo bcrypt/argon2).

### Restricciones de integridad
- Uso de constraints CHECK y FK para evitar datos inconsistentes.
- Uso de UNIQUE para emails.

### Acceso por roles
Se recomienda crear roles:

- rol_app: acceso limitado a tablas necesarias.
- rol_admin: mantenimiento y auditoría.

---

## Seguridad en Redis
Redis almacena datos temporales, por lo tanto:

- sesiones con TTL
- tokens temporales con expiración
- evitar almacenar datos sensibles innecesarios

Se recomienda:
- habilitar contraseña Redis
- restringir acceso a red privada

---

## Seguridad en Neo4j
- Uso de credenciales seguras.
- Restricción de permisos para queries.

---

## Privacidad del usuario
El sistema debe garantizar:

- posibilidad de eliminación total de cuenta (derecho al olvido),
- anonimización de datos estadísticos,
- no compartir email en recomendaciones,
- consentimiento explícito para almacenar datos.

---

## Protección contra abuso
- límite de recomendaciones por hora,
- bloqueo de spam en mensajería,
- registro de intentos fallidos de login (futuro).

---

## Observación académica
La seguridad se considera parte integral del diseño de base de datos, ya que el almacenamiento y acceso a datos es un punto crítico de exposición.
