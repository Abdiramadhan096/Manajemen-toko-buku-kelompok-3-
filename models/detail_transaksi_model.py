
from config.database import Database


class DetailTransaksiModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM detail_transaksi"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil detail transaksi: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_detail):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM detail_transaksi
                WHERE ID_Detail = %s
            """
            cursor.execute(query, (id_detail,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil detail transaksi: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_transaksi(self, id_transaksi):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT dt.*, b.Judul
                FROM detail_transaksi dt
                JOIN buku b ON dt.ID_Buku = b.ID_Buku
                WHERE dt.ID_Transaksi = %s
            """
            cursor.execute(query, (id_transaksi,))
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil rincian transaksi: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_transaksi, id_buku, jumlah,
               harga_satuan, subtotal):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO detail_transaksi
                (ID_Transaksi, ID_Buku, Jumlah,
                 Harga_Satuan, Subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                id_transaksi, id_buku, jumlah,
                harga_satuan, subtotal
            )
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan detail transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_detail, id_transaksi, id_buku,
               jumlah, harga_satuan, subtotal):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE detail_transaksi
                SET ID_Transaksi = %s,
                    ID_Buku = %s,
                    Jumlah = %s,
                    Harga_Satuan = %s,
                    Subtotal = %s
                WHERE ID_Detail = %s
            """
            values = (
                id_transaksi, id_buku, jumlah,
                harga_satuan, subtotal, id_detail
            )
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui detail transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_detail):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM detail_transaksi
                WHERE ID_Detail = %s
            """
            cursor.execute(query, (id_detail,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus detail transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
