# Template implementation.md

Checklist kerja, bukan ringkasan dan bukan kode. Nama file persis `implementation.md`.

```markdown
# Implementation — <Nama Proyek>

> **Progres** — terakhir selesai: — · berikutnya: TASK-001 · kode: `<path repo>` · stack: <dari PLAN.md>
> Sesi baru: jalankan `check_artifacts.py . --next`, baca hanya task itu dan bagian yang dirujuk.

Ref: [PRD](PRD.md) v1.0 · [PLAN](PLAN.md) v1.0 · [UI](UI.md) v1.0 · [Prototype](prototype/README.md) disetujui YYYY-MM-DD
Status: `- [ ]` belum · `- [x]` selesai + bukti · `⛔ BLOCKED` terhalang

## Setup
- [ ] **TASK-001 — Init proyek Next.js + TypeScript + linter** — Ref: PLAN §Stack · AC: `npm run dev` jalan, lint lulus · Verifikasi: `npm run lint && npm run build`.
- [ ] **TASK-002 — Tokens dan theme global** — Ref: PLAN §Desain, `prototype/assets/tokens.css` · Dep: TASK-001 · AC: nilai sama dengan tokens prototype · Verifikasi: build + cek visual 360/1280.

## Komponen
- [ ] **TASK-003 — COMP-002 Button + COMP-005 TextField dengan semua state** — Ref: COMP-002, COMP-005 · Dep: TASK-002 · AC: varian dan state sesuai UI.md dan `prototype/assets/components.css`, fokus terlihat · Verifikasi: unit test render + uji keyboard.
- [ ] **TASK-004 — COMP-001 Header, COMP-003 Card, COMP-004 Footer** — Ref: COMP-001, COMP-003, COMP-004 · Dep: TASK-002 · AC: sesuai UI.md, menu mobile buka/tutup · Verifikasi: test render 360/1280.

## Halaman
### SCR-001 — Beranda
- [ ] **TASK-005 — SCR-001: susun sesuai wireframe (hero, layanan, CTA)** — Ref: SCR-001, FR-001, [prototype](prototype/pages/scr-001-home.html) · Dep: TASK-003, TASK-004 · AC: AC FR-001 terpenuhi, tampilan cocok dengan prototype di 360/1280 · Verifikasi: test render + Lighthouse a11y ≥ 90.

### SCR-002 — Kontak
- [ ] **TASK-006 — SCR-002: form sesuai wireframe + validasi** — Ref: SCR-002, FR-002, [prototype](prototype/pages/scr-002-contact.html) · Dep: TASK-003 · AC: email invalid ditolak, sukses tampil konfirmasi · Verifikasi: unit test validasi.
- [ ] **TASK-007 — ⛔ BLOCKED: kirim email notifikasi (FR-003)** — Blocker: OQ-001 penyedia email.

## Kualitas dan rilis
- [ ] **TASK-008 — NFR-001 performa** — Verifikasi: Lighthouse LCP < 2.5 dtk.
- [ ] **TASK-009 — Deploy ke hosting + env variables** — Dep: semua task Must · Verifikasi: URL production dapat dibuka, form bekerja.

## Ringkasan
Task: 0 / 9 · Blocked: TASK-007 (OQ-001)
```

Aturan:
- Satu task = satu hasil yang bisa diverifikasi. Jangan buat task "implementasikan semua halaman".
- Komponen dibangun sebelum halaman; task halaman merujuk wireframe di UI.md dan file prototype-nya, memakai komponen, bukan membuat style sendiri.
- Prototype yang sudah ada **bukan** bukti task selesai; `[x]` hanya untuk kode aplikasi yang terverifikasi.
- `- [x]` hanya setelah verifikasi nyata, tulis buktinya di baris itu (misal `✔ npm test 12/12`).
- Angka ringkasan dari `check_artifacts.py`, bukan tebakan.
- ID task tidak dinomori ulang; task dihapus dicoret dengan alasan.
- Perbarui blok Progres setiap task selesai.
