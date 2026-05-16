# Arquitectura General (Texto)

## Componentes

[Cliente Web/Móvil]
        |
        v
[API REST / Controladores]
        |
        v
[Servicios de Dominio]
    - MatchingService
    - UserService (futuro)
    - MessagingService (futuro)
        |
        v
[Capa DAO]
    |-------------------------------|
    | PostgreSQL DAO | Redis DAO | Neo4j DAO |
    |-------------------------------|
        |
        v
[Persistencia]
- PostgreSQL (ACID)
- Redis (Cache/Sesiones)
- Neo4j (Grafo/Recomendaciones)

---

## Flujo de matching (simplificado)

1. Usuario solicita recomendaciones.
2. Se consulta Redis:
   - si existe caché → se devuelve.
3. Si no existe caché:
   - PostgreSQL filtra candidatos por tema.
   - PostgreSQL obtiene nivel/objetivo.
   - PostgreSQL verifica disponibilidad horaria.
   - Neo4j calcula proximidad indirecta.
4. Se calcula puntaje.
5. Se guarda resultado en Redis (cache:matches:{userId}).
6. Usuario selecciona candidato y confirma.
7. Se crea MATCH en PostgreSQL y relación MATCHED_WITH en Neo4j.
