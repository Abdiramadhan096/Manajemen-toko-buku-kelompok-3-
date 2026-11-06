
from config.database import Database


class PemilikModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM pemilik_toko"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data pemilik: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_pemilik):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM pemilik_toko
                WHERE ID_Pemilik = %s
            """
            cursor.execute(query, (id_pemilik,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data pemilik: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_akun, nama_pemilik):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO pemilik_toko (ID_Akun, Nama_Pemilik)
                VALUES (%s, %s)
            """
            cursor.execute(query, (id_akun, nama_pemilik))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan pemilik: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_pemilik, id_akun, nama_pemilik):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE pemilik_toko
                SET ID_Akun = %s,
                    Nama_Pemilik = %s
                WHERE ID_Pemilik = %s
            """
            cursor.execute(
                query, (id_akun, nama_pemilik, id_pemilik)
            )
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui data pemilik: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_pemilik):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM pemilik_toko
                WHERE ID_Pemilik = %s
            """
            cursor.execute(query, (id_pemilik,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus data pemilik: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
