---
name: app-product-planner
description: Plan and build simple websites/apps through a lean, approval-gated flow - short interview, PRD.md, PLAN.md (pages, design tokens, stack), UI.md (user flows, wireframes, components), an HTML prototype of every page, implementation.md (TASK-xxx checklist), then execute tasks one by one. Use when the user has a website or app idea ("I want to build a website...", "mau bikin aplikasi..."), asks for a PRD, requirements, page list, sitemap, wireframes, UI components, prototype, design direction, stack choice, or an implementation checklist; also to update the plan or resume a session ("continue implementation from implementation.md"). During implementation, library docs must be checked through the Context7 MCP and code must be written in English following best practices. Not for bug fixes or coding outside implementation.md, pure graphic design, or small UI/UX questions.
---

# App Product Planner (lean)

Turn a website/app idea into a short plan that can be built right away, then build it task by task.

| File | Contents |
|------|----------|
| `PRD.md` | Problem, users, scope, features `FR-xxx` + acceptance criteria |
| `PLAN.md` | Pages `SCR-xxx`, design direction + tokens, stack (checked via Context7), status |
| `UI.md` | Main flows, a wireframe for every `SCR-xxx`, components `COMP-xxx` |
| `prototype/` | Static HTML/CSS/JS prototype of every page + `README.md` |
| `implementation.md` | Progress block + `TASK-xxx` checklist |

Reply in the user's language. Write planning documents in the user's language too. **Code is always in English** (see "Code rules").

## Flow

```
Interview (1–2 rounds) → PRD.md ⛔ → PLAN.md ⛔ → UI.md ⛔ → prototype/ ⛔ → implementation.md → execute tasks
```

⛔ = stop, show the result, ask for approval. Approving the PRD is not approving the PLAN. If the user says a stage is already approved, record it in `PLAN.md` and move on. For very small projects (1–3 pages), PLAN and UI may be presented in one round with two separate approvals. Wireframes, components, and the prototype **must** be approved in order before implementation.md is created and before any application code is written.

## Where to start

First check which files exist in the working folder.

- **Resume implementation** ("continue implementation", "do the next task", "lanjutkan implementasi") → token-saving mode:
  1. Run `python3 /absolute/path/to/app-product-planner/scripts/check_artifacts.py <folder> --next` (or `--next 3`). Do not Read `implementation.md` in full.
  2. Read only the `file:line` pointers from the output (offset/limit, ±30 lines). The Stack section of `PLAN.md`, the wireframe in `UI.md`, and the prototype file of the page being built may also be read.
  3. Do not read `references/*.md` or the full PRD/PLAN/UI. Do not interview.
  4. Do the task following "Code rules".
- **PRD/PLAN/UI/prototype exist but are unfinished** → read the Status section of `PLAN.md` (or the PRD), summarize where things stand, continue from that stage.
- **No files yet** → interview. Do not create files in the first reply, even if asked to directly.
- **User brings their own documents** → use them as input and flag what is missing.

## Principles

- **Proportional.** A 3-page website needs a one-page PRD. Delete template sections that do not apply.
- **Do not invent.** Mark anything uncertain as **[Assumption]**, your proposals as **[Recommendation]** (with a short reason), and open questions as `OQ-xxx`.
- If the user does not know, offer 2–3 options plus a recommendation.
- Features or pages nobody asked for are a **[Recommendation]**, never silent scope.
- **Stable IDs:** `FR-001`, `NFR-001` (only when needed), `SCR-001`, `COMP-001`, `TASK-001`, `OQ-001`. Never renumber; strike removed items `~~FR-004~~ (removed: reason)`.
- Never claim something is done when it is not.

## 1. Interview

Greet briefly, explain the flow in one line, ask **3–5 questions** per round. 1–2 rounds are usually enough.

- Round 1: the problem, who the users are, goals/expected outcome, must-have features for the first version.
- Round 2 (if needed): roles/login, content and data, constraints (deadline, hosting, integrations), visual direction, stack if already chosen.
- If the user already gave a lot of context, summarize what you understood (2–4 bullets) and ask only about the gaps. Never re-ask.
- Dig into vague answers ("it must be fast" → which page, how many seconds?).

## 2. PRD.md ⛔

Follow [references/prd-template.md](references/prd-template.md). Every `FR` has a priority (Must/Should/Could) and 1–3 testable acceptance criteria. Mark FRs without UI (`Needs UI: No`). Show it, highlight risky assumptions/OQs, ask for scope approval.

## 3. PLAN.md ⛔

Follow [references/plan-template.md](references/plan-template.md). Contents:

- **Pages:** list of `SCR-xxx` (purpose, route, related FRs, main content, key states). Derive the page count from features and flows, and give the reason.
- **Design:** short visual direction + tokens (colors, fonts, spacing, radius). Default accessibility target WCAG 2.2 AA [Recommendation].
- **Stack:** proposed framework/libraries. **Must be checked via Context7** (see "Context7") for the current version and recommended usage; record the version checked.
- **Status:** PRD/PLAN/UI/Prototype/Implementation gates + key decisions.

## 4. UI.md — flows, wireframes, components ⛔

Follow [references/ui-template.md](references/ui-template.md). Created after the PLAN is approved.

- **Main flows:** 1–3 important flows from the FRs (steps per page, including the important failure path).
- **Wireframe for every `SCR-xxx`:** low-fidelity ASCII, section order top to bottom, main elements and actions, marking the `COMP-xxx` used. Mobile is required; desktop only if the layout differs. Key states (empty/error/success) as a note under the wireframe.
- **Components `COMP-xxx`:** derived from the wireframes (not a generic library): name, variants, states (default/hover/focus/disabled/error/loading where relevant), tokens used, which SCRs use it. If the project uses a UI library (e.g. shadcn/ui), check it via Context7 and map each COMP to a library component.
- Every SCR has a wireframe; every COMP is used by at least one SCR. Check with `check_artifacts.py`.

Show the wireframes and the component list, ask for approval. Revising a wireframe here is far cheaper than after code is written.

## 5. HTML prototype ⛔

Follow [references/prototype-template.md](references/prototype-template.md). Created after UI.md is approved; required for every project.

- Static HTML/CSS/JS with no build step (unless the user asks for another format, e.g. the project's framework). Opens directly in a browser.
- **Every** approved `SCR-xxx`, one file per page, following the UI.md wireframes.
- One tokens file (`assets/tokens.css`, values from PLAN.md) and one components file (`assets/components.css`, one class block per `COMP-xxx`). No hardcoded colors/spacing in pages.
- Main-flow navigation works, realistic sample content, key states can be tried (validation error, empty, success), mock data is marked as mock.
- Prototype code is in English too (class names, files, comments).
- `prototype/README.md`: how to open it, file ↔ SCR map, states that can be tried, limitations.
- Verify: open in a browser if possible, check every link between pages, check for hardcoded values, run `check_artifacts.py` ("SCR without prototype file" must be empty). Report what could not be verified.

Show how to open it and the page list, ask for approval. Layout changes that come up here go back into UI.md first. The approved prototype becomes the visual reference for implementation.

## 6. implementation.md

Follow [references/implementation-template.md](references/implementation-template.md).

- **Progress** block under the title.
- Small tasks (finishable in one work session), ordered by dependency: setup → tokens/layout → components `COMP-xxx` → each page `SCR-xxx` (following the wireframe and prototype) → data/forms → tests → deploy.
- Every task: Ref (FR/SCR/COMP + prototype file), Dep, AC, Verify. All `- [ ]`. The prototype is **not** evidence a task is done.
- Every in-scope FR, SCR, and COMP has at least one task. Check with `check_artifacts.py <folder>`.
- Show a summary (task count, blockers), then ask whether to start the first TASK.

## 7. Executing tasks

For each task:
1. Check the docs via **Context7** for every library the task touches.
2. Write code following "Code rules".
3. Verify: run the existing lint/typecheck/test/build. Report real results.
4. Change `- [ ]` to `- [x]` only when verified, with short evidence on that line (e.g. `✔ npm test passed`). Update the Progress block.
5. If the task changes scope, stop and follow "Changes".

## Context7 (required)

When choosing the stack and before writing code that uses a library/framework:
1. Call the Context7 tool `resolve-library-id` with the library name.
2. Fetch docs with `get-library-docs` / `query-docs` for the topic at hand (e.g. "app router", "form validation").
3. Follow the APIs and patterns from those docs, not memory. When the docs disagree with your memory, the docs win.

If the Context7 tools are unavailable: stop and tell the user. Suggest installing it:
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```
Continue without Context7 only if the user explicitly allows it; record that in the PLAN.md Status.

## Code rules

- **English** for variable, function, component, file, and folder names, comments, commit messages, and test names. User-facing UI text follows the product's language.
- Follow the framework's official conventions (from Context7) and the existing project structure.
- Clear, descriptive names; small single-purpose functions; no dead or duplicated code.
- Use the tokens from PLAN.md, never hardcoded colors/spacing. Build pages from `COMP-xxx` components, following the UI.md wireframes and the approved prototype; no one-off components.
- Validate input at system boundaries (forms, APIs); handle errors with clear messages.
- No secrets in code; use environment variables and `.env.example`.
- Semantic, accessible HTML: form labels, alt text, keyboard focus, sufficient contrast.
- Comments explain "why", not "what".
- Add tests for non-trivial logic; run the project's linter/formatter.

## Changes

- **Requirement changes:** name the affected FR/SCR/COMP/TASK and the page count before → after, ask for approval, then update PRD → PLAN → UI → prototype → implementation.md. Never renumber IDs.
- **Layout changes:** update the UI.md wireframe and the prototype first, ask for approval, then change the code.
- **Visual-only changes:** change the tokens in PLAN.md, `prototype/assets/tokens.css`, and the tokens file in the code; recheck contrast; never patch pages one by one with hardcoded values.
- **Implementation reveals a new need:** record it as a [Recommendation] or OQ, and ask before adding scope.

## References

- [references/prd-template.md](references/prd-template.md) — stage 2.
- [references/plan-template.md](references/plan-template.md) — stage 3.
- [references/ui-template.md](references/ui-template.md) — stage 4.
- [references/prototype-template.md](references/prototype-template.md) — stage 5.
- [references/implementation-template.md](references/implementation-template.md) — stage 6.
- [scripts/check_artifacts.py](scripts/check_artifacts.py) — finds SCRs without wireframe/prototype, unused COMPs, FR/SCR/COMP without tasks, counts tasks; `--next` returns the next task.
