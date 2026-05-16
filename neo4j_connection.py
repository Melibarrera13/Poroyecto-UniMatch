"""TemaDAO - Acceso a datos de la entidad TEMA (PostgreSQL)"""

from src.dao.postgres.postgres_connection import PostgresConnection


class TemaDAO:

    def crear_tema(self, nombre_estandar, area):
        sql = """
        INSERT INTO TEMA(nombre_estandar, area)
        VALUES (%s, %s)
        RETURNING id_tema;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre_estandar, area))
                row = cur.fetchone()
                conn.commit()
                return row["id_tema"]

    def obtener_por_id(self, id_tema):
        sql = """SELECT * FROM TEMA WHERE id_tema = %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_tema,))
                return cur.fetchone()

    def buscar_por_nombre(self, texto):
        sql = """
        SELECT * FROM TEMA
        WHERE LOWER(nombre_estandar) LIKE LOWER(%s)
        ORDER BY nombre_estandar;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (f"%{texto}%",))
                return cur.fetchall()

    def listar_temas(self):
        sql = """SELECT * FROM TEMA ORDER BY area, nombre_estandar;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
