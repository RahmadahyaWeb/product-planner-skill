# Template UI.md

Alur, wireframe, dan komponen. Dibuat setelah PLAN.md disetujui, disetujui sebelum prototype dibuat.

```markdown
# UI — <Nama Proyek>

Versi 1.0 · YYYY-MM-DD · Status: menunggu persetujuan
Tokens dan daftar halaman: lihat [PLAN.md](PLAN.md).

## Alur utama
- **Hubungi bisnis (FR-001, FR-002):** SCR-001 Beranda → klik "Hubungi kami" → SCR-002 Kontak → isi form → kirim → pesan sukses.
  Gagal: email invalid → error di field, data tetap terisi.

## Wireframe

### SCR-001 — Beranda (`/`)
Mobile 360:
┌──────────────────────────┐
│ [Logo]          [☰ Menu] │  COMP-001 Header
├──────────────────────────┤
│ Judul besar (H1)         │  Hero
│ Subjudul 1–2 baris       │
│ [ Hubungi kami ]         │  COMP-002 Button primary → SCR-002
├──────────────────────────┤
│ ┌──────────┐             │  Layanan: COMP-003 Card × n
│ │ Judul    │ (stack 1    │
│ │ Deskripsi│  kolom)     │
│ └──────────┘             │
├──────────────────────────┤
│ Footer: kontak · sosmed  │  COMP-004 Footer
└──────────────────────────┘
Desktop 1280: kartu layanan 3 kolom; menu tampil di header (tanpa ☰).
State: tidak ada layanan → teks "Layanan segera hadir".

### SCR-002 — Kontak (`/contact`)
…

## Komponen

| ID | Komponen | Varian | State | Tokens | Dipakai di |
|----|----------|--------|-------|--------|------------|
| COMP-001 | Header | — | menu terbuka/tertutup (mobile) | color-bg, space | SCR-001, SCR-002 |
| COMP-002 | Button | primary, secondary | default, hover, focus, disabled, loading | color-primary, radius | SCR-001, SCR-002 |
| COMP-003 | Card | — | default, hover | radius, space | SCR-001 |
| COMP-004 | Footer | — | — | color-text | semua |
| COMP-005 | TextField | text, email, textarea | default, focus, error, disabled | color-text, radius | SCR-002 |

Aksesibilitas komponen: fokus terlihat, label untuk setiap input, target sentuh ≥ 44px.
Library UI (bila ada): <nama, versi dicek Context7> — COMP-002 → `Button`, COMP-005 → `Input`/`Textarea`.
```

Aturan singkat:
- Wireframe = struktur dan urutan, bukan desain final. Tanpa warna; cukup kotak, label, dan aksi.
- Setiap aksi penting menyebut tujuan navigasinya (`→ SCR-xxx`).
- Komponen hanya yang benar-benar muncul di wireframe. Komponen dipakai ulang, bukan dibuat ulang per halaman.
- Modal/overlay digambar di bawah wireframe halaman induknya.
