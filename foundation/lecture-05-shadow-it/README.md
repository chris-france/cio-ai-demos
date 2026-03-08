# Lecture 4 Demo — The Shadow IT Time Bomb

**Time:** ~7 minutes | **Tool:** Claude Code

## What This Proves

Somewhere in your organization, a $50M decision runs in a spreadsheet nobody has audited. Claude Code finds the risks in minutes.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to foundation/lecture-04-shadow-it. First run generate-workbook.py to create the sample Excel file (install openpyxl if needed). Then analyze sample-workbook.xlsx — this is a financial planning spreadsheet that a finance team has been using for years. Perform a full audit:
> 1. Map all sheets, their purposes, and cross-references
> 2. Find circular references, external links, and hardcoded values
> 3. Measure formula complexity (nesting depth, volatile functions)
> 4. Identify stale assumptions (check the 'last updated' dates)
> 5. Identify business logic that should be in a real application
> 6. Generate a risk-report.html in that folder with findings, severity ratings, and recommendations. Open it in my browser when done.

## Keep Going — Paste These Next

1. "Now convert the spreadsheet logic to a proper Python application with a web dashboard"
2. "Create a data flow diagram showing all cross-sheet dependencies"
3. "Write a monitoring script that alerts when assumptions are more than 6 months old"

## CIO Takeaway

> "Every finding in that report exists right now in your organization."
