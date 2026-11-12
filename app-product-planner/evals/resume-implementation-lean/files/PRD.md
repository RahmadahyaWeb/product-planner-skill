# PRD — KasirKu

| Versi | Tanggal | Status | Penulis |
|-------|---------|--------|---------|
| 1.0 | 2026-10-01 | Disetujui (2026-10-03) | Tim produk |

**Riwayat perubahan**
| Versi | Tanggal | Perubahan | ID terdampak |
|-------|---------|-----------|--------------|
| 1.0 | 2026-10-01 | Versi awal | semua |

Legenda label: [Fakta] [Keputusan] [Rekomendasi] [Asumsi] [OQ-xxx]

## 1. Ringkasan produk
KasirKu adalah aplikasi kasir web (mobile-first) untuk warung kopi kecil dengan 1 pemilik dan 1–3 kasir, menggantikan pencatatan di buku tulis.

## 2. Masalah
[Fakta] Pemilik mencatat penjualan di buku; stok sering selisih dan laporan harian butuh 30 menit dihitung manual setiap malam.

## 3. Pengguna
| Persona | Peran | Konteks |
|---------|-------|---------|
| Bu Rina | Pemilik | Mengelola produk, melihat laporan dari HP |
| Dimas | Kasir | Mencatat penjualan saat antrean ramai, satu tangan |

## 4. Tujuan dan metrik
| ID | Tujuan | Metrik | Baseline | Target |
|----|--------|--------|----------|--------|
| G-1 | Pencatatan penjualan cepat | Waktu catat 1 transaksi | ~60 dtk (buku) | < 20 dtk |
| G-2 | Laporan harian otomatis | Waktu tutup buku | 30 menit | < 2 menit |

**Non-tujuan:** akuntansi lengkap, multi-cabang, pembayaran QRIS terintegrasi (fase 2).

## 5. Ruang lingkup MVP
Login, catat penjualan, kelola produk & stok, laporan harian, backup otomatis.

## 8. User stories
| ID | Sebagai | Saya ingin | Sehingga | Tujuan |
|----|---------|-----------|----------|--------|
| US-001 | Pengguna | masuk dengan nomor HP | akun aman tanpa password | G-1 |
| US-002 | Kasir | mencatat penjualan dari daftar produk | transaksi cepat | G-1 |
| US-003 | Pemilik | menambah/mengubah produk dan stok | daftar produk akurat | G-1 |
| US-004 | Pemilik | melihat laporan penjualan harian | tutup buku cepat | G-2 |

## 9. Functional requirements
| ID | Requirement | US/Tujuan | Butuh UI? | Prioritas | AC |
|----|-------------|-----------|-----------|-----------|----|
| FR-001 | Login dengan nomor HP + OTP (disimulasikan di MVP) | US-001 | Ya | Must | AC-001, AC-002 |
| FR-002 | Kasir memilih produk, mengatur jumlah, dan menyimpan transaksi tunai | US-002 | Ya | Must | AC-003 |
| FR-003 | Transaksi ditolak jika jumlah melebihi stok | US-002 | Ya | Must | AC-004 |
| FR-004 | Pemilik menambah, mengubah, dan menonaktifkan produk serta stok | US-003 | Ya | Must | AC-005, AC-006 |
| FR-005 | Pemilik melihat laporan penjualan harian (total, jumlah transaksi, produk terlaris) | US-004 | Ya | Must | AC-007 |
| FR-006 | Sistem membuat backup data otomatis setiap hari pukul 23.00 | G-2 | Tidak | Should | AC-008 |

## 10. Acceptance criteria
- **AC-001 (FR-001)** Given nomor HP terdaftar, When OTP benar dimasukkan, Then pengguna masuk ke halaman sesuai peran (Kasir → Kasir, Pemilik → Laporan).
- **AC-002 (FR-001, failure)** Given OTP salah 3 kali, Then input dikunci 5 menit dengan pesan jelas.
- **AC-003 (FR-002)** Given keranjang berisi 2 Kopi Susu (Rp18.000), When kasir menekan Bayar lalu Simpan dengan uang Rp50.000, Then transaksi tersimpan, kembalian Rp32.000 tampil, stok berkurang 2.
- **AC-004 (FR-003, failure)** Given stok Kopi Susu = 1, When kasir menambah jumlah menjadi 2, Then tombol Bayar nonaktif dan pesan "Stok Kopi Susu tersisa 1" tampil.
- **AC-005 (FR-004)** Given Pemilik di halaman Produk, When menambah produk dengan nama, harga, stok valid, Then produk muncul di halaman Kasir.
- **AC-006 (FR-004, izin)** Given pengguna berperan Kasir, When membuka /produk, Then akses ditolak dengan pesan dan tautan kembali ke Kasir.
- **AC-007 (FR-005)** Given ada 12 transaksi hari ini, When Pemilik membuka Laporan, Then total, jumlah transaksi, dan 3 produk terlaris tampil.
- **AC-008 (FR-006)** Given pukul 23.00, Then backup dibuat dan gagal backup tercatat di log.

## 11. Non-functional requirements
| ID | Kategori | Requirement | Target | Verifikasi |
|----|----------|-------------|--------|------------|
| NFR-001 | Performance | Halaman Kasir siap dipakai | < 2 dtk p95, Android menengah, 4G | Lighthouse |
| NFR-002 | Aksesibilitas | Semua halaman MVP | WCAG 2.2 AA | axe + uji keyboard |
| NFR-003 | Usability | Target sentuh | ≥ 44×44 px | design QA |

## 12. Business rules
| ID | Aturan |
|----|--------|
| BR-001 | Stok tidak boleh negatif |
| BR-002 | Hanya Pemilik yang dapat mengelola produk dan melihat laporan |

## 13. Hak akses
| Kemampuan | Pemilik | Kasir |
|-----------|---------|-------|
| Catat penjualan | Ya | Ya |
| Kelola produk | Ya | Tidak |
| Laporan | Ya | Tidak |

## 16. Analytics
| Event | Pemicu | Tujuan |
|-------|--------|--------|
| sale_completed | Transaksi tersimpan | G-1 |
| report_viewed | Laporan dibuka | G-2 |

## 17. Risiko
| ID | Risiko | Mitigasi |
|----|--------|----------|
| RISK-001 | Kasir enggan beralih dari buku | Alur catat < 20 dtk, pelatihan 10 menit |

## 18. Open questions
| ID | Pertanyaan | Rekomendasi default |
|----|-----------|---------------------|
| OQ-001 | Penyedia OTP (WhatsApp vs SMS)? | WhatsApp — diputuskan sebelum implementasi |
