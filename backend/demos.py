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
