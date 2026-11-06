
from config.database import Database


class AdminModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM admin"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data admin: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_admin):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM admin WHERE ID_Admin = %s"
            cursor.execute(query, (id_admin,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data admin: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_akun, nama_admin):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO admin (ID_Akun, Nama_Admin)
                VALUES (%s, %s)
            """
            cursor.execute(query, (id_akun, nama_admin))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan admin: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_admin, id_akun, nama_admin):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE admin
                SET ID_Akun = %s,
                    Nama_Admin = %s
                WHERE ID_Admin = %s
            """
            cursor.execute(
                query, (id_akun, nama_admin, id_admin)
            )
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui admin: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_admin):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = "DELETE FROM admin WHERE ID_Admin = %s"
            cursor.execute(query, (id_admin,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus admin: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
