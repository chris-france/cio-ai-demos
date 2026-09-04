"""
Assumption Staleness Monitor

Checks all financial assumptions and alerts when any are older than 6 months.
Run manually, via cron, or as a scheduled job.

Usage:
    python3 monitor.py              # print report to terminal
    python3 monitor.py --json       # output JSON (for pipelines)
    python3 monitor.py --notify     # open HTML alert in browser if stale found
"""

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from dataclasses import dataclass


STALE_THRESHOLD_DAYS = 180  # 6 months


@dataclass
class Assumption:
    parameter: str
    value: float
    last_updated: date
    updated_by: str

    @property
    def age_days(self) -> int:
        return (date.today() - self.last_updated).days

    @property
    def age_label(self) -> str:
        years = self.age_days / 365.25
        if years >= 1:
            return f"{years:.1f} years"
        months = self.age_days / 30.44
        return f"{months:.0f} months"

    @property
    def is_stale(self) -> bool:
        return self.age_days > STALE_THRESHOLD_DAYS

    @property
    def severity(self) -> str:
        if self.age_days > 1460:  # 4 years
            return "CRITICAL"
        if self.age_days > 730:   # 2 years
            return "HIGH"
        if self.age_days > STALE_THRESHOLD_DAYS:
            return "WARNING"
        return "OK"


# The same data as app.py — in production, both would read from a shared database
ASSUMPTIONS = [
    Assumption("Tax Rate", 0.21, date(2022, 1, 15), "jsmith"),
    Assumption("Discount Rate", 0.08, date(2021, 6, 30), "UNKNOWN"),
    Assumption("Growth Target", 0.15, date(2023, 3, 1), "cfo_direct"),
    Assumption("Inflation Adj", 0.035, date(2020, 12, 1), "UNKNOWN"),
    Assumption("FX Rate EUR/USD", 1.08, date(2024, 2, 15), "treasury"),
    Assumption("Benefits Load", 0.30, date(2019, 8, 22), "hr_admin"),
    Assumption("Contingency %", 0.10, date(2021, 11, 1), "UNKNOWN"),
]


def run_check() -> dict:
    stale = [a for a in ASSUMPTIONS if a.is_stale]
    unknown = [a for a in ASSUMPTIONS if a.updated_by == "UNKNOWN"]
    oldest = max(ASSUMPTIONS, key=lambda a: a.age_days)

    return {
        "check_date": date.today().isoformat(),
        "threshold_days": STALE_THRESHOLD_DAYS,
        "total_assumptions": len(ASSUMPTIONS),
        "stale_count": len(stale),
        "unknown_author_count": len(unknown),
        "oldest": {"parameter": oldest.parameter, "age": oldest.age_label, "severity": oldest.severity},
        "status": "FAIL" if stale else "PASS",
        "findings": [
            {
                "parameter": a.parameter,
                "value": a.value,
                "last_updated": a.last_updated.isoformat(),
                "updated_by": a.updated_by,
                "age_days": a.age_days,
                "age_label": a.age_label,
                "severity": a.severity,
                "is_stale": a.is_stale,
            }
            for a in sorted(ASSUMPTIONS, key=lambda a: -a.age_days)
        ],
    }


def print_report(result: dict) -> None:
    status = result["status"]
    icon = "\033[91mFAIL\033[0m" if status == "FAIL" else "\033[92mPASS\033[0m"

    print(f"\n{'='*60}")
    print(f"  ASSUMPTION STALENESS MONITOR — [{icon}]")
    print(f"  Checked: {result['check_date']}  Threshold: {result['threshold_days']} days")
    print(f"{'='*60}\n")

    sev_colors = {
        "CRITICAL": "\033[91m",  # red
        "HIGH": "\033[93m",      # yellow
        "WARNING": "\033[33m",   # amber
        "OK": "\033[92m",        # green
    }
    reset = "\033[0m"

    for f in result["findings"]:
        sev = f["severity"]
        color = sev_colors.get(sev, "")
        stale_marker = " ← STALE" if f["is_stale"] else ""
        author_flag = " [UNKNOWN AUTHOR]" if f["updated_by"] == "UNKNOWN" else ""

        print(f"  {color}{sev:8s}{reset}  {f['parameter']:20s}  "
              f"value={f['value']:<8}  updated={f['last_updated']}  "
              f"age={f['age_label']:>10}{stale_marker}{author_flag}")

    print(f"\n  Summary: {result['stale_count']}/{result['total_assumptions']} stale, "
          f"{result['unknown_author_count']} unknown authors")
    print(f"  Oldest:  {result['oldest']['parameter']} ({result['oldest']['age']})\n")

    if result["status"] == "FAIL":
        print("  ACTION REQUIRED: Review and update stale assumptions.")
        print("  Dashboard: http://localhost:5055")
        print()


def show_browser_alert(result: dict) -> None:
    stale = [f for f in result["findings"] if f["is_stale"]]
    if not stale:
        print("All assumptions current — no alert needed.")
        return

    sev_colors = {"CRITICAL": "#dc2626", "HIGH": "#d97706", "WARNING": "#ca8a04", "OK": "#16a34a"}
    sev_bg = {"CRITICAL": "#fef2f2", "HIGH": "#fffbeb", "WARNING": "#fefce8", "OK": "#f0fdf4"}

    rows = "\n".join(
        f'<tr style="background:{sev_bg.get(f["severity"],"")}"><td style="padding:8px 12px;font-weight:600;">{f["parameter"]}</td>'
        f'<td style="padding:8px 12px;text-align:right;font-family:monospace;">{f["value"]}</td>'
        f'<td style="padding:8px 12px;">{f["last_updated"]}</td>'
        f'<td style="padding:8px 12px;{" color:#dc2626;font-weight:700;" if f["updated_by"]=="UNKNOWN" else ""}">{f["updated_by"]}</td>'
        f'<td style="padding:8px 12px;text-align:right;font-weight:700;color:{sev_colors.get(f["severity"],"#333")};">{f["age_label"]}</td>'
        f'<td style="padding:8px 12px;"><span style="background:{sev_colors.get(f["severity"],"#999")};color:white;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:700;">{f["severity"]}</span></td></tr>'
        for f in stale
    )

    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>ALERT: Stale Assumptions</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>*{{font-family:'Inter',sans-serif;}}body{{margin:0;padding:40px;background:#fef2f2;}}</style></head>
<body>
<div style="max-width:800px;margin:0 auto;background:white;border-radius:16px;border:2px solid #fca5a5;padding:32px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="width:48px;height:48px;border-radius:12px;background:#fef2f2;display:flex;align-items:center;justify-content:center;font-size:24px;">&#9888;</div>
<div><h1 style="margin:0;font-size:22px;color:#991b1b;">Stale Assumption Alert</h1>
<p style="margin:4px 0 0;font-size:13px;color:#6b7280;">{result["check_date"]} &mdash; {len(stale)} of {result["total_assumptions"]} assumptions exceed {result["threshold_days"]}-day threshold</p></div></div>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="background:#f9fafb;text-align:left;">
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;">Parameter</th>
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;text-align:right;">Value</th>
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;">Last Updated</th>
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;">Owner</th>
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;text-align:right;">Age</th>
<th style="padding:8px 12px;color:#6b7280;font-size:11px;text-transform:uppercase;">Severity</th></tr></thead>
<tbody>{rows}</tbody></table>
<div style="margin-top:20px;padding:16px;background:#fef2f2;border:1px solid #fca5a5;border-radius:8px;font-size:13px;">
<strong style="color:#991b1b;">Action Required:</strong> <span style="color:#374151;">Review each stale assumption with its owner. Update values, record the new date and author, and get CFO sign-off for any changes that affect financial reporting.</span></div>
<p style="margin-top:16px;font-size:11px;color:#9ca3af;text-align:center;">Generated by monitor.py &mdash; CIO AI Curriculum, Lecture 05</p>
</div></body></html>"""

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        path = f.name

    subprocess.run(["open", path])
    print(f"Alert opened in browser: {path}")


def main():
    parser = argparse.ArgumentParser(description="Assumption Staleness Monitor")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--notify", action="store_true", help="Open browser alert if stale found")
    args = parser.parse_args()

    result = run_check()

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    if args.notify:
        show_browser_alert(result)

    sys.exit(1 if result["status"] == "FAIL" else 0)


if __name__ == "__main__":
    main()
