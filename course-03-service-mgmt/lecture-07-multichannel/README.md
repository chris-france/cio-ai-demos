# Lecture 7 Demo — Multi-Channel Ingestion

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

Your users don't pick one channel. They email on Monday, Slack on Tuesday, and submit a web form on Wednesday. The AI meets them everywhere and feeds every request into the same classification engine. Channel doesn't matter — the experience is identical.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-03-service-mgmt/lecture-07-multichannel.
>
> Build me a multi-channel ingestion demo as a single index.html using Tailwind CSS and Chart.js. Three-column layout showing tickets arriving from Email, Slack, and Web Portal simultaneously with animated message bubbles. Below that, a unified queue table showing all tickets merged with source channel badges, AI category, priority, and status (auto-resolved vs assigned). Include a "Start Live Simulation" button that feeds 12 tickets through the channels one at a time. Add KPI cards for total ingested, per-channel counts, and auto-resolved count. Include a channel distribution pie chart and a response time comparison chart (traditional vs AI-powered by channel).

## Keep Going — Paste These Next

1. "Add a phone/voicemail channel that transcribes calls and creates tickets automatically"
2. "Show duplicate detection — when the same user sends the same issue via email AND Slack, merge them into one ticket"
3. "Add a sentiment score to each message — flag angry or frustrated users for priority handling"

## CIO Takeaway

> "Your AI help desk can't live on a portal nobody visits. Wire it into Slack, email, and every tool your users already use. One brain, every channel — that's how you get adoption on day one."
