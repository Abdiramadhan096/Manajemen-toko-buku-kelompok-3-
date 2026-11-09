# Sistem Informasi Manajemen Toko Buku
Tugas Besar Project UAS Rekayasa Perangkat Lunak (RPL) - Kelas SI A

## Anggota Kelompok 4
1. Moh. Abdi Ramadhan (F5212510001)
2. Andi Nayla Sava Arrahmah P (F5212510005)
3. Adelia Mutmaina (F5212510012)
4. Shafairunizar Neirabista E (F5212510018)
5. Rendra Akbar Fauzi (F5212510024)
6. Meuthia Sari Rusdy (F5212510027)
7. Nailah Afifah (F5212520034)

---

## Studi Kasus & Deskripsi Sistem
Aplikasi Sistem Informasi Manajemen Toko Buku berbasis desktop yang dibangun menggunakan Python (CustomTkinter) dengan arsitektur Model-View-Controller (MVC) dan basis data MySQL.

Sistem ini membantu operasional toko buku sehari-hari, mulai dari pengelolaan katalog buku, transaksi penjualan kasir, pencatatan pasokan supplier, pencetakan struk transaksi, hingga laporan penjualan.

### Fitur Utama
- **Autentikasi & Hak Akses:** Login multi-peran (Admin dan Kasir).
- **Manajemen Buku:** Tambah, ubah, hapus, dan cari data buku beserta kategorinya.
- **Transaksi Kasir:** Pembuatan transaksi penjualan, keranjang belanja, hitung kembalian, dan cetak bukti transaksi.
- **Manajemen Supplier:** Pengelolaan data supplier dan pencatatan riwayat pasokan stok.
- **Laporan Penjualan:** Rekapitulasi transaksi dan pendapatan toko.

---

## Struktur Folder (MVC)
```text
├── config/             # Konfigurasi koneksi database
├── controllers/        # Logika alur proses & penghubung model-view
├── database/           # File skema database SQL (tokobuku.sql)
├── models/             # Query database (CRUD)
├── tests/              # Skrip pengujian otomatis (pytest)
├── views/              # Tampilan antarmuka (CustomTkinter)
├── .github/workflows/  # Konfigurasi CI Pipeline (GitHub Actions)
├── main.py             # File utama untuk menjalankan aplikasi
└── requirements.txt    # Daftar dependensi modul Python
```

---

## Cara Menjalankan Aplikasi

### 1. Prasyarat
- Python 3.10+
- Laragon / MySQL Server aktif

### 2. Setup Database
1. Pastikan MySQL di Laragon sudah berjalan.
2. Buat database baru bernama `toko_buku` (atau sesuaikan di `config/database.py`).
3. Import file database yang ada di folder `database/tokobuku.sql`.

### 3. Instalasi Dependensi
Buka terminal di direktori proyek dan jalankan:
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
python main.py
```

### 5. Menjalankan Pengujian (Unit Test)
```bash
pytest
```
