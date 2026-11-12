# Template PRD.md

Daftar periksa, bukan formulir. Hapus bagian yang tidak relevan. Website kecil cukup 1 halaman.

```markdown
# PRD — <Nama Proyek>

Versi 1.0 · YYYY-MM-DD · Status: menunggu persetujuan

## Masalah
<1–3 kalimat: masalah apa, untuk siapa, cara saat ini>

## Pengguna
- <Peran> — <kebutuhan utama>

## Tujuan
- <hasil yang diharapkan, sebisa mungkin terukur>

**Bukan tujuan versi ini:** <yang sengaja tidak dikerjakan>

## Fitur

| ID | Fitur | Prioritas | Butuh UI |
|----|-------|-----------|----------|
| FR-001 | Pengunjung melihat daftar layanan | Must | Ya |
| FR-002 | Pengunjung mengirim form kontak | Must | Ya |
| FR-003 | Admin menerima email notifikasi kontak | Should | Tidak |

### FR-001 — Daftar layanan
- AC: Given halaman Layanan dibuka, Then semua layanan aktif tampil dengan judul, deskripsi, harga.
- AC: Given tidak ada layanan, Then tampil pesan kosong yang jelas.

### FR-002 — Form kontak
- AC: Given nama, email valid, dan pesan terisi, When kirim, Then pesan tersimpan dan tampil konfirmasi.
- AC: Given email tidak valid, Then form menolak dengan pesan error di field email.

## Kebutuhan non-fungsional (hanya bila perlu)
| ID | Kebutuhan | Target | Cara cek |
|----|-----------|--------|----------|
| NFR-001 | Performa halaman utama | LCP < 2.5 dtk di 4G | Lighthouse |

## Batasan
<tenggat, hosting, budget, integrasi, bahasa>

## Asumsi dan pertanyaan terbuka
- [Asumsi] …
- OQ-001 — … (memblokir: FR-00x?)
```

Aturan singkat:
- AC konkret dan bisa diuji, termasuk satu kasus gagal yang penting.
- NFR punya angka atau cara cek, bukan "cepat"/"aman".
- Prioritas eksplisit; Must = wajib ada di versi pertama.
