# prototype/ template

A static HTML/CSS/JS prototype of every page. Created after UI.md is approved; approved before implementation.md.

## Structure

```
prototype/
├── index.html              # page list + links (hub)
├── README.md
├── assets/
│   ├── tokens.css          # CSS variables from PLAN.md (single source of values)
│   ├── components.css      # one class block per COMP-xxx, using var(--…) only
│   ├── app.js              # shared interactions (menu, modal, demo validation)
│   └── mock-data.js        # sample data, marked MOCK
└── pages/
    ├── scr-001-home.html
    └── scr-002-contact.html
```

## Rules

- Page file name `scr-xxx-<slug>.html`. First line after `<!doctype html>`:
  `<!-- SCR-002 Contact + SCR-002a Success modal | FR-002 -->`
  (the part before `|` = the SCRs this file covers; read by `check_artifacts.py`).
- Every page loads `tokens.css`, then `components.css`. No `style=""` and no color/spacing/font values outside the tokens.
- Component classes carry an ID comment: `/* COMP-002 Button */ .btn, .btn--primary, .btn:disabled …`.
- Section order matches the UI.md wireframe exactly; mobile-first, checked at 360 and 1280.
- Main-flow navigation is real (links between pages). Actions that need a backend are simulated in `app.js` and marked `// MOCK`.
- Key states can be tried: e.g. submitting an empty form → error; a `?state=empty` parameter for the empty view.
- Semantic, accessible HTML: `<label>` for inputs, `alt`, visible focus, landmarks (`header`, `main`, `nav`, `footer`).
- Class names, file names, ids, and comments are in English; visible text follows the product's language.

## README.md

```markdown
# Prototype — <Project Name>

Open: `prototype/index.html` in a browser (no server needed).

| SCR | Page | File | Status |
|-----|------|------|--------|
| SCR-001 | Home | [pages/scr-001-home.html](pages/scr-001-home.html) | done |

Try: the contact flow (send empty → error, fill in correctly → success), `?state=empty` on Home.
Simulated (MOCK): form submission, service data.
Limitations: no backend, no real authentication.
```

## Verify before asking for approval

1. `check_artifacts.py <folder>` → "SCR without prototype file: none".
2. Every link between pages and from `index.html` works.
3. `grep -nE '#[0-9a-fA-F]{3,6}|[0-9]+px' prototype/pages prototype/assets/components.css` → no values outside the tokens (except deliberate ones; name them).
4. Open it in a browser if available; if not, say the visuals have not been checked.
