# Lecture 6 Demo — SLA Prediction and Breach Prevention

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

AI can predict which tickets will breach their SLA hours before it happens. The dashboard color-codes 20 active tickets by risk level (green/yellow/red), shows breach probability, and demonstrates automatic actions the AI takes to prevent breaches — reassigning agents, boosting priority, and notifying team leads.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-03-service-mgmt/lecture-06-sla-prediction.
>
> Build me an SLA prediction dashboard as a single index.html using Tailwind CSS and Chart.js. Show 20 active tickets, each with: ticket ID, category, priority, current age in hours, SLA deadline, AI-predicted resolution time, time remaining, breach probability percentage, and risk level (green/yellow/red). Color-code rows by risk. Make imminent breach rows pulse red. Include KPI cards, a risk filter dropdown, sortable columns, a bar chart showing average breach probability by category, and a 30-day SLA performance line chart. Show what AI action is being taken for each risk level.

## Keep Going — Paste These Next

1. "Add a workload balance panel — show which agents are overloaded and suggest redistributing at-risk tickets to available agents"
2. "Add automatic SLA adjustment recommendations — which categories need longer SLAs based on historical performance?"
3. "Show me the cost of each prevented breach — calculate penalty fees and customer impact"

## CIO Takeaway

> "You're not managing SLAs if you find out about breaches after they happen. This dashboard predicts them hours in advance and takes action automatically. That's the difference between reactive and proactive operations."
