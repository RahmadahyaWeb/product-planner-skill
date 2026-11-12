---
type: llm
focus: trace
weight: 1
---

Before writing code that uses a library or framework, the agent queries Context7 (resolve-library-id then get-library-docs/query-docs); if Context7 tools are unavailable it tells the user and does not silently continue. Any code written uses English identifiers, file names and comments.
