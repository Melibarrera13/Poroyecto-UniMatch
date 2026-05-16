"""PostgreSQL Configuration - UniMatch 2.0

Este archivo centraliza parámetros de conexión para PostgreSQL.
En un entorno real se recomienda usar variables de entorno y un gestor de secretos.

Requiere: psycopg2
"""

POSTGRES_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "unimatch",
    "user": "postgres",
    "password": "postgres"
}
