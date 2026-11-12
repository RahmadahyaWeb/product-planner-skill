# PLAN.md template

One file for pages, design, stack, and status. Delete sections that do not apply. Write it in the user's language.

```markdown
# PLAN — <Project Name>

Version 1.0 · YYYY-MM-DD

## Status
| Stage | Status | Date |
|-------|--------|------|
| PRD | approved | YYYY-MM-DD |
| PLAN | awaiting approval | |
| UI (wireframes + components) | not started | |
| Prototype | not started | |
| Implementation | not started | |

Decisions: <date> — <decision> (source: user / approved recommendation)
Next step: …

## Pages

<N> pages, because: <the flows/features that require them>.

| ID | Page | Route | FR | Main content | Key states |
|----|------|-------|----|--------------|------------|
| SCR-001 | Home | `/` | FR-001 | hero, service summary, contact CTA | — |
| SCR-002 | Contact | `/contact` | FR-002 | name/email/message form | validation error, success, send failure |

Navigation: header (Home, Services, Contact) · footer.
Modals/overlays: <if any, name the parent SCR>.
Deferred: <pages not in this version>.

## Design
Visual direction: <2–3 sentences: feel, references, mobile-first?>

Tokens (single source of truth; in code they become CSS variables / theme config):
| Token | Value |
|-------|-------|
| color-primary | #1D4ED8 |
| color-text | #111827 |
| color-bg | #FFFFFF |
| font-body | Inter, sans-serif |
| space-unit | 4px |
| radius | 8px |

Breakpoints: 360 / 768 / 1280. Accessibility: WCAG 2.2 AA [Recommendation]; contrast primary vs bg: 4.5:1 ✔.
Components and wireframes: see [UI.md](UI.md).

## Stack
| Part | Choice | Version (checked via Context7) | Reason |
|------|--------|--------------------------------|--------|
| Framework | Next.js | 15.x | SSG + form API route |
| Styling | Tailwind CSS | 4.x | tokens via theme |
| Hosting | Vercel | — | free at this scale |

Conventions: code in English, folder structure follows the framework docs, linter/formatter: <…>.
```

Short rules:
- Derive the page count from flows, not from the number of features. One page may cover several FRs.
- Every FR with `Needs UI: Yes` appears in the FR column of at least one page.
- A stack the user has not confirmed is marked [Recommendation].
