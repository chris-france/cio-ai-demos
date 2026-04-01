# Lecture 1 Demo — Monitoring is Not Observability

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

90% of infrastructure alerts are noise. This dashboard analyzes 90 days of real-world alert data to show the staggering false positive rate, the cost of alert fatigue, and exactly which rules need to be replaced with AI-driven baselines.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-04-infra-ops/lecture-01-alert-noise. Read the alert data. Generate an alert-noise analysis dashboard showing: pie chart of real vs noise, alerts by category and time of day, top 20 noisiest rules with false positive rates, and KPIs for total alerts, false positive rate, mean time to acknowledge, and alert fatigue index. Open in browser.

## Keep Going — Paste These Next

1. "Calculate the annual cost of alert fatigue assuming $85/hour blended ops rate"
2. "Recommend which 5 alert rules to eliminate first and what to replace them with"
3. "Draft a proposal to the VP of Ops explaining why we need to move from threshold-based monitoring to AI-driven observability"

## CIO Takeaway

> "Your ops team is spending 312 hours per quarter acknowledging alerts that mean nothing. That's $26,520 in wasted labor — plus the real incidents getting buried in the noise. AI-driven baselines eliminate 90% of this waste on day one."
