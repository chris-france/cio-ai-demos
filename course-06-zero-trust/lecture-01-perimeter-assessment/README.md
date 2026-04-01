# Lecture 1 Demo — Beyond the Perimeter

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

Your network perimeter is an illusion. This dashboard inventories every entry point — VPN gateways, cloud endpoints, partner links, legacy FTP servers — scores each for risk, and reveals how many are unaudited, using legacy auth, or completely invisible to your security team.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-06-zero-trust/lecture-01-perimeter-assessment.
>
> I need to assess our network perimeter for zero trust readiness. Build me a Perimeter Assessment Dashboard as a single index.html using Tailwind CSS and Chart.js from CDN. Include KPI cards for total entry points, high-risk items, unaudited endpoints, legacy auth methods, and zero trust score. Add a stacked bar chart by zone (DMZ, Cloud, Remote, Partner), an exposure trend line chart, and a sortable risk table with 15 entry points showing zone, protocol, ports, auth method, last audit date, and risk score. Flag anything over 80 in red. Add a critical findings section.

## Keep Going — Paste These Next

1. "Add a remediation priority list — for each critical finding, suggest the specific zero trust control that would reduce the risk"
2. "Create a network diagram showing all entry points grouped by zone with risk color coding"
3. "Generate a 90-day action plan to close the top 5 gaps"

## CIO Takeaway

> "Your firewall gives you a false sense of security. This dashboard shows every way into your network — and how many of those doors are wide open. Zero trust starts with knowing what you're protecting."
