"""UsuarioDAO - Acceso a datos de la entidad USUARIO (PostgreSQL)"""

from src.dao.postgres.postgres_connection import PostgresConnection


class UsuarioDAO:

    def crear_usuario(self, nombre, email, contrasena_hash, pais, idioma, id_universidad):
        sql = """
        INSERT INTO USUARIO(nombre, email, contrasena_hash, pais, idioma, id_universidad)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_usuario;
        """

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nombre, email, contrasena_hash, pais, idioma, id_universidad))
                row = cur.fetchone()
                conn.commit()
                return row["id_usuario"]

    def obtener_por_id(self, id_usuario):
        sql = """SELECT * FROM USUARIO WHERE id_usuario = %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario,))
                return cur.fetchone()

    def obtener_por_email(self, email):
        sql = """SELECT * FROM USUARIO WHERE email = %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (email,))
                return cur.fetchone()

    def listar_usuarios(self, limit=50):
        sql = """SELECT * FROM USUARIO ORDER BY id_usuario ASC LIMIT %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit,))
                return cur.fetchall()

    def eliminar_usuario(self, id_usuario):
        sql = """DELETE FROM USUARIO WHERE id_usuario = %s;"""

        with PostgresConnection.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id_usuario,))
                conn.commit()
                return cur.rowcount > 0
