# Template prototype/

Prototype HTML/CSS/JS statis semua halaman. Dibuat setelah UI.md disetujui, disetujui sebelum implementation.md.

## Struktur

```
prototype/
├── index.html              # daftar halaman + tautan (hub)
├── README.md
├── assets/
│   ├── tokens.css          # CSS variables dari PLAN.md (satu sumber nilai)
│   ├── components.css      # satu blok kelas per COMP-xxx, hanya pakai var(--…)
│   ├── app.js              # interaksi bersama (menu, modal, validasi demo)
│   └── mock-data.js        # data contoh, ditandai MOCK
└── pages/
    ├── scr-001-home.html
    └── scr-002-contact.html
```

## Aturan

- Nama file halaman `scr-xxx-<slug>.html`. Baris pertama setelah `<!doctype html>`:
  `<!-- SCR-002 Contact + SCR-002a Success modal | FR-002 -->`
  (bagian sebelum `|` = SCR yang dicakup file ini; dibaca `check_artifacts.py`).
- Setiap halaman memuat `tokens.css` lalu `components.css`. Tidak ada `style=""` atau nilai warna/spacing/font di luar tokens.
- Kelas komponen diberi komentar ID: `/* COMP-002 Button */ .btn, .btn--primary, .btn:disabled …`.
- Susunan section persis mengikuti wireframe UI.md; mobile-first, cek di 360 dan 1280.
- Navigasi alur utama nyata (tautan antarhalaman). Aksi yang butuh backend disimulasikan di `app.js` dan ditandai `// MOCK`.
- State penting bisa dicoba: misal submit form kosong → error; parameter `?state=empty` untuk tampilan kosong.
- HTML semantik dan aksesibel: `<label>` untuk input, `alt`, fokus terlihat, landmark (`header`, `main`, `nav`, `footer`).
- Nama kelas, file, id, dan komentar dalam bahasa Inggris; teks tampilan mengikuti bahasa produk.

## README.md

```markdown
# Prototype — <Nama Proyek>

Buka: `prototype/index.html` di browser (tanpa server).

| SCR | Halaman | File | Status |
|-----|---------|------|--------|
| SCR-001 | Beranda | [pages/scr-001-home.html](pages/scr-001-home.html) | selesai |

Bisa dicoba: alur kontak (kirim kosong → error, isi benar → sukses), `?state=empty` di Beranda.
Disimulasikan (MOCK): pengiriman form, data layanan.
Keterbatasan: tanpa backend, tanpa autentikasi nyata.
```

## Verifikasi sebelum minta persetujuan

1. `check_artifacts.py <folder>` → "SCR tanpa file prototype: tidak ada".
2. Semua tautan antarhalaman dan dari `index.html` berfungsi.
3. `grep -nE '#[0-9a-fA-F]{3,6}|[0-9]+px' prototype/pages prototype/assets/components.css` → tidak ada nilai di luar tokens (kecuali yang memang sengaja, sebutkan).
4. Buka di browser bila tersedia; jika tidak, katakan bahwa tampilan belum dicek visual.
