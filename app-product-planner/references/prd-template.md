# PRD.md template

A checklist, not a form. Delete sections that do not apply. A small website fits on one page. Write the document in the user's language; the headings below may be translated.

```markdown
# PRD — <Project Name>

Version 1.0 · YYYY-MM-DD · Status: awaiting approval

## Problem
<1–3 sentences: what problem, for whom, how it is handled today>

## Users
- <Role> — <main need>

## Goals
- <expected outcome, measurable where possible>

**Not a goal for this version:** <what is deliberately left out>

## Features

| ID | Feature | Priority | Needs UI |
|----|---------|----------|----------|
| FR-001 | Visitors see the list of services | Must | Yes |
| FR-002 | Visitors send the contact form | Must | Yes |
| FR-003 | Admin receives an email notification for each contact | Should | No |

### FR-001 — Service list
- AC: Given the Services page is opened, Then every active service shows its title, description, and price.
- AC: Given there are no services, Then a clear empty message is shown.

### FR-002 — Contact form
- AC: Given a name, a valid email, and a message, When sent, Then the message is saved and a confirmation is shown.
- AC: Given an invalid email, Then the form rejects it with an error on the email field.

## Non-functional requirements (only when needed)
| ID | Requirement | Target | How to check |
|----|-------------|--------|--------------|
| NFR-001 | Home page performance | LCP < 2.5 s on 4G | Lighthouse |

## Constraints
<deadline, hosting, budget, integrations, language>

## Assumptions and open questions
- [Assumption] …
- OQ-001 — … (blocks: FR-00x?)
```

Short rules:
- Acceptance criteria are concrete and testable, including one important failure case.
- NFRs have a number or a way to check them, never just "fast"/"secure".
- Priorities are explicit; Must = required in the first version.
- In the Needs UI column, `No` (or `Tidak`) marks an FR without a page; `check_artifacts.py` reads it.
