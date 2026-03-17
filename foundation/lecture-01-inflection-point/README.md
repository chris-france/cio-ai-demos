# Lecture 1 Demo — The AI Inflection Point

**Time:** ~5 minutes | **Tool:** Claude Code

## What This Proves

You describe a business need in plain English. A board-ready dashboard appears. No commands, no coding, no developer ticket.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to foundation/lecture-01-inflection-point.
>
> I'm a new CIO and I need to audit our backup routines for all mission-critical data. Build me a Backup Audit Dashboard as a single index.html file using Tailwind CSS and Chart.js from CDN (no build step).
>
> Generate realistic test data for about 14 enterprise systems — things like SAP ERP, Salesforce CRM, Oracle HCM, SQL Server for financials, a data lake, a data warehouse, Active Directory, email, etc. Each system needs: data store type, environment, backup method, schedule, RPO and RTO targets, last backup time, status (Success/Warning/Failed), backup size, retention policy, and compliance tags like SOX, HIPAA, PCI-DSS, GDPR. Make 2-3 systems overdue or failed so the dashboard shows real risk.
>
> I want to see: KPI cards across the top (total systems, success rate, overdue count, total storage, RPO compliance percentage), a sortable searchable status table with color-coded status badges, a line chart showing backup success rate over the last 30 days, a bar chart showing storage consumed by system, a compliance coverage matrix so I can spot gaps, and an acronym glossary defining every acronym you use.
>
> White background, vibrant colors that pop, executive-ready look. When you're done, open it in my browser.

That's it. CC builds the entire dashboard and opens it for you.

## Keep Going — Paste These Next

1. "Add a filter dropdown so I can view systems by compliance framework — show me only SOX-tagged systems"
2. "Add an alert panel at the top that flags the 3 highest-risk systems with a recommended action for each"
3. "Export the dashboard data as a CSV report I can email to my IT director"

## CIO Takeaway

> "This is the inflection point. You described a business need and a board-ready dashboard appeared. No developer ticket, no two-week sprint, no vendor demo."
