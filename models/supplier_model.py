
from config.database import Database


class SupplierModel:

    def get_all(self):
        conn = Database().get_connection()
        if conn is None:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM supplier"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Gagal mengambil data supplier: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def get_by_id(self, id_supplier):
        conn = Database().get_connection()
        if conn is None:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT * FROM supplier
                WHERE ID_Supplier = %s
            """
            cursor.execute(query, (id_supplier,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal mengambil data supplier: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def create(self, id_admin, nama_supplier, alamat, no_telepon):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO supplier
                (ID_Admin, Nama_Supplier, Alamat, No_Telepon)
                VALUES (%s, %s, %s, %s)
            """
            values = (id_admin, nama_supplier, alamat, no_telepon)
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menambahkan supplier: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def update(self, id_supplier, id_admin, nama_supplier,
               alamat, no_telepon):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                UPDATE supplier
                SET ID_Admin = %s,
                    Nama_Supplier = %s,
                    Alamat = %s,
                    No_Telepon = %s
                WHERE ID_Supplier = %s
            """
            values = (
                id_admin, nama_supplier, alamat,
                no_telepon, id_supplier
            )
            cursor.execute(query, values)
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal memperbarui supplier: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()

    def delete(self, id_supplier):
        conn = Database().get_connection()
        if conn is None:
            return False

        cursor = None
        try:
            cursor = conn.cursor()
            query = """
                DELETE FROM supplier
                WHERE ID_Supplier = %s
            """
            cursor.execute(query, (id_supplier,))
            conn.commit()
            return True

        except Exception as e:
            print(f"Gagal menghapus supplier: {e}")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            conn.close()
