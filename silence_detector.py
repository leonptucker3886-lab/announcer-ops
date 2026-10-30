#!/usr/bin/env python3
"""Silence detector: flags team members who go quiet or post status instead of work.
Input: JSON list of {"team","speaker","ts"(ISO),"message","has_file"(bool)}.
Usage: python silence_detector.py messages.json [--quiet-hours 3] [--min-daily 3]
"""
import json, sys, re, argparse
from datetime import datetime, timezone
from collections import defaultdict

STATUS = re.compile(r"\b(waiting on|standing by|copy|roger|will do|starting now|on it|ready when)\b", re.I)
WORK = re.compile(r"(https?://github\.com/\S+/commit/|```|\bcommit [0-9a-f]{7,}|\.pdf\b|\bdeployed\b|\bshipped\b)", re.I)

def classify(m):
    if m.get("has_file") or WORK.search(m.get("message", "")): return "work"
    if STATUS.search(m.get("message", "")): return "status"
    return "other"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("file")
    ap.add_argument("--quiet-hours", type=float, default=3); ap.add_argument("--min-daily", type=int, default=3)
    a = ap.parse_args(); msgs = json.load(open(a.file)); now = datetime.now(timezone.utc)
    last = {}; counts = defaultdict(lambda: defaultdict(int)); daily = defaultdict(int)
    for m in msgs:
        t = datetime.fromisoformat(m["ts"].replace("Z", "+00:00")); k = (m["team"], m["speaker"])
        last[k] = max(last.get(k, t), t); c = classify(m); counts[k][c] += 1
        if c == "work" and t.date() == now.date(): daily[m["team"]] += 1
    print("== SILENCE ==")
    for (team, sp), t in sorted(last.items()):
        h = (now - t).total_seconds() / 3600
        if h >= a.quiet_hours: print(f"{team} | {sp} | quiet {h:.1f}h")
    print("== STATUS-OVER-WORK ==")
    for (team, sp), c in sorted(counts.items()):
        if c["status"] > c["work"]: print(f"{team} | {sp} | status {c['status']} vs work {c['work']}")
    print("== DAILY OUTPUT ==")
    for team in sorted({k[0] for k in last}):
        n = daily[team]; print(f"{team} | {n}/{a.min_daily} {'OK' if n >= a.min_daily else 'SHORT'}")

if __name__ == "__main__": main()
