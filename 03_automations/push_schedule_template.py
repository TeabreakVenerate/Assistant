#!/usr/bin/env python3
"""
Template script: Parsing task_calendar.md and preparing events for calendar sync.
"""

import os
import re

CALENDAR_FILE = os.path.join(os.path.dirname(__file__), "..", "01_logs_operational_history", "task_calendar.md")

def parse_schedule():
    if not os.path.exists(CALENDAR_FILE):
        print(f"Calendar file not found at: {CALENDAR_FILE}")
        return []
    
    with open(CALENDAR_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    print("Found calendar content. Scanning for scheduled blocks...")
    blocks = re.findall(r"- \*\*(.*?)\*\*:(.*)", content)
    for time_range, task in blocks:
        print(f"  [PARSED] {time_range.strip()} -> {task.strip()}")
    
    return blocks

if __name__ == "__main__":
    print("--- Local Schedule Parser (Dry Run) ---")
    events = parse_schedule()
    print(f"Total events ready for calendar sync: {len(events)}")
