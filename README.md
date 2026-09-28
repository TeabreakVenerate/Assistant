# The Mirror System: Persistent AI Operating Assistant Template

> An open-source, local-first framework that turns **any AI tool or LLM**—whether an AI code editor (Antigravity, Cursor, Windsurf, VS Code Copilot, Claude Code) or a standard web chat (ChatGPT, Gemini, Claude)—into a persistent executive assistant with zero daily memory loss.

Built by **Endurance Owie** ([LinkedIn](https://www.linkedin.com/in/endurance-owie))

---

## The Core Problem: AI Amnesia & Polite Hallucinations

Anyone who uses AI models to manage daily schedules, project pipelines, and intellectual work encounters two massive bottlenecks:

1. **Daily Amnesia:** Web chat windows reset constantly. You spend 20 minutes re-explaining your schedule, active deadlines, and working rules, only for the AI to forget everything the moment you open a new tab.
2. **Polite, Generic Advice (Sycophancy):** When you feed an LLM an unvetted idea or a vague task, it defaults to agreeable fluff. Instead of pointing out unrealistic timelines, missing details, or obvious bottlenecks, it generates three pages of bloated boilerplate.

### The Solution: The Mirror System

The Mirror System replaces ephemeral chat prompts with a **persistent local folder of markdown files**:

* **Your Context Stays on Your Laptop:** Your timetable, active deadlines, expense logs, and rules live as plain text files on your local drive.
* **Persistent Rulebook (`AGENTS.md`):** A single master directive file defines the AI's identity, anti-sycophancy guardrails, context router, and logging rules.
* **Universal Compatibility:** Works seamlessly with agent-enabled IDEs (reading and writing files automatically) OR with standard browser chats (by uploading or referencing your workspace files).

---

## System Architecture

```text
antigravity-mirror-template/
├── AGENTS.md                          # Master system prompt and operational rulebook
├── 01_logs_operational_history/       # Real-time operational audit logs
│   ├── accountability_log.md         # Daily Trophy Room (wins) & Graveyard (slips)
│   ├── financial_log.md              # Personal expense ledger
│   ├── task_calendar.md              # Active commitments & weekly landscape
│   ├── command_log.md                # System commands & script execution records
│   ├── session_summary.md            # High-bandwidth session milestones
│   └── chat_summary.md               # Key architectural decisions & context backup
├── 02_identity_and_rules/             # Personal context & physical reality
│   ├── profile_and_constraints.md    # Working hours, battery windows, Wi-Fi zones
│   └── weekly_timetable.md           # Class, work, or recurring schedule grid
├── 03_automations/                    # Optional automation scripts
│   ├── README.md                     # Automation setup guide
│   └── push_schedule_template.py     # Calendar sync starter template
├── 04_frameworks_decision_engines/    # Cognitive models for the assistant
│   ├── eisenhower_matrix.md          # Q1-Q4 triage rules (eliminate Q4 immediately)
│   └── idea_tank.md                  # Idea parking lot (stops shiny-object syndrome)
└── .agents/skills/                    # Specialized agent tool workflows
    ├── mirror-accountability/        # Brain dump parsing and schedule building
    └── humanizer/                    # Anti-AI writing filter and rhythm validator
```

---

## Works Across Any AI Tool

You do not need a specific proprietary editor to use this system. It adapts to whatever AI environment you use:

### Option A: In an AI-Enabled Code Editor (Antigravity, Cursor, Windsurf, VS Code Copilot)
* Open this folder as your workspace.
* The editor mounts `AGENTS.md` automatically on every turn.
* The AI reads your timetable and logs directly from your drive, sorts your schedule, and writes completed wins back to your files without copy-pasting.

### Option B: In Command-Line Agents (Claude Code, Aider)
* Run your CLI agent directly inside this repository.
* The agent reads `AGENTS.md` and updates files as you give verbal or typed instructions.

### Option C: In Standard Web Chats (ChatGPT, Google Gemini, Claude, Perplexity)
* Keep this folder organized on your laptop.
* When starting a new session or planning your week, attach or paste:
  1. `AGENTS.md` (to set the rules, anti-sycophancy, and tone).
  2. `02_identity_and_rules/weekly_timetable.md` (to give it your real schedule).
  3. Your raw task dump.
* Copy the output back into your local markdown files at the end of the day.

---

## The Universal "Grill-Me" Protocol

One of the most powerful workflows in this framework is the **Grill-Me Protocol**.

### Why It Matters
When you ask an AI: *"Help me design a launch plan for my app"* or *"Help me study for my exams"*, standard models immediately generate generic 10-step plans filled with empty corporate jargon. They do not know your constraints, your actual time availability, your budget, or your skill level.

Instead of letting the AI guess, you force it to **interrogate you first**.

### The Universal Grill-Me Prompt (Copy & Paste Into ANY LLM)

Drop this exact prompt into ChatGPT, Gemini, Claude, or your code editor whenever you are starting a new project, plan, or piece of writing:

```text
I want to [INSERT GOAL OR PROJECT HERE, e.g. build an MVP for student book preorders / prepare for finals / write a personal essay], but DO NOT give me a solution, plan, or draft yet.

Act as an elite, ruthless systems architect and consultant. Your job right now is to interview and GRILL me to extract all necessary context, uncover blind spots, and challenge weak assumptions.

Ask me 3 to 5 targeted, high-friction questions covering:
1. Hard constraints (actual available hours per day, budget, deadlines, physical gear limitations).
2. Concrete reality (exact numbers, existing tech stack or materials, who has actually committed vs. who is just cheering).
3. Past failure points (what broke the last time I attempted something similar, and what friction I am currently avoiding).

Format your questions clearly with selectable options where possible. Wait for my answers before you propose any architecture, schedule, or plan.
```

### What Happens When You Use This:
* **Zero Fluff:** The AI stops nodding along and forces you to confront the real constraints of your week.
* **High-Signal Plans:** Once you answer the questions, the resulting execution plan is tailored to your exact reality rather than a generic template.
* **Catches Self-Deception:** If you claim you will study 8 hours on a day packed with lectures, the AI flags the mathematical impossibility immediately.

---

## Quickstart Guide

### Step 1: Clone This Repository
```bash
git clone https://github.com/<your-username>/antigravity-mirror-template.git my-assistant
cd my-assistant
```

### Step 2: Customize Your Identity
1. Open `AGENTS.md` and replace the placeholder fields (`{{USER_NAME}}`, `{{FIELD_OR_ROLE}}`, `{{ORGANIZATION_OR_UNIVERSITY}}`).
2. Fill in `02_identity_and_rules/weekly_timetable.md` with your recurring commitments.
3. Fill in `02_identity_and_rules/profile_and_constraints.md` with your device battery windows and working hours.

### Step 3: Run Your First Daily Brain Dump
Type or dictate a raw, messy list of everything in your head:
```text
I have a test next Tuesday. I have a meeting today by 8:00 PM and another tomorrow by 7:00 PM. 
Then I have an assignment due next week. I need to stock up on groceries, call my parents, 
and spend 2 hours on my side project. Help me organize my day.
```

The assistant will:
1. Read your `weekly_timetable.md` to identify open time blocks.
2. Filter the tasks using `04_frameworks_decision_engines/eisenhower_matrix.md` into Q1 (Crisis), Q2 (Deep Work), Q3 (Admin), and Q4 (Eliminate).
3. Output a time-blocked execution plan.
4. Record your wins to `01_logs_operational_history/accountability_log.md`.

---

## Core Decision Frameworks Included

### 1. The Eisenhower Matrix (`04_frameworks_decision_engines/eisenhower_matrix.md`)
* **Q1 (Urgent & Important):** Crisis, hard deadlines, exams. Execute immediately.
* **Q2 (Not Urgent but Important):** Deep work, software architecture, skill acquisition. Protect dedicated calendar blocks.
* **Q3 (Urgent but Not Important):** Errands, shallow messages, routine check-ins. Batch into 30-minute low-energy windows.
* **Q4 (Not Urgent & Not Important):** Distractions, infinite scrolling, busywork. Eliminate ruthlessly.

### 2. The Idea Tank (`04_frameworks_decision_engines/idea_tank.md`)
Builders constantly get distracted by new ideas mid-week. The assistant intercepts unvetted ideas and parks them in `idea_tank.md` until the Sunday Weekly Review, keeping active focus blocks intact.

### 3. The Trophy Room & Graveyard (`01_logs_operational_history/accountability_log.md`)
* **Trophy Room:** Records concrete high-leverage wins achieved each day.
* **Graveyard:** Records missed tasks paired with an objective, emotion-free root-cause autopsy.

---

## Contributing & License

Feel free to fork this template, adapt it for your specific workflow, or submit improvements.

Released under the [MIT License](LICENSE).
