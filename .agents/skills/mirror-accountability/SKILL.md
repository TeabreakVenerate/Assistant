---
name: mirror-accountability
description: Automates daily and weekly task planning, unstructured brain dump processing, Eisenhower Matrix prioritization (Q1-Q4), time-blocking schedule generation, and daily accountability auditing. Activate whenever the user asks to plan their day, provides a messy task dump, or audits daily wins and slips.
---

# Mirror Accountability Skill

This skill transforms chaotic brain dumps into disciplined, time-blocked execution schedules.

## Workflow

### 1. Process Unstructured Brain Dumps
When the user pastes or dictates a raw dump of tasks:
1. Parse every distinct task, commitment, test, and errand.
2. Filter through `04_frameworks_decision_engines/eisenhower_matrix.md`:
   - Sort into Q1 (Crisis), Q2 (Deep Work), Q3 (Admin/Errands), and Q4 (Eliminate).
3. Read `02_identity_and_rules/weekly_timetable.md` to identify open time slots.
4. Output a clean, time-blocked daily execution plan.

### 2. Daily Accountability Audit
When the user reviews their day:
1. Compare completed work against planned focus blocks.
2. Append completed high-leverage tasks to `01_logs_operational_history/accountability_log.md` under **Trophy Room**.
3. Record incomplete tasks to **Graveyard** with an objective root-cause diagnosis.
