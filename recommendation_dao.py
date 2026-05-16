"""HorarioDAO - Acceso a datos de la entidad HORARIO_DISPONIBLE (PostgreSQL)"""

from src.dao.postgres.postgres_connection import PostgresConnection


class HorarioDAO:

    def crear_horario(self, dia, hora_inicio, hora_fin, zona_horaria, id_usuario):
        sql = """
        INSERT INTO HORARIO_DISPONIBLE(dia, hora_inicio, hora_fin, zona_horaria, id_usuario)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_horario;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (dia, hora_inicio, hora_fin, zona_horaria, id_usuario))
                row = cur.fetchone()
                conn.commit()
                return row["id_horario"]

    def listar_horarios_usuario(self, id_usuario):
        sql = """
        SELECT dia, hora_inicio, hora_fin, zona_horaria
        FROM HORARIO_DISPONIBLE
        WHERE id_usuario = %s
        ORDER BY dia, hora_inicio;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario,))
                return cur.fetchall()

    def eliminar_horario(self, id_horario):
        sql = """DELETE FROM HORARIO_DISPONIBLE WHERE id_horario = %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_horario,))
                conn.commit()
                return cur.rowcount > 0
