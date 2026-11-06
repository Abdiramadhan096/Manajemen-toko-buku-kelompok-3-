
from config.database import Database


class BukuModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM buku"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_buku):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM buku WHERE ID_Buku = %s"
            cursor.execute(query, (id_buku,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data buku: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def search(self, keyword):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM buku
                WHERE Judul LIKE %s
                OR Penulis LIKE %s
                OR Penerbit LIKE %s
            """
            keyword = f"%{keyword}%"
            cursor.execute(query, (keyword, keyword, keyword))
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mencari buku: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_kategori, id_admin, judul, penulis,
               penerbit, harga_jual, stok):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO buku
                (ID_Kategori, ID_Admin, Judul, Penulis,
                 Penerbit, Harga_Jual, Stok)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                id_kategori, id_admin, judul, penulis,
                penerbit, harga_jual, stok
            )

            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan buku: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_buku, id_kategori, id_admin, judul,
               penulis, penerbit, harga_jual, stok):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE buku
                SET ID_Kategori = %s,
                    ID_Admin = %s,
                    Judul = %s,
                    Penulis = %s,
                    Penerbit = %s,
                    Harga_Jual = %s,
                    Stok = %s
                WHERE ID_Buku = %s
            """
            values = (
                id_kategori, id_admin, judul, penulis,
                penerbit, harga_jual, stok, id_buku
            )

            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui buku: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_buku):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = "DELETE FROM buku WHERE ID_Buku = %s"
            cursor.execute(query, (id_buku,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus buku: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
