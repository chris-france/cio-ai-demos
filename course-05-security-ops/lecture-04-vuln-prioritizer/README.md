# Lecture 4 Demo — Vulnerability Management

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

AI turns a 500-item vulnerability scan from a panic-inducing list into an actionable, prioritized remediation plan by factoring in exploitability, asset exposure, and business impact — not just CVSS scores. You stop patching randomly and start patching strategically.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-05-security-ops/lecture-04-vuln-prioritizer. Build an AI Vulnerability Prioritizer. Generate 50 real CVEs from a simulated Nessus scan. For each: CVE ID, description, CVSS score, exploitability (Active/PoC/Theoretical), asset exposure (Internet/Internal/N/A), business impact, and an AI-calculated priority score. Create index.html with a sortable table, severity distribution chart, scatter plot of CVSS vs AI priority, and remediation timeline. Open in browser.

## Keep Going — Paste These Next

1. "Group these vulnerabilities into change windows and generate patch deployment tickets"
2. "For the top 5, generate compensating controls we can deploy today while waiting for patch windows"
3. "Create a weekly vulnerability trend report showing risk reduction over time"

## CIO Takeaway

> "You have 500 vulnerabilities. Only 3 will actually get you breached. AI finds those 3 so your team stops drowning in noise and starts eliminating real risk."
