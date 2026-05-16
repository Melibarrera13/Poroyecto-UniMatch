# Neo4j — Modelo de Nodos y Relaciones

## Nodos

### (:User)
Propiedades sugeridas:
- userId (int)
- nombre (string)
- pais (string)
- idioma (string)

### (:Topic)
Propiedades sugeridas:
- topicId (int)
- nombre (string)
- area (string)

### (:University)
Propiedades sugeridas:
- universityId (int)
- nombre (string)
- pais (string)

---

## Relaciones

### (User)-[:STUDIES]->(Topic)
Propiedades:
- nivel
- objetivo
- updatedAt

### (User)-[:BELONGS_TO]->(University)
Propiedades:
- createdAt

### (User)-[:MATCHED_WITH]->(User)
Propiedades:
- topicId
- score
- createdAt

### (Topic)-[:RELATED_TO]->(Topic)
Propiedades:
- weight (0..1)
- createdAt

---

## Ejemplos de creación de relaciones (Cypher)

```cypher
MATCH (u:User {userId: 1}), (t:Topic {topicId: 10})
MERGE (u)-[:STUDIES {nivel: "intermedio", objetivo: "practicar", updatedAt: datetime()}]->(t);
```

```cypher
MATCH (u1:User {userId: 1}), (u2:User {userId: 2})
MERGE (u1)-[:MATCHED_WITH {topicId: 10, score: 105.5, createdAt: datetime()}]->(u2);
```

```cypher
MATCH (t1:Topic {topicId: 10}), (t2:Topic {topicId: 11})
MERGE (t1)-[:RELATED_TO {weight: 0.8, createdAt: datetime()}]->(t2);
```

---

## Consulta de proximidad (recomendación indirecta)

Buscar usuarios a distancia 2 desde un usuario dado:

```cypher
MATCH (u:User {userId: 1})-[:STUDIES]->(:Topic)<-[:STUDIES]-(other:User)
WHERE other.userId <> 1
RETURN other.userId, other.nombre
LIMIT 20;
```
