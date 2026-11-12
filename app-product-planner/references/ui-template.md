# UI.md template

Flows, wireframes, and components. Created after PLAN.md is approved; approved before the prototype is built. Write it in the user's language.

```markdown
# UI — <Project Name>

Version 1.0 · YYYY-MM-DD · Status: awaiting approval
Tokens and page list: see [PLAN.md](PLAN.md).

## Main flows
- **Contact the business (FR-001, FR-002):** SCR-001 Home → click "Contact us" → SCR-002 Contact → fill in the form → send → success message.
  Failure: invalid email → error on the field, entered data is kept.

## Wireframes

### SCR-001 — Home (`/`)
Mobile 360:
┌──────────────────────────┐
│ [Logo]          [☰ Menu] │  COMP-001 Header
├──────────────────────────┤
│ Big headline (H1)        │  Hero
│ Subheading, 1–2 lines    │
│ [ Contact us ]           │  COMP-002 Button primary → SCR-002
├──────────────────────────┤
│ ┌──────────┐             │  Services: COMP-003 Card × n
│ │ Title    │ (stacked,   │
│ │ Desc.    │  1 column)  │
│ └──────────┘             │
├──────────────────────────┤
│ Footer: contact · social │  COMP-004 Footer
└──────────────────────────┘
Desktop 1280: service cards in 3 columns; menu shown in the header (no ☰).
State: no services → text "Services coming soon".

### SCR-002 — Contact (`/contact`)
…

## Components

| ID | Component | Variants | States | Tokens | Used in |
|----|-----------|----------|--------|--------|---------|
| COMP-001 | Header | — | menu open/closed (mobile) | color-bg, space | SCR-001, SCR-002 |
| COMP-002 | Button | primary, secondary | default, hover, focus, disabled, loading | color-primary, radius | SCR-001, SCR-002 |
| COMP-003 | Card | — | default, hover | radius, space | SCR-001 |
| COMP-004 | Footer | — | — | color-text | all |
| COMP-005 | TextField | text, email, textarea | default, focus, error, disabled | color-text, radius | SCR-002 |

Component accessibility: visible focus, a label for every input, touch targets ≥ 44px.
UI library (if any): <name, version checked via Context7> — COMP-002 → `Button`, COMP-005 → `Input`/`Textarea`.
```

Short rules:
- A wireframe is structure and order, not the final design. No colors; boxes, labels, and actions are enough.
- Every important action names its navigation target (`→ SCR-xxx`).
- Each page gets a heading with its SCR ID (`### SCR-001 — …`); `check_artifacts.py` uses these headings.
- Only components that actually appear in a wireframe. Components are reused, never rebuilt per page.
- In the "Used in" column, list SCR IDs or `all`; a component with neither is reported as unused.
- Modals/overlays are drawn under their parent page's wireframe.
