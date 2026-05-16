# Redis — Diseño lógico de Keys

## Objetivo
Redis se utiliza como almacenamiento temporal en memoria para mejorar rendimiento.

---

## Keys principales

### Sesiones
- Key: `session:{userId}`
- Tipo: HASH
- TTL: 3600 segundos (1 hora)

Ejemplo:
```
HSET session:15 token "abc123" createdAt "2026-05-16T10:00:00"
EXPIRE session:15 3600
```

---

### Caché de recomendaciones
- Key: `cache:matches:{userId}`
- Tipo: LIST o JSON string
- TTL: 600 segundos (10 minutos)

Ejemplo:
```
LPUSH cache:matches:15 "{...json...}"
EXPIRE cache:matches:15 600
```

---

### Ranking de temas más consultados
- Key: `ranking:topics`
- Tipo: SORTED SET

Ejemplo:
```
ZINCRBY ranking:topics 1 "Bases de Datos"
ZINCRBY ranking:topics 1 "Álgebra Lineal"
ZRANGE ranking:topics 0 9 WITHSCORES
```

---

### Tokens temporales (recuperación)
- Key: `token:reset:{email}`
- Tipo: STRING
- TTL: 900 segundos (15 minutos)

Ejemplo:
```
SET token:reset:usuario@mail.com "tokenXYZ" EX 900
```
