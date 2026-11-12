# UI — KasirKu

Versi 1.0 · Status: disetujui

## Wireframe
### SCR-001 — Login
Tujuan: masuk. Aksi utama: Kirim OTP / Masuk. State: OTP salah, terkunci. Komponen: COMP-001, COMP-002. Breakpoint: 360, 768.

### SCR-002 — Kasir
Tujuan: catat penjualan. Data: grid produk aktif (nama, harga, stok), keranjang. Validasi: jumlah ≤ stok (BR-001). State: stok kurang, keranjang kosong. Komponen: COMP-001, COMP-003, COMP-004, COMP-005, COMP-006, COMP-007, COMP-009. NFR-001, NFR-003.

### SCR-002a — Modal Bayar
Input uang diterima, kembalian dihitung, Simpan. Validasi: uang ≥ total. Komponen: COMP-005, COMP-002, COMP-001.

### SCR-003 — Produk
Tujuan: kelola produk. Daftar produk + form tambah/ubah, nonaktifkan dengan konfirmasi. State: permission-denied untuk Kasir, error validasi. Komponen: COMP-001, COMP-002, COMP-007, COMP-009.

### SCR-004 — Laporan Harian
Tujuan: tutup buku. StatCard total, jumlah transaksi, 3 terlaris. State: empty. Komponen: COMP-008, COMP-009.


## Komponen

| ID | Komponen | Dipakai di |
|----|----------|------------|
| COMP-001 | Button (primary, secondary, danger) | semua aksi |
| COMP-002 | TextField (label, help, error) | FR-001, FR-004 |
| COMP-003 | ProductTile | FR-002 |
| COMP-004 | CartBar (total + Bayar, sticky bawah) | FR-002, FR-003 |
| COMP-005 | Modal | FR-002 bayar |
| COMP-006 | Toast | feedback simpan |
| COMP-007 | Banner (error/info) | FR-003, AC-006 |
| COMP-008 | StatCard | FR-005 |
| COMP-009 | BottomNav (per peran) | navigasi |
