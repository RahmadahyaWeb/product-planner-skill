# implementation.md template

A work checklist, not a summary and not code. The file name is exactly `implementation.md`. Write task text in the user's language; IDs and code references stay as they are.

```markdown
# Implementation — <Project Name>

> **Progress** — last done: — · next: TASK-001 · code: `<repo path>` · stack: <from PLAN.md>
> New session: run `check_artifacts.py . --next`, read only that task and the sections it references.

Ref: [PRD](PRD.md) v1.0 · [PLAN](PLAN.md) v1.0 · [UI](UI.md) v1.0 · [Prototype](prototype/README.md) approved YYYY-MM-DD
Status: `- [ ]` open · `- [x]` done + evidence · `⛔ BLOCKED` blocked

## Setup
- [ ] **TASK-001 — Init Next.js + TypeScript + linter** — Ref: PLAN §Stack · AC: `npm run dev` runs, lint passes · Verify: `npm run lint && npm run build`.
- [ ] **TASK-002 — Global tokens and theme** — Ref: PLAN §Design, `prototype/assets/tokens.css` · Dep: TASK-001 · AC: values match the prototype tokens · Verify: build + visual check at 360/1280.

## Components
- [ ] **TASK-003 — COMP-002 Button + COMP-005 TextField with all states** — Ref: COMP-002, COMP-005 · Dep: TASK-002 · AC: variants and states match UI.md and `prototype/assets/components.css`, visible focus · Verify: render unit tests + keyboard test.
- [ ] **TASK-004 — COMP-001 Header, COMP-003 Card, COMP-004 Footer** — Ref: COMP-001, COMP-003, COMP-004 · Dep: TASK-002 · AC: match UI.md, mobile menu opens/closes · Verify: render tests at 360/1280.

## Pages
### SCR-001 — Home
- [ ] **TASK-005 — SCR-001: build per wireframe (hero, services, CTA)** — Ref: SCR-001, FR-001, [prototype](prototype/pages/scr-001-home.html) · Dep: TASK-003, TASK-004 · AC: FR-001 criteria met, matches the prototype at 360/1280 · Verify: render test + Lighthouse a11y ≥ 90.

### SCR-002 — Contact
- [ ] **TASK-006 — SCR-002: form per wireframe + validation** — Ref: SCR-002, FR-002, [prototype](prototype/pages/scr-002-contact.html) · Dep: TASK-003 · AC: invalid email rejected, success shows a confirmation · Verify: validation unit tests.
- [ ] **TASK-007 — ⛔ BLOCKED: send notification email (FR-003)** — Blocker: OQ-001 email provider.

## Quality and release
- [ ] **TASK-008 — NFR-001 performance** — Verify: Lighthouse LCP < 2.5 s.
- [ ] **TASK-009 — Deploy to hosting + environment variables** — Dep: all Must tasks · Verify: production URL opens, form works.

## Summary
Tasks: 0 / 9 · Blocked: TASK-007 (OQ-001)
```

Rules:
- One task = one verifiable result. Never a task like "implement all pages".
- Components are built before pages; page tasks reference the UI.md wireframe and their prototype file, and use components instead of their own styles.
- An existing prototype is **not** evidence a task is done; `[x]` is only for verified application code.
- `- [x]` only after real verification, with the evidence on that line (e.g. `✔ npm test 12/12`).
- Summary numbers come from `check_artifacts.py`, not guesses.
- Task IDs are never renumbered; removed tasks are struck through with a reason.
- Dependencies are written as `Dep: TASK-xxx` (or `Dependencies:`); `--next` skips tasks whose dependencies are not `[x]`.
- Update the Progress block after every finished task.
