"""Neo4j Configuration - UniMatch 2.0

Neo4j se utiliza para modelar relaciones y recomendaciones por proximidad.
Requiere: neo4j (Neo4j Python Driver)
"""

NEO4J_CONFIG = {
    "uri": "bolt://localhost:7687",
    "user": "neo4j",
    "password": "password"
}
