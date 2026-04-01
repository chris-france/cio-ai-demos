# Lecture 1 Demo — The Help Desk is Broken

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

You can build a complete help desk analytics dashboard from a plain-English description. The dashboard exposes the exact pain points from the lecture — high cost per ticket, low CSAT, overloaded agents — giving a CIO immediate visibility into why the traditional help desk model is failing.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-03-service-mgmt/lecture-01-helpdesk-analytics.
>
> I run IT for a 200-person company and my help desk is struggling. Build me an analytics dashboard as a single index.html using Tailwind CSS and Chart.js from CDN.
>
> I need: KPI cards showing total tickets (about 1,200/month), average resolution time (over 4 hours), cost per ticket ($22), CSAT score (3.2/5 — bad), and agent utilization (94% — way too high). Add a line chart showing daily ticket volume vs resolved over 30 days, a doughnut chart breaking down tickets by category (password resets, software installs, hardware, network/VPN, email, printing, other), and an agent performance table with 10 agents across L1/L2/L3 showing tickets resolved, avg resolution time, CSAT, utilization, and reopen rate. Make it sortable and filterable by tier. Flag overloaded agents in red.

That's it. CC builds the dashboard and opens it for you.

## Keep Going — Paste These Next

1. "Add a trend sparkline to each KPI card showing the last 12 weeks"
2. "Highlight any agent with a reopen rate above 5% and add a tooltip explaining why that matters"
3. "Add a section showing estimated annual cost — multiply tickets by cost per ticket and show what 50% automation would save"

## CIO Takeaway

> "Before you can fix the help desk, you need to see how broken it is. This dashboard shows the five numbers every CIO should track — and it took eight minutes to build, not eight weeks."
