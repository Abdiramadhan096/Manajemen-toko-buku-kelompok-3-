
from config.database import Database


class KasirModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM kasir"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data kasir: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_kasir):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM kasir WHERE ID_Kasir = %s"
            cursor.execute(query, (id_kasir,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data kasir: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_akun, nama_kasir):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO kasir (ID_Akun, Nama_Kasir)
                VALUES (%s, %s)
            """
            cursor.execute(query, (id_akun, nama_kasir))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan kasir: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_kasir, id_akun, nama_kasir):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE kasir
                SET ID_Akun = %s,
                    Nama_Kasir = %s
                WHERE ID_Kasir = %s
            """
            cursor.execute(
                query, (id_akun, nama_kasir, id_kasir)
            )
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui kasir: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_kasir):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = "DELETE FROM kasir WHERE ID_Kasir = %s"
            cursor.execute(query, (id_kasir,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus kasir: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
