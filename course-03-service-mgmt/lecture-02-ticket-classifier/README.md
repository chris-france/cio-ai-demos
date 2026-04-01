# Lecture 2 Demo — AI Triage: How Machines Read Tickets

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

AI classifies tickets by understanding intent, not matching keywords. The demo shows 10 real-world tickets classified in real time with category, confidence score, priority, and reasoning — demonstrating why NLP-based triage is fundamentally different from rules-based routing.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-03-service-mgmt/lecture-02-ticket-classifier.
>
> Build me an AI ticket classifier demo as a single index.html using Tailwind CSS and Chart.js. Show 10 realistic help desk tickets being classified in real time. Each ticket should show: the original text, the AI-assigned category, a confidence score with a visual bar, the priority level, and a one-line reasoning explanation. Include a "Classify All Tickets" button that animates through the tickets one by one. Add summary cards showing total classified, average confidence, and processing time. After classification, show a bar chart of category distribution and a confidence score chart.

## Keep Going — Paste These Next

1. "Add a comparison column showing what a keyword-based system would have classified each ticket as — highlight the mismatches"
2. "Let me type a custom ticket in a text box and classify it on the fly"
3. "Show the confusion matrix — which categories does the AI mix up most often?"

## CIO Takeaway

> "Keyword routing sends 'I changed my password and now VPN won't connect' to the wrong queue. NLP reads the intent and routes it correctly the first time. That's the difference between a rules engine and intelligence."
