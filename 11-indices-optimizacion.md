# 08 — Reglas de Negocio

## Reglas de usuario
1. El email debe ser único y obligatorio.
2. Un usuario debe estar asociado a una universidad (puede existir una universidad genérica "Independiente").
3. El usuario debe registrar al menos un tema para poder recibir recomendaciones.

## Reglas de temas
4. Un tema tiene un nombre estándar único.
5. Un tema puede tener múltiples alias por idioma.
6. Un alias pertenece obligatoriamente a un tema.

## Reglas de disponibilidad horaria
7. Un usuario puede registrar múltiples bloques horarios.
8. La hora_fin debe ser mayor que hora_inicio.
9. El día debe ser un valor válido (Lunes a Domingo).

## Reglas de matching
10. Un match siempre se genera para un tema específico.
11. Un match relaciona dos usuarios diferentes (id_usuario1 != id_usuario2).
12. No puede existir un match activo duplicado para el mismo par de usuarios y tema.
13. El estado de un match solo puede ser:
    - pendiente
    - aceptado
    - rechazado
    - finalizado
14. Un match en estado rechazado o finalizado no permite mensajes nuevos.

## Reglas de mensajería
15. Un mensaje debe pertenecer a un match existente.
16. El emisor debe ser uno de los usuarios del match.
17. Los mensajes se ordenan por fecha_hora.
18. El sistema permite marcar un mensaje como leído.

## Reglas de Redis
19. Una sesión activa expira automáticamente tras un tiempo de inactividad.
20. La caché de recomendaciones tiene TTL para evitar inconsistencia.
21. El ranking de temas se actualiza por cada búsqueda realizada.

## Reglas de Neo4j
22. Cada usuario debe existir como nodo en el grafo.
23. Cada tema debe existir como nodo en el grafo.
24. La relación (User)-[:STUDIES]->(Topic) incluye propiedades nivel y objetivo.
25. Las recomendaciones indirectas se basan en proximidad de segundo y tercer grado.
