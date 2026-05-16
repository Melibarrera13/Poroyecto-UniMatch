"""MensajeDAO - Acceso a datos de la entidad MENSAJE (PostgreSQL)"""

from src.dao.postgres.postgres_connection import PostgresConnection


class MensajeDAO:

    def enviar_mensaje(self, id_match, id_emisor, contenido):
        sql = """
        INSERT INTO MENSAJE(id_match, id_emisor, contenido)
        VALUES (%s, %s, %s)
        RETURNING id_mensaje;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_match, id_emisor, contenido))
                row = cur.fetchone()
                conn.commit()
                return row["id_mensaje"]

    def listar_mensajes_match(self, id_match):
        sql = """
        SELECT m.id_mensaje, m.contenido, m.fecha_hora, m.leido, u.nombre AS emisor
        FROM MENSAJE m
        JOIN USUARIO u ON u.id_usuario = m.id_emisor
        WHERE m.id_match = %s
        ORDER BY m.fecha_hora ASC;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_match,))
                return cur.fetchall()

    def marcar_leido(self, id_mensaje):
        sql = """
        UPDATE MENSAJE
        SET leido = TRUE
        WHERE id_mensaje = %s;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_mensaje,))
                conn.commit()
                return cur.rowcount > 0
