"""Módulo de conexión PostgreSQL - UniMatch 2.0"""

import psycopg2
from psycopg2.extras import RealDictCursor
from src.config.postgres_config import POSTGRES_CONFIG


class PostgresConnection:
    """Clase utilitaria para obtener conexiones PostgreSQL."""

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host=POSTGRES_CONFIG["host"],
            port=POSTGRES_CONFIG["port"],
            dbname=POSTGRES_CONFIG["database"],
            user=POSTGRES_CONFIG["user"],
            password=POSTGRES_CONFIG["password"],
            cursor_factory=RealDictCursor
        )
