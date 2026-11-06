
from config.database import Database


class TransaksiModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM transaksi ORDER BY Tanggal DESC"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data transaksi: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_transaksi):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM transaksi
                WHERE ID_Transaksi = %s
            """
            cursor.execute(query, (id_transaksi,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data transaksi: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_kasir, tanggal, total_harga,
               metode_pembayaran, jumlah_bayar, kembalian):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO transaksi
                (ID_Kasir, Tanggal, Total_Harga,
                 Metode_Pembayaran, Jumlah_Bayar, Kembalian)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                id_kasir, tanggal, total_harga,
                metode_pembayaran, jumlah_bayar, kembalian
            )
            cursor.execute(query, values)
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            print(f"Gagal menambahkan transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_transaksi, id_kasir, tanggal,
               total_harga, metode_pembayaran,
               jumlah_bayar, kembalian):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE transaksi
                SET ID_Kasir = %s,
                    Tanggal = %s,
                    Total_Harga = %s,
                    Metode_Pembayaran = %s,
                    Jumlah_Bayar = %s,
                    Kembalian = %s
                WHERE ID_Transaksi = %s
            """
            values = (
                id_kasir, tanggal, total_harga,
                metode_pembayaran, jumlah_bayar,
                kembalian, id_transaksi
            )
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_transaksi):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM transaksi
                WHERE ID_Transaksi = %s
            """
            cursor.execute(query, (id_transaksi,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus transaksi: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
