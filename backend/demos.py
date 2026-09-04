"""Demo data for all lectures."""

from __future__ import annotations
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

FOUNDATION_DEMOS = [
    {
        "num": "1",
        "title": "The AI Inflection Point",
        "subtitle": "Watch Claude Code build an enterprise backup dashboard from a single prompt",
        "tool": "Claude Code",
        "time": "~5 min",
        "folder": "foundation/lecture-01-inflection-point",
        "description": (
            "You paste one prompt describing what a new CIO needs to audit backup "
            "routines. Claude Code builds a complete interactive dashboard with KPI "
            "cards, sortable tables, charts, a compliance matrix, and a glossary — "
            "all in a single HTML file. You never type a command. This is the moment "
            "it clicks."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below — that's it, CC does everything else",
            "Watch CC build the entire dashboard from scratch",
            "CC opens the dashboard in your browser — explore the tables, charts, and filters",
            "Keep going — paste the follow-up prompts below to add features live",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-01-inflection-point.\n\n"
            "I'm a new CIO and I need to audit our backup routines for all mission-critical "
            "data. Build me a Backup Audit Dashboard as a single index.html file using "
            "Tailwind CSS and Chart.js from CDN (no build step).\n\n"
            "Generate realistic test data for about 14 enterprise systems — things like "
            "SAP ERP, Salesforce CRM, Oracle HCM, SQL Server for financials, a data lake, "
            "a data warehouse, Active Directory, email, etc. Each system needs: data store "
            "type, environment, backup method, schedule, RPO and RTO targets, last backup "
            "time, status (Success/Warning/Failed), backup size, retention policy, and "
            "compliance tags like SOX, HIPAA, PCI-DSS, GDPR. Make 2-3 systems overdue or "
            "failed so the dashboard shows real risk.\n\n"
            "I want to see:\n"
            "- KPI cards across the top: total systems, success rate, overdue count, "
            "total storage, RPO compliance percentage\n"
            "- A sortable, searchable status table with color-coded status badges and "
            "red-highlighted rows for RPO breaches\n"
            "- A line chart showing backup success rate over the last 30 days\n"
            "- A bar chart showing storage consumed by system\n"
            "- A compliance coverage matrix so I can spot gaps\n"
            "- An acronym glossary — define every acronym you use\n\n"
            "White background, vibrant colors that pop, executive-ready look. "
            "When you're done, open it in my browser."
        ),
        "takeaway": (
            "This is the inflection point. You described a business need in plain English "
            "and a board-ready dashboard appeared. No developer ticket, no two-week sprint, "
            "no vendor demo. This changes everything about how technology gets built."
        ),
        "followups": [
            "Add a filter dropdown so I can view systems by compliance framework — show me only SOX-tagged systems",
            "Add an alert panel at the top that flags the 3 highest-risk systems with a recommended action for each",
            "Export the dashboard data as a CSV report I can email to my IT director",
        ],
    },
    {
        "num": "2",
        "title": "LLMs Demystified",
        "subtitle": "See the difference between small and large models with your own eyes",
        "tool": "Claude Code + Ollama",
        "time": "~10 min",
        "folder": "foundation/lecture-02-llm-demystified",
        "description": (
            "You paste one prompt. Claude Code installs Ollama, pulls a small model "
            "and a medium model, runs the same prompt on both, and shows you the "
            "difference in speed, quality, and resource usage. You'll understand "
            "parameters, inference, and the cost tradeoff every CIO needs to know."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "At least 8GB RAM (for running small local models)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "Watch CC install Ollama and pull two models of different sizes",
            "CC runs the same prompt on both and compares speed, quality, and resource usage",
            "Paste follow-up prompts to explore larger models and cost questions",
        ],
        "cc_prompt": (
            "I want to understand LLMs hands-on. Here's what I need:\n"
            "1. Check if Ollama is installed on my machine. If not, install it.\n"
            "2. Pull two models: a small one (llama3.2:1b) and a medium one "
            "(llama3.2:3b).\n"
            "3. Run the exact same prompt on both: \"Explain cloud computing to a "
            "CEO in 3 sentences.\"\n"
            "4. Show me the results side by side — the response text, how long each "
            "took, and tokens per second.\n"
            "5. Show me how much memory and disk each model uses.\n"
            "6. Now run a harder prompt on both: \"Write a 90-day IT modernization "
            "plan for a mid-size company. Include milestones, risks, and budget "
            "considerations.\"\n"
            "7. Compare the quality of both responses and explain the tradeoff "
            "between model size, speed, cost, and quality in plain CIO language "
            "— no data science jargon.\n"
            "8. Save your comparison results to the course workbook by sending a PUT "
            "request to http://localhost:18801/api/workbook/2/llm_comparison with the "
            "data as JSON. Format: {\"data\": [{\"model\": \"...\", \"provider\": \"...\", "
            "\"parameters\": \"...\", \"monthly_cost\": \"...\", \"speed\": \"...\", "
            "\"quality\": N, \"best_use\": \"...\", \"data_leaves\": \"Yes/No\"}, ...]}. "
            "Include all models you tested plus the major cloud models (Claude, GPT-4, Gemini)."
        ),
        "takeaway": (
            "You don't need to be a data scientist. But you need to know enough to "
            "call BS when a vendor says their model is 'enterprise-grade.' After this "
            "demo, you can."
        ),
        "followups": [
            "Now pull a larger model like llama3.1:8b and run the same hard prompt. Show me how quality improves with size.",
            "Explain the difference between training and inference. What does each cost? Which one am I paying for when I use Claude or ChatGPT?",
            "If I wanted to run AI locally so no data leaves my building, what hardware would I need? Give me a budget for small, medium, and enterprise setups.",
            "Open the CIO AI Demos app at http://localhost:18802, go to the Workbook tab, and expand Lecture 2. Verify your comparison data was saved. Add any models you want to research further.",
        ],
    },
    {
        "num": "3",
        "title": "Finding Your $250K Moment",
        "subtitle": "AI builds a cost displacement dashboard from your vendor data",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "foundation/lecture-03-250k-moment",
        "description": (
            "Your workbook has vendor invoices pre-loaded with sample data. You paste one "
            "prompt. Claude Code reads your vendor data, classifies each into the Four-Zone "
            "Framework (Quick Win, Strategic, Optimize, Keep), builds an interactive "
            "dashboard with a quadrant visualization, and highlights your biggest AI "
            "displacement opportunity — the $250K moment hiding in your budget."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
            "CIO AI Demos app running (for workbook data)",
        ],
        "steps": [
            "First, open http://localhost:18802 and go to the Workbook tab",
            "Expand Lecture 3 — review the sample vendor data (or replace with your own)",
            "Open any terminal and type: claude",
            "Paste the prompt below — CC reads your workbook data and builds the dashboard",
            "Explore the Four-Zone quadrant chart and displacement recommendations",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-03-250k-moment.\n\n"
            "First, fetch my vendor invoice data from the course workbook API:\n"
            "curl -s http://localhost:18801/api/workbook/3/vendor_invoices\n\n"
            "Use this data to "
            "Build a Four-Zone Cost Displacement Dashboard as a single index.html file "
            "using Tailwind CSS and Chart.js from CDN (no build step):\n\n"
            "1. Parse all vendor invoices with their annual costs, categories, and zones\n"
            "2. Create a 2x2 quadrant scatter chart — X axis: Annual Cost, Y axis: "
            "AI Displacement Potential. Plot each vendor as a labeled bubble sized by cost\n"
            "3. Color code by zone: Quick Win (green), Strategic (blue), Optimize (amber), "
            "Keep (gray)\n"
            "4. Add KPI cards: Total Annual Spend, Quick Win Savings (sum of Quick Win "
            "vendors), Biggest Single Opportunity, Number of Displacement Candidates\n"
            "5. Add a sortable table of all vendors with zone, cost, and a recommendation "
            "column explaining WHY each is in its zone and what to do about it\n"
            "6. Highlight the single biggest displacement opportunity with a callout box: "
            "'YOUR $250K MOMENT' — explain the savings potential\n"
            "7. Add an executive summary paragraph at the top\n\n"
            "White background, vibrant colors, executive-ready. Open it in my browser."
        ),
        "takeaway": (
            "Every organization has a $250K moment hiding in plain sight. You just used AI "
            "to find it in 5 minutes. The audit tool that found the savings was itself "
            "built by AI — for about $0.15 in inference costs."
        ),
        "followups": [
            "Generate a one-page executive memo I can send to the CFO recommending we cut the top 3 Quick Win vendors. Include the dollar amounts and what replaces each one.",
            "Add a timeline view showing which vendor contracts expire in the next 12 months — I want to know which renewals to challenge first",
            "Create a risk assessment for each Quick Win displacement — what could go wrong and what's the mitigation plan?",
        ],
    },
    {
        "num": "4",
        "title": "Legacy Code is Not a Dead End",
        "subtitle": "Watch Claude Code convert a 1985 COBOL program to modern Python in minutes",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "foundation/lecture-04-legacy-code",
        "description": (
            "You paste one prompt. Claude Code finds a real COBOL accounting program "
            "on your machine, reads it, understands the business logic, converts it to "
            "clean Python with type hints, writes unit tests, adds a REST API, and runs "
            "the tests to prove it works. You don't touch a single file."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "Watch CC find the COBOL file, convert it, write tests, and run them",
            "CC reports the test results — all should pass",
            "Paste follow-up prompts to add more features",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-04-legacy-code and read accounting.cob. This is a "
            "COBOL accounting system from 1985 with view balance, credit, and debit "
            "operations. Convert it to modern Python in that same folder with:\n"
            "1. A clean Account class with type hints\n"
            "2. All original functionality preserved (balance check, credit, debit, "
            "transaction limits, account status enforcement)\n"
            "3. Unit tests in test_accounting.py that verify each operation\n"
            "4. A simple Flask REST API in api.py with endpoints for "
            "/balance, /credit, /debit\n"
            "Install any packages you need. Run the tests and tell me the results."
        ),
        "takeaway": (
            "Code nobody has touched for 40 years just became a modern web service in "
            "5 minutes. Your IBM rep will tell you this is impossible. Show them this demo."
        ),
        "followups": [
            "Add a /transactions endpoint that returns the last 10 transactions for an account",
            "Add JWT authentication to the API",
            "Generate Swagger API documentation and open it in my browser",
        ],
    },
    {
        "num": "5",
        "title": "The Shadow IT Time Bomb",
        "subtitle": "Claude Code audits a complex spreadsheet and finds the risks nobody knew about",
        "tool": "Claude Code",
        "time": "~7 min",
        "folder": "foundation/lecture-05-shadow-it",
        "description": (
            "Somewhere in your organization, a $50M decision runs in a spreadsheet nobody "
            "has audited. You paste one prompt. Claude Code finds the workbook on your "
            "machine, analyzes every sheet, discovers hardcoded values, stale assumptions, "
            "cross-sheet dependency chains, nested formulas — then generates an HTML risk "
            "report and opens it for you."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below — CC handles everything",
            "Watch CC generate the sample workbook, then analyze every sheet and formula",
            "CC generates risk-report.html and opens it in your browser",
            "Paste follow-up prompts to go deeper",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-05-shadow-it. First run generate-workbook.py to create "
            "the sample Excel file (install openpyxl if needed). Then analyze "
            "sample-workbook.xlsx — this is a financial planning spreadsheet that a "
            "finance team has been using for years. Perform a full audit:\n"
            "1. Map all sheets, their purposes, and cross-references\n"
            "2. Find circular references, external links, and hardcoded values\n"
            "3. Measure formula complexity (nesting depth, volatile functions)\n"
            "4. Identify stale assumptions (check the 'last updated' dates)\n"
            "5. Identify business logic that should be in a real application\n"
            "6. Generate a risk-report.html in that folder with findings, severity "
            "ratings, and recommendations. Open it in my browser when done."
        ),
        "takeaway": (
            "Every finding in that report exists right now in your organization. The question "
            "isn't whether you have shadow IT — it's whether you discover the risks before "
            "they discover you."
        ),
        "followups": [
            "Now convert the spreadsheet logic to a proper Python application with a web dashboard",
            "Create a data flow diagram showing all cross-sheet dependencies",
            "Write a monitoring script that alerts when assumptions are more than 6 months old",
            (
                "DEMO 2 — Shadow IT Triage Dashboard:\n"
                "Fetch my shadow IT inventory from the course workbook API:\n"
                "curl -s http://localhost:18801/api/workbook/5/shadow_it\n\n"
            "Use this data to "
                "Build a Shadow IT Triage Dashboard as shadow-it-triage.html in the "
                "foundation/lecture-05-shadow-it folder:\n"
                "1. Risk score each item (0-100) based on data sensitivity and business criticality\n"
                "2. Create a risk matrix scatter chart — X: Business Criticality, Y: Data Sensitivity, "
                "bubble size = risk score\n"
                "3. Color code: red (Migrate immediately), amber (Monitor closely), green (Acceptable risk)\n"
                "4. Add a prioritized action table sorted by risk score with recommended triage action\n"
                "5. Add KPI cards: Total Shadow Systems, Critical Risk Count, Estimated Migration Effort\n"
                "6. Executive summary paragraph at top\n\n"
                "White background, vibrant colors. Open it in my browser."
            ),
        ],
    },
    {
        "num": "6",
        "title": "The Death of Offshore Labor Arbitrage",
        "subtitle": "Claude Code completes a developer sprint ticket in 90 seconds",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "foundation/lecture-06-offshore-death",
        "description": (
            "There's a Flask app with no input validation — that's the sprint ticket. "
            "You paste one prompt. Claude Code finds the app on your machine, reads every "
            "file, installs dependencies, runs the existing tests, implements validation "
            "across multiple files, writes new tests, runs them, and reports results. "
            "A typical 2-hour offshore ticket done in 90 seconds."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below — this is your 'sprint ticket'",
            "Watch CC find the app, install deps, run tests, implement the feature",
            "CC runs the new tests and reports results — all should pass",
            "Paste follow-up prompts to keep building on the app",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-06-offshore-death. Read the entire codebase — this is a "
            "Flask user registration app. Install the requirements and run the existing "
            "tests to confirm they pass. Then implement this sprint ticket:\n\n"
            "TICKET: Add input validation to user registration\n"
            "- Email must be valid format (contains @ and a domain)\n"
            "- Password must be 8+ characters with at least one number\n"
            "- Username must be 3-20 characters, alphanumeric only\n"
            "- Show clear error messages on the registration form\n"
            "- Update existing tests and add new test cases for all validation rules\n\n"
            "Run all tests when done and report the results."
        ),
        "takeaway": (
            "That was a 2-hour offshore ticket at $40/hour. AI did it in 90 seconds "
            "for about $0.15. The math on labor arbitrage just broke permanently."
        ),
        "followups": [
            "Add a password strength meter to the registration form using JavaScript",
            "Add rate limiting — max 5 registration attempts per IP per minute",
            "Launch the app so I can test the registration form in my browser",
        ],
    },
    {
        "num": "7",
        "title": "Renegotiating Your SaaS Stack",
        "subtitle": "Claude Code builds a SaaS audit dashboard that shows where you're overpaying",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "foundation/lecture-07-saas-renegotiation",
        "description": (
            "Your workbook has your SaaS inventory pre-loaded. You paste one prompt. "
            "Claude Code reads your workbook data, calculates per-user costs, flags overpriced "
            "and underutilized tools, detects duplicates, suggests open-source alternatives, "
            "totals the savings, builds a complete HTML dashboard with charts, and opens it for you."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned (use the Master Setup prompt above)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "Watch CC fetch your workbook data, analyze it, build charts, generate the dashboard",
            "CC opens saas-audit.html in your browser",
            "Paste follow-up prompts to generate negotiation emails or consolidation plans",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "foundation/lecture-07-saas-renegotiation.\n\n"
            "Fetch my SaaS inventory from the course workbook API:\n"
            "curl -s http://localhost:18801/api/workbook/7/saas_audit\n\n"
            "Use this data to build a complete SaaS audit tool:\n"
            "1. Calculate cost per user per month for every tool\n"
            "2. Flag tools over $50/user/month as 'overpriced'\n"
            "3. Flag tools with under 40% utilization as 'underutilized'\n"
            "4. Detect overlapping tools (e.g., multiple project management or "
            "messaging tools)\n"
            "5. Suggest open-source alternatives for the top 5 most expensive tools\n"
            "6. Calculate total potential annual savings\n"
            "7. Generate a professional saas-audit.html dashboard in that folder with "
            "charts and a summary table\n"
            "Use pandas for analysis and matplotlib for charts — install if needed. "
            "Save charts as embedded base64 in the HTML. Open it in my browser when done."
        ),
        "takeaway": (
            "Every SaaS vendor assumed their tool was sticky. AI just gave you a credible "
            "alternative to half your stack — and the audit tool itself cost nothing to build."
        ),
        "followups": [
            "Write a negotiation email for the 3 worst-value contracts — firm but professional",
            "Create a renewal calendar showing which contracts expire in the next 6 months",
            "Build a consolidation roadmap — which tools to eliminate first and what replaces them",
        ],
    },
]

ADVANCED_DEMOS = [
    {
        "num": "8",
        "title": "Build vs Buy Just Changed",
        "subtitle": "Build a production AI app from scratch with Claude Code",
        "tool": "Claude Code + Ollama",
        "time": "~10 min",
    },
    {
        "num": "9",
        "title": "Leading Teams Through AI Disruption",
        "subtitle": "Build a skills gap analyzer for your team",
        "tool": "Claude Code",
        "time": "~7 min",
    },
    {
        "num": "10",
        "title": "AI Governance and IP Protection",
        "subtitle": "Scan an LLM for security vulnerabilities with Model Security Scanner",
        "tool": "Model Security Scanner",
        "time": "~8 min",
    },
    {
        "num": "11",
        "title": "Your 90-Day AI Leadership Roadmap",
        "subtitle": "Build a visual 90-day plan with Claude Code",
        "tool": "Claude Code",
        "time": "~8 min",
    },
    {
        "num": "12",
        "title": "Building Your AI-Era IT Team",
        "subtitle": "Build an AI-powered triage agent with local models",
        "tool": "Claude Code + Ollama",
        "time": "~8 min",
    },
    {
        "num": "13",
        "title": "AI Tools, Dependency, and Vendor Risk",
        "subtitle": "Compare LLM providers and benchmark for vendor independence",
        "tool": "Claude Code + Ollama",
        "time": "~8 min",
    },
]


SERVICE_MGMT_DEMOS = [
    {
        "num": "14",
        "title": "The Help Desk is Broken",
        "subtitle": "Build an analytics dashboard that reveals the real cost of your help desk",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "course-03-service-mgmt/lecture-01-helpdesk-broken",
        "description": (
            "Your workbook has 25 real support tickets. You paste one prompt. Claude Code "
            "fetches the data, calculates cost per ticket, resolution time distributions, "
            "category breakdowns, channel analysis, and builds a complete analytics dashboard "
            "that exposes exactly where your help desk is failing — and how much it costs."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "cio-ai-demos repo cloned",
            "CIO AI Demos app running (for workbook data)",
        ],
        "steps": [
            "Open http://localhost:18802 → Workbook tab → expand Lecture 14 to review ticket data",
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC fetches your ticket data and builds the analytics dashboard",
            "Explore the charts and cost analysis",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-01-helpdesk-broken.\n\n"
            "Fetch my help desk ticket data from the course workbook API:\n"
            "curl -s http://localhost:18801/api/workbook/14/helpdesk_tickets\n\n"
            "Also fetch my baseline metrics:\n"
            "curl -s http://localhost:18801/api/workbook/14/helpdesk_baseline\n\n"
            "Build a Help Desk Analytics Dashboard as index.html using Tailwind CSS and "
            "Chart.js from CDN (no build step):\n\n"
            "1. KPI cards: Total Tickets, Avg Resolution Time, SLA Compliance Rate, "
            "Cost Per Ticket (use $45/hour fully loaded IT staff rate), Open Tickets\n"
            "2. Bar chart: Tickets by category (Hardware, Software, Network, Access, Email)\n"
            "3. Pie chart: Tickets by channel (Slack, Teams, Email, Portal, Phone)\n"
            "4. Line chart: Resolution time distribution (how many tickets resolved in "
            "<15min, 15-60min, 1-4hr, 4-24hr, >24hr)\n"
            "5. Bar chart: Tickets by department — who generates the most work?\n"
            "6. Stacked bar: Charlotte vs Raleigh comparison\n"
            "7. Cost analysis box: Annual support cost, cost per ticket, projected cost "
            "of AI displacement (show 70% auto-resolution scenario)\n"
            "8. Sortable table of all tickets with color-coded priority and status badges\n\n"
            "White background, vibrant charts, executive-ready. Open in browser."
        ),
        "takeaway": (
            "Your help desk is a cost center you've been ignoring. Now you can see exactly "
            "where the money goes and which categories AI can displace. The 70% auto-resolution "
            "scenario you just saw? That's real. We'll build it in the next demo."
        ),
        "followups": [
            "Show me which tickets could have been auto-resolved by AI. Highlight them in the table with a green badge.",
            "Generate a one-page executive summary I can email to the CIO showing the cost of the status quo vs. AI help desk",
            "Add a recurring issues section — which problems keep coming back? What's the root cause?",
        ],
    },
    {
        "num": "15",
        "title": "AI Triage — How Machines Read Tickets",
        "subtitle": "Build a live ticket classifier that categorizes, prioritizes, and routes in real-time",
        "tool": "Claude Code + Ollama",
        "time": "~10 min",
        "folder": "course-03-service-mgmt/lecture-02-ai-triage",
        "description": (
            "You paste one prompt. Claude Code builds a web app where you type a ticket "
            "in plain English and watch AI classify it in real-time: category, priority, "
            "confidence score, suggested routing, and recommended response. You see exactly "
            "how AI reads and understands support tickets."
        ),
        "prerequisites": [
            "Claude Code installed with Claude Pro/Max subscription ($20/month)",
            "Ollama installed with at least one model (llama3.2:3b)",
            "cio-ai-demos repo cloned",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC builds the classifier app and launches it",
            "Type sample tickets and watch AI classify them in real-time",
            "Try edge cases — vague tickets, multi-issue tickets, urgent vs. routine",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-02-ai-triage.\n\n"
            "Build a live AI Ticket Classifier as a single-page web app (index.html + "
            "a small Python backend). The student types a support ticket in a text box "
            "and clicks 'Classify'. The AI returns:\n\n"
            "1. Category (Hardware, Software, Network, Access, Email, Other)\n"
            "2. Priority (Critical, High, Medium, Low) with reasoning\n"
            "3. Confidence score (0-100%) shown as a colored progress bar\n"
            "4. Suggested routing (which team or person should handle this)\n"
            "5. Suggested first response (what to say back to the employee)\n"
            "6. Keywords extracted from the ticket\n\n"
            "Use Ollama with llama3.2:3b as the AI backend. The prompt should include "
            "the classification taxonomy and examples. Parse the response as JSON.\n\n"
            "Pre-load 5 sample tickets as clickable buttons so students can see instant "
            "classifications:\n"
            "- 'My laptop screen is cracked'\n"
            "- 'VPN keeps disconnecting every 10 minutes'\n"
            "- 'Need access to the new SharePoint site for the airport project'\n"
            "- 'Outlook is sending duplicate emails to clients'\n"
            "- 'The entire Raleigh office lost internet'\n\n"
            "Professional UI with Tailwind CSS. Show the AI thinking process — display "
            "the raw prompt and response so students understand what's happening. "
            "Launch the backend on port 8850 and open the page in the browser."
        ),
        "takeaway": (
            "The AI didn't study ITIL. It didn't take a certification. You gave it a "
            "taxonomy and examples, and it classifies better than most L1 staff — in "
            "200 milliseconds. That's the triage revolution."
        ),
        "followups": [
            "Now send 10 tickets through the classifier at once (batch mode) and show me the results in a table",
            "Add a 'confidence threshold' slider — below the threshold, the ticket auto-escalates to a human instead of auto-classifying",
            "Compare classification quality between the small model (3b) and a larger model (8b). Which is more accurate? Is the speed tradeoff worth it?",
        ],
    },
    {
        "num": "16",
        "title": "Auto-Resolution — The 70% Rule",
        "subtitle": "Build a simulation showing which tickets AI resolves vs. escalates",
        "tool": "Claude Code + Ollama",
        "time": "~10 min",
        "folder": "course-03-service-mgmt/lecture-03-auto-resolution",
        "description": (
            "Your workbook tickets flow through an auto-resolution pipeline. AI classifies "
            "each one, checks confidence, and either resolves it autonomously (high confidence), "
            "drafts a response for human review (medium), or escalates with full context (low). "
            "You watch the 70% rule play out in real-time."
        ),
        "prerequisites": [
            "Claude Code installed",
            "Ollama installed with llama3.2:3b",
            "CIO AI Demos app running (for workbook data)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "Watch CC build the pipeline and process all 25 tickets",
            "See the dashboard showing auto-resolved vs. drafted vs. escalated",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-03-auto-resolution.\n\n"
            "Fetch ticket data: curl -s http://localhost:18801/api/workbook/14/helpdesk_tickets\n\n"
            "Build an Auto-Resolution Pipeline Simulator:\n\n"
            "1. For each ticket, use Ollama (llama3.2:3b) to:\n"
            "   - Classify the ticket\n"
            "   - Generate a confidence score (0-100)\n"
            "   - Generate a suggested resolution\n"
            "2. Apply the 70% rule:\n"
            "   - Confidence > 90%: AUTO-RESOLVED (green) — AI sends the response\n"
            "   - Confidence 60-90%: DRAFT FOR REVIEW (amber) — AI drafts, human approves\n"
            "   - Confidence < 60%: ESCALATE (red) — routed to human with full context\n"
            "3. Build a dashboard (index.html) showing:\n"
            "   - Animated pipeline: tickets flow through classification → resolution\n"
            "   - KPI cards: Total Processed, Auto-Resolved %, Drafted %, Escalated %\n"
            "   - Donut chart: resolution breakdown\n"
            "   - Table of all tickets with their AI decision, confidence, and suggested response\n"
            "   - Time saved calculation: auto-resolved tickets × avg resolution time × hourly rate\n"
            "   - Side-by-side comparison: 'Before AI' vs 'After AI' cost and staffing\n\n"
            "If Ollama is not available, use a rule-based classifier with realistic confidence "
            "scores as a fallback. The dashboard should still work without Ollama.\n\n"
            "Tailwind CSS, professional look. Open in browser."
        ),
        "takeaway": (
            "70% of your tickets just disappeared from the human queue. The remaining 30% "
            "arrive with full context — the AI already did the research. Your L1 team didn't "
            "lose their jobs; they got promoted to the interesting problems."
        ),
        "followups": [
            "Show me the tickets that were escalated — what made them hard? What would it take for AI to handle those too?",
            "Calculate the ROI: if we deploy this for real, what's the annual savings?",
            "Add a 'replay' button that lets me adjust the confidence thresholds and see how the percentages change",
        ],
    },
    {
        "num": "17",
        "title": "Knowledge Base That Builds Itself",
        "subtitle": "Watch AI turn resolved tickets into searchable KB articles",
        "tool": "Claude Code + Ollama",
        "time": "~8 min",
        "folder": "course-03-service-mgmt/lecture-04-knowledge-base",
        "description": (
            "You select a resolved ticket. AI reads the problem and solution, generates "
            "a clean KB article with title, steps, related articles, and search keywords. "
            "Then it builds a searchable knowledge base UI from all your resolved tickets."
        ),
        "prerequisites": [
            "Claude Code installed",
            "Ollama installed with llama3.2:3b",
            "CIO AI Demos app running",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC processes resolved tickets and generates KB articles",
            "Search the KB and see how it self-populates",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-04-knowledge-base.\n\n"
            "Fetch resolved tickets: curl -s http://localhost:18801/api/workbook/14/helpdesk_tickets\n\n"
            "Build a Self-Generating Knowledge Base:\n\n"
            "1. For each resolved ticket (status = Resolved), use Ollama to generate a KB article:\n"
            "   - Title (clear, searchable)\n"
            "   - Problem summary (1-2 sentences)\n"
            "   - Step-by-step solution\n"
            "   - Category and tags\n"
            "   - Related article suggestions\n"
            "2. Build a knowledge base web app (index.html):\n"
            "   - Search bar at the top (filters articles by keyword)\n"
            "   - Category filter sidebar\n"
            "   - Article cards with title, summary, and 'View Solution' expand\n"
            "   - A 'Generate from Ticket' demo: paste a ticket, click generate, see the article appear\n"
            "   - Stats: total articles, most viewed categories, articles generated today\n"
            "3. Include a before/after comparison:\n"
            "   - Before: 'Our KB has 12 articles from 2019. Nobody updates it.'\n"
            "   - After: 'Every resolved ticket automatically becomes a searchable article.'\n\n"
            "If Ollama unavailable, generate articles using templates based on ticket data.\n"
            "Tailwind CSS. Open in browser."
        ),
        "takeaway": (
            "Your knowledge base just went from 12 stale articles to a living system that "
            "grows with every resolved ticket. The next time someone has the same problem, "
            "AI finds the article before they even finish typing."
        ),
        "followups": [
            "Show me duplicate articles — tickets that generated the same KB article. How many tickets could have been self-served?",
            "Add a 'Did this help?' button to each article. Track which articles are most useful.",
            "Generate a monthly report: new articles created, most searched topics, gaps where articles are missing",
        ],
    },
    {
        "num": "18",
        "title": "Escalation Intelligence",
        "subtitle": "Build the 'talk to a human' flow with full context handoff",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "course-03-service-mgmt/lecture-05-escalation",
        "description": (
            "The 'Talk to a Human' button must always be visible. When clicked, AI hands off "
            "to a person with full context — what the user tried, what AI already attempted, "
            "relevant KB articles, and a suggested resolution. The human never asks the user "
            "to repeat themselves."
        ),
        "prerequisites": [
            "Claude Code installed",
            "cio-ai-demos repo cloned",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC builds the escalation flow simulator",
            "Walk through the experience as an employee submitting a ticket",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-05-escalation.\n\n"
            "Build a Smart Escalation Simulator (index.html) that shows the employee experience:\n\n"
            "1. LEFT PANEL — Employee View:\n"
            "   - Chat interface where the employee describes their problem\n"
            "   - AI responds with suggestions (simulate a conversation)\n"
            "   - Big green 'TALK TO A HUMAN' button — always visible, never hidden\n"
            "   - When clicked: 'Connecting you with Marcus from IT. He has your full context.'\n\n"
            "2. RIGHT PANEL — IT Staff View (what Marcus sees):\n"
            "   - Employee name, department, location\n"
            "   - Problem description\n"
            "   - What AI already tried (with results)\n"
            "   - Related KB articles\n"
            "   - AI's suggested resolution\n"
            "   - Priority and SLA countdown\n"
            "   - Employee's ticket history (past issues)\n\n"
            "3. BOTTOM — Metrics:\n"
            "   - Average escalation context score (how much info the human gets)\n"
            "   - Time saved vs. starting from scratch\n"
            "   - Employee satisfaction comparison: escalation WITH context vs WITHOUT\n\n"
            "Pre-load 3 scenarios the student can click through:\n"
            "- Password reset that AI solved (no escalation needed)\n"
            "- Projector issue that needs physical help (clean escalation)\n"
            "- Complex Revit crash that AI can't diagnose (full context handoff)\n\n"
            "Tailwind CSS. Split-screen layout. Open in browser."
        ),
        "takeaway": (
            "The difference between good AI support and terrible AI support is one button. "
            "The 'Talk to a Human' button must always be visible, never hidden, and when "
            "clicked, the human gets everything — not a cold transfer to someone who asks "
            "'can you describe the issue again?'"
        ),
        "followups": [
            "Add a 'frustrated employee' scenario where the user types 'THIS IS RIDICULOUS JUST LET ME TALK TO SOMEONE' — show how AI detects frustration and immediately escalates",
            "Show the same escalation WITHOUT context — the old way. How long does it take when the human starts from zero?",
            "Build a dashboard showing escalation patterns — which categories escalate most? What time of day? Which AI gaps should we fix?",
        ],
    },
    {
        "num": "19",
        "title": "SLA Prediction and Breach Prevention",
        "subtitle": "Build a dashboard that predicts SLA breaches before they happen",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "course-03-service-mgmt/lecture-06-sla-prediction",
        "description": (
            "SLA targets: Critical=2hr, High=4hr, Medium=24hr, Low=48hr. AI monitors every "
            "open ticket and predicts which ones will breach — before they do. Auto-reprioritizes "
            "and alerts the team before the clock runs out."
        ),
        "prerequisites": [
            "Claude Code installed",
            "cio-ai-demos repo cloned",
            "CIO AI Demos app running",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC builds the SLA prediction dashboard",
            "Watch the countdown timers and breach predictions in real-time",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-06-sla-prediction.\n\n"
            "Fetch ticket data: curl -s http://localhost:18801/api/workbook/14/helpdesk_tickets\n\n"
            "Build an SLA Prediction Dashboard (index.html):\n\n"
            "SLA targets: Critical=2hr, High=4hr, Medium=24hr, Low=48hr\n\n"
            "1. KPI cards: Open Tickets, At Risk (>75% of SLA elapsed), Breached, "
            "On Track, SLA Compliance Rate\n"
            "2. For each open/in-progress ticket, show:\n"
            "   - Countdown timer (time remaining before SLA breach)\n"
            "   - Risk score (green/amber/red based on elapsed %)\n"
            "   - Predicted breach time based on category avg resolution\n"
            "   - Auto-suggested action: reassign, escalate, or add resources\n"
            "3. Timeline chart: show when each ticket was submitted vs. when SLA expires\n"
            "4. Breach prediction: 'Based on current resolution patterns, 3 tickets will "
            "breach in the next 2 hours'\n"
            "5. Historical view: SLA compliance over the past 90 days by priority level\n"
            "6. Auto-reprioritization demo: button that reshuffles the queue to minimize "
            "total breaches\n\n"
            "Use JavaScript timers to make countdowns animate in real-time.\n"
            "Tailwind CSS. Open in browser."
        ),
        "takeaway": (
            "Traditional help desks measure SLA breaches after they happen. You just built "
            "a system that predicts them before they happen. The shift from reactive to "
            "predictive is the entire point of AI in service management."
        ),
        "followups": [
            "Add email/Slack alerts that fire when a ticket hits 80% of its SLA window",
            "Show me which IT staff members have the best SLA compliance — who should get the critical tickets?",
            "Build a 'what-if' simulator: if we add one more IT staff member, how does SLA compliance change?",
        ],
    },
    {
        "num": "20",
        "title": "Integrating with Your Stack",
        "subtitle": "Build a multi-channel ticket ingestion demo — Slack, Teams, email, and portal",
        "tool": "Claude Code",
        "time": "~7 min",
        "folder": "course-03-service-mgmt/lecture-07-multichannel",
        "description": (
            "Employees don't care about your ticketing system. They care about getting help "
            "where they already are — Slack, Teams, email, or a web portal. This demo shows "
            "tickets arriving from all four channels, normalized into a single unified queue."
        ),
        "prerequisites": [
            "Claude Code installed",
            "cio-ai-demos repo cloned",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC builds the multi-channel ingestion simulator",
            "Watch tickets arrive from different channels in real-time",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-07-multichannel.\n\n"
            "Build a Multi-Channel Ticket Ingestion Simulator (index.html):\n\n"
            "1. Four columns representing channels: Slack, Teams, Email, Web Portal\n"
            "   - Each column shows messages arriving in that channel's visual style\n"
            "   - Slack: purple sidebar, message bubbles\n"
            "   - Teams: blue header, conversation threads\n"
            "   - Email: inbox format with subject lines\n"
            "   - Portal: clean form submissions\n\n"
            "2. Center: Unified Ticket Queue\n"
            "   - All messages normalize into the same ticket format\n"
            "   - Each ticket shows: source channel icon, subject, category, priority, timestamp\n"
            "   - Sortable and filterable\n\n"
            "3. Animation: every 3 seconds, a new ticket arrives in a random channel, "
            "animates across to the unified queue, and gets classified\n\n"
            "4. Stats bar: Tickets per channel, avg response time per channel, "
            "which channel is fastest\n\n"
            "5. Key insight callout: 'Employees submit tickets where they're comfortable. "
            "AI meets them there. The system behind the scenes is the same regardless of channel.'\n\n"
            "Use JavaScript setInterval for the animation. Pre-load 20 realistic tickets "
            "from an AEC firm (mix of hardware, software, network, access issues).\n"
            "Tailwind CSS, vibrant, animated. Open in browser."
        ),
        "takeaway": (
            "The channel doesn't matter. What matters is that every message — whether it's "
            "a Slack DM, a Teams chat, an email, or a portal form — becomes the same ticket "
            "in the same queue with the same AI classification. Meet users where they are."
        ),
        "followups": [
            "Add a 'natural language' channel — let me type a ticket as if I'm texting a friend and watch AI parse it into structured fields",
            "Show me channel analytics: which departments prefer which channel? Is there a pattern?",
            "Add a chatbot interface that responds in-channel: when someone messages in Slack, the AI replies in Slack — not a ticketing portal",
        ],
    },
    {
        "num": "21",
        "title": "The Transition Plan",
        "subtitle": "Build an interactive ROI calculator and 90-day implementation roadmap",
        "tool": "Claude Code",
        "time": "~8 min",
        "folder": "course-03-service-mgmt/lecture-08-transition-plan",
        "description": (
            "The final demo: an interactive tool where you input your company's numbers — "
            "employees, IT staff, ticket volume, current costs — and get a personalized ROI "
            "projection plus a visual 90-day implementation roadmap. This is the tool you "
            "use to build the business case for your CIO."
        ),
        "prerequisites": [
            "Claude Code installed",
            "cio-ai-demos repo cloned",
            "CIO AI Demos app running (for workbook baseline data)",
        ],
        "steps": [
            "Open any terminal and type: claude",
            "Paste the prompt below",
            "CC builds the ROI calculator and roadmap",
            "Input your company's real numbers and see the projections",
        ],
        "cc_prompt": (
            "Find the cio-ai-demos repo on my machine. Inside it, go to "
            "course-03-service-mgmt/lecture-08-transition-plan.\n\n"
            "Fetch baseline data: curl -s http://localhost:18801/api/workbook/14/helpdesk_baseline\n\n"
            "Build an AI Help Desk ROI Calculator & Transition Roadmap (index.html):\n\n"
            "SECTION 1 — ROI Calculator:\n"
            "- Input sliders: Company Size (100-5000), IT Support Staff (1-50), "
            "Monthly Ticket Volume (50-2000), Avg IT Salary ($60K-$150K), "
            "Current MSP Cost (if any)\n"
            "- Auto-calculate: Current Annual Cost, AI Help Desk Cost, Annual Savings, "
            "ROI %, Payback Period (months)\n"
            "- Assumptions box: 70% auto-resolution, $45/hr loaded rate, 15-min avg AI resolution\n"
            "- Chart: 3-year projection showing cumulative savings vs. investment\n"
            "- Pre-populate with workbook baseline data\n\n"
            "SECTION 2 — 90-Day Implementation Roadmap:\n"
            "- Visual timeline with 3 phases:\n"
            "  Week 1-2: Foundation (tool selection, data import, KB seed)\n"
            "  Week 3-6: Pilot (1 department, 1 channel, measure auto-resolution rate)\n"
            "  Week 7-12: Scale (all departments, all channels, SLA tracking)\n"
            "- Each phase has: milestones, risks, success metrics\n"
            "- Gantt-style chart with clickable phases that expand to show details\n\n"
            "SECTION 3 — Executive Summary Generator:\n"
            "- Button: 'Generate Board Memo'\n"
            "- Takes the calculator inputs and generates a 1-page executive summary "
            "with the ROI case, implementation timeline, and risk mitigation\n"
            "- Copyable text that can be pasted into an email or document\n\n"
            "Tailwind CSS, professional, executive-ready. Open in browser."
        ),
        "takeaway": (
            "You now have everything you need to make the business case: the cost analysis, "
            "the implementation plan, the risk mitigation, and the executive memo. You built "
            "all of it with AI in 8 demos. That's the meta-lesson — the tools you built to "
            "analyze your help desk were themselves built by AI."
        ),
        "followups": [
            "Adjust the auto-resolution rate to 50% instead of 70%. How does the ROI change? What's the break-even rate?",
            "Add a risk assessment section: what are the top 5 risks of deploying AI help desk, and what's the mitigation for each?",
            "Generate a comparison table: current state vs. AI help desk vs. outsourced MSP. Three options for the board.",
        ],
    },
]


def get_demo_status(folder: str | None) -> str:
    """Return 'ready' if demo folder has real content."""
    if not folder:
        return "stub"
    demo_dir = PROJECT_ROOT / folder
    # Also check sibling directories (e.g., ai-inference-cost-calculator)
    if not demo_dir.exists():
        demo_dir = PROJECT_ROOT.parent / folder
    if not demo_dir.exists():
        return "stub"
    # Check for at least a README or data file beyond .gitkeep
    files = [f for f in demo_dir.iterdir() if f.name != '.gitkeep' and not f.name.startswith('.')]
    return "ready" if len(files) >= 2 else "stub"


def enrich_demos(demos: list[dict]) -> list[dict]:
    """Add status to each demo."""
    result = []
    for d in demos:
        enriched = {**d}
        enriched["status"] = get_demo_status(d.get("folder"))
        result.append(enriched)
    return result
