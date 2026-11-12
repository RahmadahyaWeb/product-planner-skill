# Template PLAN.md

Satu file untuk halaman, desain, stack, dan status. Hapus bagian yang tidak relevan.

```markdown
# PLAN — <Nama Proyek>

Versi 1.0 · YYYY-MM-DD

## Status
| Tahap | Status | Tanggal |
|-------|--------|---------|
| PRD | disetujui | YYYY-MM-DD |
| PLAN | menunggu persetujuan | |
| UI (wireframe + komponen) | belum | |
| Prototype | belum | |
| Implementasi | belum | |

Keputusan: <tanggal> — <keputusan> (sumber: pengguna / rekomendasi disetujui)
Langkah berikutnya: …

## Halaman

<N> halaman, karena: <alur/fitur yang menuntutnya>.

| ID | Halaman | Route | FR | Isi utama | State penting |
|----|---------|-------|----|-----------|---------------|
| SCR-001 | Beranda | `/` | FR-001 | hero, ringkasan layanan, CTA kontak | — |
| SCR-002 | Kontak | `/contact` | FR-002 | form nama/email/pesan | error validasi, sukses, gagal kirim |

Navigasi: header (Beranda, Layanan, Kontak) · footer.
Modal/overlay: <bila ada, sebut induk SCR-nya>.
Ditunda: <halaman yang tidak masuk versi ini>.

## Desain
Arah visual: <2–3 kalimat: kesan, referensi, mobile-first?>

Tokens (sumber kebenaran; di kode jadi CSS variables / theme config):
| Token | Nilai |
|-------|-------|
| color-primary | #1D4ED8 |
| color-text | #111827 |
| color-bg | #FFFFFF |
| font-body | Inter, sans-serif |
| space-unit | 4px |
| radius | 8px |

Breakpoint: 360 / 768 / 1280. Aksesibilitas: WCAG 2.2 AA [Rekomendasi]; kontras primary vs bg: 4.5:1 ✔.
Komponen dan wireframe: lihat [UI.md](UI.md).

## Stack
| Bagian | Pilihan | Versi (dicek Context7) | Alasan |
|--------|---------|------------------------|--------|
| Framework | Next.js | 15.x | SSG + form API route |
| Styling | Tailwind CSS | 4.x | tokens via theme |
| Hosting | Vercel | — | gratis untuk skala ini |

Konvensi: kode in English, struktur folder mengikuti docs framework, linter/formatter: <…>.
```

Aturan singkat:
- Jumlah halaman dari alur, bukan dari jumlah fitur. Satu halaman boleh memenuhi beberapa FR.
- Setiap FR yang `Butuh UI: Ya` muncul di kolom FR minimal satu halaman.
- Stack yang belum dikonfirmasi pengguna ditandai [Rekomendasi].
