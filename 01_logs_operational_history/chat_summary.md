# Chat Context & Architecture Summary

A persistent backup of strategic decisions, architectural agreements, and contextual memory. When starting a fresh AI conversation or switching between LLMs, point the assistant to this file to prevent information loss.

---

## 1. System Operating Principles
* **Local State Over Cloud Memory:** Context lives in plain markdown files on your local drive, not inside ephemeral browser tabs.
* **Anti-Sycophancy Invariant:** The assistant is instructed to provide honest, friction-filled feedback, eliminate bloated plans, and audit failures objectively.
* **The Two-Strike Rule:** If any script or implementation fails twice, the assistant stops, analyzes the failure, and awaits instructions.

---

## 2. Active Milestones & Architectural Decisions
* **Decision 1 (Markdown Single Source of Truth):** Using markdown ledgers (`accountability_log.md`, `financial_log.md`) as the definitive records for daily operations.
* **Decision 2 (Idea Containment):** Any new venture or tool idea raised mid-week is redirected to `idea_tank.md` and evaluated strictly during the Sunday review.
* **Decision 3 (Grill-Me Protocol):** The user can trigger `/grill-me` whenever formulating a new project or plan to force the AI into an interrogative interview mode before generating solutions.
