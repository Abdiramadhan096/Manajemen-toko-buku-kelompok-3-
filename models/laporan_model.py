
from config.database import Database


class LaporanModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM laporan
                ORDER BY Tanggal_Dibuat DESC
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data laporan: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_laporan):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM laporan
                WHERE ID_Laporan = %s
            """
            cursor.execute(query, (id_laporan,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil laporan: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_jenis(self, jenis_laporan):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM laporan
                WHERE Jenis_Laporan = %s
                ORDER BY Tanggal_Dibuat DESC
            """
            cursor.execute(query, (jenis_laporan,))
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mencari jenis laporan: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_pemilik, id_transaksi, id_buku,
               jenis_laporan, tanggal_awal, tanggal_akhir):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO laporan
                (ID_Pemilik, ID_Transaksi, ID_Buku,
                 Jenis_Laporan, Tanggal_Awal, Tanggal_Akhir)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                id_pemilik, id_transaksi, id_buku,
                jenis_laporan, tanggal_awal, tanggal_akhir
            )
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal membuat laporan: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_laporan):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM laporan
                WHERE ID_Laporan = %s
            """
            cursor.execute(query, (id_laporan,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus laporan: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
