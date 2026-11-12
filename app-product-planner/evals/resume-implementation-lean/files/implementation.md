# Implementation Checklist — KasirKu

| Versi | Tanggal | Status |
|-------|---------|--------|
| 1.0 | 2026-10-13 | Draft handoff |

## Referensi artefak
| Artefak | Versi | Status |
|---------|-------|--------|
| [PRD](PRD.md) | v1.0 | Disetujui 2026-10-03 |
| [Design System](DESIGN-SYSTEM.md) | v1.0 | Disetujui 2026-10-06 |
| [UI-UX-PLAN](UI-UX-PLAN.md) | v1.0 | Disetujui 2026-10-09 |
| [Prototype](prototype/README.md) | v1.0 | 5/5 completed |
| [Traceability](TRACEABILITY.md) | v1.0 | |

## Ringkasan scope
MVP: login OTP, kasir, produk, laporan harian, backup harian.

## Keputusan teknis
- Dikonfirmasi: web mobile-first (DEC-001).
- Usulan: Next.js + PostgreSQL (belum dikonfirmasi).

## Dependensi dan blocker
| ID | Blocker | Memblokir | Status |
|----|---------|-----------|--------|
| OQ-001 | Penyedia OTP | TASK-012 | terbuka |

## Definition of Done
Semua task Must selesai dengan bukti; AC lulus; NFR terverifikasi; design QA lulus.

## Arti status
`- [ ]` belum · `- [x]` selesai dengan bukti · `⛔ BLOCKED` terhalang

## A. Readiness
- [ ] **TASK-001 — Konfirmasi scope MVP** — Ref: PRD §5 · AC: product sign-off · Verifikasi: catatan rapat.
- [ ] **TASK-002 — Putuskan penyedia OTP (OQ-001)** — Ref: FR-001 · AC: keputusan tercatat di DEC · Verifikasi: PLANNING-STATUS.
- [ ] **TASK-003 — Konfirmasi stack dan environment** — AC: stack disetujui engineering.

## B. Design System
- [ ] **TASK-004 — Implementasi tokens dari prototype/assets/tokens.css** — Ref: DESIGN-SYSTEM §3 · AC: semua nilai sama · Verifikasi: review kode.
- [ ] **TASK-005 — Komponen COMP-001..COMP-009 dengan states** — Dep: TASK-004 · AC: states sesuai DS · Verifikasi: storybook/visual test.
- [ ] **TASK-006 — Verifikasi kontras warna (NFR-002)** — Ref: DESIGN-SYSTEM §3 tabel kontras · AC: semua pasangan ≥ 4.5:1 · Verifikasi: tool kontras.

## C. Data & business rules
- [ ] **TASK-007 — Model data produk, transaksi, pengguna** — AC: skema mendukung FR-002..FR-005.
- [ ] **TASK-008 — BR-001 stok tidak negatif (server-side)** — Ref: FR-003, AC-004 · Verifikasi: unit test.
- [ ] **TASK-009 — BR-002 otorisasi peran** — Ref: FR-004, FR-005, AC-006 · Verifikasi: test otorisasi.
- [ ] **TASK-010 — Job backup harian 23.00 (FR-006)** — AC: AC-008 · Verifikasi: test job + log gagal.

## D. Halaman
### SCR-001 — Login (FLOW-001)
- [ ] **TASK-011 — SCR-001: struktur, route /login, form** — Ref: FR-001, AC-001 · Dep: TASK-005 · Verifikasi: e2e.
- [ ] **TASK-012 — ⛔ BLOCKED: SCR-001 integrasi OTP nyata** — Blocker: OQ-001 · AC: AC-001, AC-002 · Verifikasi: integration test sandbox.
- [ ] **TASK-013 — SCR-001: state OTP salah/terkunci, a11y, responsive** — AC: AC-002, NFR-002 · Verifikasi: e2e + axe.
### SCR-002 / SCR-002a — Kasir + Modal Bayar (FLOW-002)
- [ ] **TASK-014 — SCR-002: struktur, route /kasir, data produk nyata** — Ref: FR-002 · Dep: TASK-007 · Verifikasi: integration test.
- [ ] **TASK-015 — SCR-002a: modal bayar, kembalian, simpan** — Ref: FR-002, AC-003 · Verifikasi: acceptance test.
- [ ] **TASK-016 — SCR-002: validasi stok + banner (FR-003)** — AC: AC-004 · Verifikasi: acceptance test.
- [ ] **TASK-017 — SCR-002: performance, a11y, target sentuh, design QA** — AC: NFR-001, NFR-002, NFR-003 · Verifikasi: Lighthouse, axe, review design.
### SCR-003 — Produk (FLOW-003)
- [ ] **TASK-018 — SCR-003: daftar, tambah, ubah, nonaktifkan** — Ref: FR-004, AC-005 · Verifikasi: e2e.
- [ ] **TASK-019 — SCR-003: permission-denied untuk Kasir, a11y, design QA** — AC: AC-006, NFR-002 · Verifikasi: e2e peran.
### SCR-004 — Laporan (FLOW-004)
- [ ] **TASK-020 — SCR-004: data laporan nyata, empty state** — Ref: FR-005, AC-007 · Verifikasi: integration test.
- [ ] **TASK-021 — SCR-004: a11y, responsive, design QA** — AC: NFR-002 · Verifikasi: axe + review.

## E. Integrasi
- Tercakup di TASK-012 (OTP). Tidak ada integrasi lain di MVP.

## F. NFR
- [ ] **TASK-022 — NFR-001 performance Kasir** — Target < 2 dtk p95 · Verifikasi: Lighthouse staging.
- [ ] **TASK-023 — NFR-002 audit WCAG 2.2 AA semua halaman** — Verifikasi: axe + keyboard manual.

## G. Analytics
- [ ] **TASK-024 — Event sale_completed, report_viewed** — Verifikasi: payload tervalidasi di staging.

## H. Testing
- [ ] **TASK-025 — E2E FLOW-001..FLOW-004** — Verifikasi: CI hijau.
- [ ] **TASK-026 — Design QA vs Design System & prototype** — Verifikasi: checklist design QA.

## I. Release
- [ ] **TASK-027 — Go/no-go, rollback, secrets production**

## J. Post-release
- [ ] **TASK-028 — Smoke test, monitoring, validasi metrik G-1/G-2**

## Summary
- Task selesai: 0 / 28
- Task blocked: 1 (TASK-012)
- Requirement tanpa task: tidak ada
- Halaman tanpa task: tidak ada
- Blocker: OQ-001

**Readiness:** siap sebagian — semua kecuali integrasi OTP.

## Sign-off
| Peran | Nama | Tanggal |
|-------|------|---------|
| Product | | |
| Design | | |
| Engineering | | |
| QA | | |
