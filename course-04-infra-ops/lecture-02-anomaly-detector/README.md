# Lecture 2 Demo — AI Anomaly Detection

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

Static threshold monitoring (CPU > 80% = alert) generates 89% false positives because it has zero context. AI anomaly detection learns what "normal" looks like for each system — backup windows, business hours, deploy patterns — and only alerts when something genuinely deviates from the learned baseline.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-04-infra-ops/lecture-02-anomaly-detector. Generate a side-by-side anomaly detection comparison dashboard. Left panel: traditional threshold monitoring showing 47 alerts (most false). Right panel: AI-filtered view showing only 5 real anomalies. Include a time-series chart with CPU data and threshold line, plus a scoring table for each anomaly. Open in browser.

## Keep Going — Paste These Next

1. "Show me what the AI's 14-day learning period looks like — what patterns does it discover?"
2. "Calculate the cost difference between investigating 47 alerts vs 5 real anomalies per week"
3. "Generate a rollout plan for deploying AI anomaly detection across our 200-server fleet"

## CIO Takeaway

> "Your on-call engineer is being paged 47 times a week for a threshold that someone set three years ago. AI learned in 14 days what that threshold never could — context. The result: 5 actionable alerts instead of 47 interruptions."
