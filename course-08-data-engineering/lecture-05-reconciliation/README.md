# Lecture 5 Demo — Cross-System Reconciliation

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

When the same data lives in multiple systems, discrepancies are inevitable. This dashboard compares records across system pairs, calculates match rates, and flags failures — catching the data drift that leads to incorrect reports.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-08-data-engineering/lecture-05-reconciliation.
>
> Build me a Data Reconciliation Dashboard as a single index.html using Tailwind CSS and Chart.js from CDN. Compare 8 system pairs, show match rates, discrepancy counts, and pass/warn/fail status.

## Keep Going — Paste These Next

1. "Drill into the Legacy Oracle vs Snowflake failure — show me the specific records that don't match"
2. "Build an automated reconciliation scheduler that runs these checks every night"
3. "Calculate the business risk of each discrepancy — which mismatches affect financial reporting?"

## CIO Takeaway

> "If your CRM says 4,280 customers and your warehouse says 4,275, which number goes in the board report? Automated reconciliation answers that question before anyone asks it."
