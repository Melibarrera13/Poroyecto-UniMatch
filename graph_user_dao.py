"""MatchDAO - Acceso a datos de la entidad MATCH (PostgreSQL)"""

from src.dao.postgres.postgres_connection import PostgresConnection


class MatchDAO:

    def crear_match(self, id_usuario1, id_usuario2, id_tema, puntaje, estado="pendiente"):
        sql = """
        INSERT INTO MATCH(id_usuario1, id_usuario2, id_tema, estado, puntaje_compatibilidad)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_match;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario1, id_usuario2, id_tema, estado, puntaje))
                row = cur.fetchone()
                conn.commit()
                return row["id_match"]

    def existe_match_activo(self, id_usuario1, id_usuario2, id_tema):
        sql = """
        SELECT 1
        FROM MATCH
        WHERE LEAST(id_usuario1, id_usuario2) = LEAST(%s, %s)
          AND GREATEST(id_usuario1, id_usuario2) = GREATEST(%s, %s)
          AND id_tema = %s
          AND estado IN ('pendiente','aceptado')
        LIMIT 1;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario1, id_usuario2, id_usuario1, id_usuario2, id_tema))
                return cur.fetchone() is not None

    def actualizar_estado(self, id_match, nuevo_estado):
        sql = """
        UPDATE MATCH
        SET estado = %s
        WHERE id_match = %s;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nuevo_estado, id_match))
                conn.commit()
                return cur.rowcount > 0

    def obtener_matches_usuario(self, id_usuario):
        sql = """
        SELECT *
        FROM MATCH
        WHERE id_usuario1 = %s OR id_usuario2 = %s
        ORDER BY fecha_match DESC;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario, id_usuario))
                return cur.fetchall()
