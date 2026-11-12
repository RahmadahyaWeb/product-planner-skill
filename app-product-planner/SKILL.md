---
name: app-product-planner
description: Merencanakan dan mengerjakan website/aplikasi sederhana dengan alur ringkas - interview singkat, PRD.md, PLAN.md (halaman, desain, stack), UI.md (user flow, wireframe, komponen), prototype HTML semua halaman, implementation.md (checklist TASK-xxx), lalu eksekusi task satu per satu. Gunakan saat pengguna punya ide website/aplikasi ("mau bikin website...", "I have an app idea"), meminta PRD, requirement, daftar halaman, sitemap, wireframe, komponen UI, prototype, rencana desain, pilihan stack, atau checklist implementasi; juga untuk memperbarui rencana atau melanjutkan sesi ("lanjutkan implementasi dari implementation.md"). Saat implementasi wajib cek dokumentasi library lewat MCP Context7 dan menulis kode dalam bahasa Inggris dengan best practices. Bukan untuk bug fix atau coding di luar implementation.md, desain grafis murni, atau pertanyaan UI/UX kecil.
---

# App Product Planner (ringkas)

Ubah ide website/aplikasi jadi rencana pendek yang langsung bisa dikerjakan, lalu kerjakan task-nya.

| File | Isi |
|------|-----|
| `PRD.md` | Masalah, pengguna, scope, fitur `FR-xxx` + acceptance criteria |
| `PLAN.md` | Halaman `SCR-xxx`, arah desain + tokens, stack (dicek via Context7), status |
| `UI.md` | Alur utama, wireframe tiap `SCR-xxx`, komponen `COMP-xxx` |
| `prototype/` | Prototype HTML/CSS/JS statis semua halaman + `README.md` |
| `implementation.md` | Blok Progres + checklist `TASK-xxx` |

Balas dalam bahasa pengguna. Dokumen perencanaan ditulis dalam bahasa pengguna. **Kode selalu dalam bahasa Inggris** (lihat "Aturan kode").

## Alur

```
Interview (1–2 ronde) → PRD.md ⛔ → PLAN.md ⛔ → UI.md ⛔ → prototype/ ⛔ → implementation.md → kerjakan task
```

⛔ = berhenti, tunjukkan hasil, minta persetujuan. Persetujuan PRD bukan persetujuan PLAN. Jika pengguna bilang tahap sudah disetujui, catat di `PLAN.md` dan lanjut. Untuk proyek yang sangat kecil (1–3 halaman), PLAN dan UI boleh disajikan dalam satu putaran dengan dua persetujuan terpisah. Wireframe, komponen, dan prototype **wajib** disetujui berurutan sebelum implementation.md dibuat dan sebelum kode aplikasi ditulis.

## Titik mulai

Cek dulu file yang ada di folder kerja.

- **Lanjut implementasi** ("lanjutkan implementasi", "kerjakan task berikutnya") → mode hemat:
  1. Jalankan `python3 /path/absolut/ke/app-product-planner/scripts/check_artifacts.py <folder> --next` (atau `--next 3`). Jangan Read `implementation.md` penuh.
  2. Read hanya pointer `file:line` dari output (offset/limit ±30 baris). Bagian Stack di `PLAN.md` wireframe di `UI.md`, dan file prototype halaman yang dikerjakan boleh dibaca.
  3. Jangan baca `references/*.md` atau PRD/PLAN/UI penuh. Jangan interview.
  4. Kerjakan task sesuai "Aturan kode".
- **Ada PRD/PLAN/UI/prototype, belum selesai** → baca bagian Status di `PLAN.md` (atau PRD), ringkas posisi, lanjut dari tahap itu.
- **Belum ada file** → interview. Jangan buat file di respons pertama, meski diminta langsung.
- **Pengguna bawa dokumen sendiri** → pakai sebagai input, tandai yang kurang.

## Prinsip

- **Proporsional.** Website 3 halaman cukup PRD 1 halaman. Hapus bagian template yang tidak relevan.
- **Jangan mengarang.** Yang belum pasti ditandai **[Asumsi]**, usulanmu **[Rekomendasi]** (dengan alasan singkat), pertanyaan terbuka `OQ-xxx`.
- Kalau pengguna tidak tahu, beri 2–3 opsi + rekomendasi.
- Fitur atau halaman yang tidak diminta = **[Rekomendasi]**, bukan scope diam-diam.
- **ID stabil:** `FR-001`, `NFR-001` (hanya bila perlu), `SCR-001`, `COMP-001`, `TASK-001`, `OQ-001`. Tidak dinomori ulang; yang dihapus dicoret `~~FR-004~~ (dihapus: alasan)`.
- Jangan klaim selesai jika belum.

## 1. Interview

Sapa singkat, jelaskan alur dalam satu baris, ajukan **3–5 pertanyaan** per ronde. Biasanya 1–2 ronde cukup.

- Ronde 1: masalah, siapa penggunanya, tujuan/hasil yang diharapkan, fitur wajib versi awal.
- Ronde 2 (bila perlu): peran/login, konten dan data, batasan (tenggat, hosting, integrasi), arah visual, stack bila sudah ada.
- Jika pengguna sudah memberi banyak konteks, ringkas yang kamu tangkap (2–4 butir) dan tanya hanya yang kurang. Jangan tanya ulang.
- Gali jawaban umum ("harus cepat" → halaman mana, berapa detik?).

## 2. PRD.md ⛔

Ikuti [references/prd-template.md](references/prd-template.md). Setiap `FR` punya prioritas (Must/Should/Could) dan 1–3 acceptance criteria yang bisa diuji. Tandai FR tanpa UI (`Butuh UI: Tidak`). Tunjukkan, sorot asumsi/OQ berisiko, minta persetujuan scope.

## 3. PLAN.md ⛔

Ikuti [references/plan-template.md](references/plan-template.md). Isinya:

- **Halaman:** daftar `SCR-xxx` (tujuan, route, FR terkait, isi utama, state penting). Jumlah halaman diturunkan dari fitur dan alur, beri alasannya.
- **Desain:** arah visual singkat + tokens (warna, font, spacing, radius). Target aksesibilitas default WCAG 2.2 AA [Rekomendasi].
- **Stack:** usulan framework/library. **Wajib cek lewat Context7** (lihat "Context7") untuk versi terbaru dan cara pakai yang direkomendasikan; tulis versi yang dicek.
- **Status:** gate PRD/PLAN/UI/Prototype/Implementasi + keputusan penting.

## 4. UI.md — alur, wireframe, komponen ⛔

Ikuti [references/ui-template.md](references/ui-template.md). Dibuat setelah PLAN disetujui.

- **Alur utama:** 1–3 alur penting dari FR (langkah per halaman, termasuk jalur gagal yang penting).
- **Wireframe tiap `SCR-xxx`:** ASCII low-fidelity, urutan section dari atas ke bawah, elemen dan aksi utama, tandai `COMP-xxx` yang dipakai. Mobile wajib; desktop hanya jika layout berbeda. State penting (kosong/error/sukses) cukup catatan di bawah wireframe.
- **Komponen `COMP-xxx`:** diturunkan dari wireframe (bukan library generik): nama, varian, state (default/hover/focus/disabled/error/loading bila relevan), tokens yang dipakai, dipakai di SCR mana. Jika proyek memakai library UI (misal shadcn/ui), cek via Context7 dan petakan COMP ke komponen library.
- Setiap SCR punya wireframe; setiap COMP dipakai minimal satu SCR. Cek dengan `check_artifacts.py`.

Tunjukkan wireframe dan daftar komponen, minta persetujuan. Revisi wireframe di sini jauh lebih murah daripada setelah kode ditulis.

## 5. Prototype HTML ⛔

Ikuti [references/prototype-template.md](references/prototype-template.md). Dibuat setelah UI.md disetujui; wajib untuk setiap proyek.

- HTML/CSS/JS statis tanpa build step (kecuali pengguna minta format lain, misal framework proyek). Bisa dibuka langsung di browser.
- **Semua** `SCR-xxx` yang disetujui, satu file per halaman, mengikuti wireframe UI.md.
- Satu file tokens (`assets/tokens.css`, nilai dari PLAN.md) dan satu file komponen (`assets/components.css`, kelas per `COMP-xxx`). Tidak ada warna/spacing hardcoded di halaman.
- Navigasi alur utama berfungsi, konten contoh realistis, state penting bisa dicoba (error validasi, kosong, sukses), data mock ditandai mock.
- Kode prototype juga dalam bahasa Inggris (nama kelas, file, komentar).
- `prototype/README.md`: cara membuka, peta file ↔ SCR, state yang bisa dicoba, keterbatasan.
- Verifikasi: buka di browser bila bisa, cek semua tautan antarhalaman, cek tidak ada nilai hardcoded, jalankan `check_artifacts.py` (SCR tanpa file prototype harus kosong). Laporkan yang tidak bisa diverifikasi.

Tunjukkan cara membuka dan daftar halaman, minta persetujuan. Perubahan layout yang muncul di sini dibalikkan ke UI.md dulu. Prototype yang disetujui menjadi acuan visual implementasi.

## 6. implementation.md

Ikuti [references/implementation-template.md](references/implementation-template.md).

- Blok **Progres** di bawah judul.
- Task kecil (selesai dalam satu sesi kerja), urut sesuai dependensi: setup → tokens/layout → komponen `COMP-xxx` → per halaman `SCR-xxx` (sesuai wireframe dan prototype) → data/form → test → deploy.
- Setiap task: Ref (FR/SCR/COMP + file prototype), Dep, AC, Verifikasi. Semua `- [ ]`. Prototype **bukan** bukti task selesai.
- Setiap FR, SCR, dan COMP dalam scope punya minimal satu task. Cek dengan `check_artifacts.py <folder>`.
- Tunjukkan ringkasan (jumlah task, blocker), lalu tanya apakah mulai mengerjakan TASK pertama.

## 7. Mengerjakan task

Untuk setiap task:
1. Cek dokumentasi lewat **Context7** untuk library yang disentuh task.
2. Tulis kode sesuai "Aturan kode".
3. Verifikasi: jalankan lint/typecheck/test/build yang ada. Laporkan hasil nyata.
4. Ubah `- [ ]` jadi `- [x]` hanya jika terverifikasi, dengan bukti singkat di baris itu (misal `✔ npm test lulus`). Perbarui blok Progres.
5. Jika task mengubah scope, berhenti dan ikuti "Perubahan".

## Context7 (wajib)

Saat memilih stack dan sebelum menulis kode yang memakai library/framework:
1. Panggil tool Context7 `resolve-library-id` dengan nama library.
2. Ambil docs dengan `get-library-docs` / `query-docs` untuk topik yang dikerjakan (misal "app router", "form validation").
3. Ikuti API dan pola dari docs itu, bukan ingatan. Jika docs bertentangan dengan ingatanmu, docs menang.

Jika tool Context7 tidak tersedia: berhenti dan beri tahu pengguna. Sarankan pasang:
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```
Lanjut tanpa Context7 hanya jika pengguna mengizinkan secara eksplisit; catat di Status PLAN.md.

## Aturan kode

- **Bahasa Inggris** untuk nama variabel, fungsi, komponen, file, folder, komentar, pesan commit, dan nama test. Teks UI yang dilihat pengguna akhir tetap mengikuti bahasa produk.
- Ikuti konvensi resmi framework (dari Context7) dan struktur proyek yang sudah ada.
- Nama jelas dan deskriptif; fungsi kecil dengan satu tanggung jawab; tidak ada kode mati atau duplikasi.
- Pakai tokens dari PLAN.md, bukan warna/spacing hardcoded. Bangun halaman dari komponen `COMP-xxx`, ikuti wireframe UI.md dan tampilan prototype yang disetujui; jangan membuat komponen satu-off.
- Validasi input di batas sistem (form, API); tangani error dengan pesan yang jelas.
- Tidak ada secret di kode; pakai env variable dan `.env.example`.
- HTML semantik dan aksesibel: label form, alt text, fokus keyboard, kontras cukup.
- Komentar hanya untuk "kenapa", bukan "apa".
- Tambah test untuk logika yang tidak trivial; jalankan linter/formatter proyek.

## Perubahan

- **Requirement berubah:** sebut FR/SCR/COMP/TASK terdampak dan jumlah halaman sebelum → sesudah, minta persetujuan, lalu perbarui PRD → PLAN → UI → prototype → implementation.md. Jangan nomori ulang ID.
- **Layout berubah:** perbarui wireframe di UI.md dan prototype dulu, minta persetujuan, baru ubah kode.
- **Hanya visual berubah:** ubah tokens di PLAN.md, `prototype/assets/tokens.css`, dan file tokens di kode; cek kontras ulang; jangan edit halaman satu per satu dengan nilai hardcoded.
- **Implementasi mengungkap kebutuhan baru:** catat sebagai [Rekomendasi] atau OQ, tanya dulu sebelum menambah scope.

## Referensi

- [references/prd-template.md](references/prd-template.md) — tahap 2.
- [references/plan-template.md](references/plan-template.md) — tahap 3.
- [references/ui-template.md](references/ui-template.md) — tahap 4.
- [references/prototype-template.md](references/prototype-template.md) — tahap 5.
- [references/implementation-template.md](references/implementation-template.md) — tahap 6.
- [scripts/check_artifacts.py](scripts/check_artifacts.py) — cek SCR tanpa wireframe/prototype, COMP tak terpakai, FR/SCR/COMP tanpa task, hitung task; `--next` untuk task berikutnya.
