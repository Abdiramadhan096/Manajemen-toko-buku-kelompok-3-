
from config.database import Database


class KategoriModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM kategori"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data kategori: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_kategori):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM kategori
                WHERE ID_Kategori = %s
            """
            cursor.execute(query, (id_kategori,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data kategori: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, nama_kategori):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO kategori (Nama_Kategori)
                VALUES (%s)
            """
            cursor.execute(query, (nama_kategori,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan kategori: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_kategori, nama_kategori):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE kategori
                SET Nama_Kategori = %s
                WHERE ID_Kategori = %s
            """
            cursor.execute(query, (nama_kategori, id_kategori))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui kategori: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_kategori):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM kategori
                WHERE ID_Kategori = %s
            """
            cursor.execute(query, (id_kategori,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus kategori: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
