"""Workbook form definitions per lecture.

CIOs: customize this file with Claude Code to match your business.
Each lecture has one or more sections with form fields.
Field types: text, textarea, number, select, table
"""

WORKBOOK_SECTIONS = {
    1: {
        "title": "AI Readiness Self-Assessment",
        "lecture_title": "The AI Inflection Point",
        "sections": [
            {
                "key": "readiness",
                "title": "AI Readiness Self-Assessment",
                "fields": [
                    {"name": "ai_maturity", "label": "Current AI Maturity Level", "type": "select",
                     "options": ["Not Started", "Experimenting", "Piloting", "Scaling", "Embedded"]},
                    {"name": "top_priorities", "label": "Top 3 AI Priorities", "type": "textarea",
                     "placeholder": "1. ...\n2. ...\n3. ..."},
                    {"name": "biggest_concern", "label": "Biggest Concern About AI Adoption", "type": "textarea"},
                    {"name": "budget_available", "label": "Approximate AI Budget Available", "type": "text",
                     "placeholder": "$"},
                    {"name": "executive_support", "label": "Executive Support Level (1-10)", "type": "number",
                     "min": 1, "max": 10},
                    {"name": "quick_win", "label": "One Process AI Could Improve Tomorrow", "type": "textarea"},
                ],
                "default_data": {
                    "ai_maturity": "Experimenting",
                    "top_priorities": "1. Reduce vendor software costs\n2. Automate manual reporting and data aggregation\n3. Modernize legacy systems that are expensive to maintain",
                    "biggest_concern": "Vendor lock-in and paying for AI wrappers when the underlying models cost pennies",
                    "budget_available": "$50,000",
                    "executive_support": 6,
                    "quick_win": "Monthly board reporting — currently takes 3 people 2 days to compile from 6 different systems",
                },
            }
        ],
    },
    2: {
        "title": "LLM Landscape Comparison",
        "lecture_title": "LLMs Demystified",
        "sections": [
            {
                "key": "llm_comparison",
                "title": "AI Model Comparison — What Your Ollama Demo Revealed",
                "type": "table",
                "columns": [
                    {"name": "model", "label": "Model", "type": "text"},
                    {"name": "provider", "label": "Provider", "type": "text"},
                    {"name": "parameters", "label": "Parameters", "type": "text"},
                    {"name": "monthly_cost", "label": "Monthly Cost", "type": "text"},
                    {"name": "speed", "label": "Speed", "type": "select",
                     "options": ["Very Fast", "Fast", "Medium", "Slow"]},
                    {"name": "quality", "label": "Quality (1-10)", "type": "number"},
                    {"name": "best_use", "label": "Best Use Case", "type": "text"},
                    {"name": "data_leaves", "label": "Data Leaves Building?", "type": "select",
                     "options": ["Yes", "No"]},
                ],
                "initial_rows": 8,
                "default_data": [
                    {"model": "Llama 3.2 1B", "provider": "Meta (local)", "parameters": "1B", "monthly_cost": "$0 (your hardware)", "speed": "Very Fast", "quality": 4, "best_use": "Simple categorization, routing, basic text", "data_leaves": "No"},
                    {"model": "Llama 3.2 3B", "provider": "Meta (local)", "parameters": "3B", "monthly_cost": "$0 (your hardware)", "speed": "Fast", "quality": 6, "best_use": "Summaries, basic code, decent writing", "data_leaves": "No"},
                    {"model": "Llama 3.1 8B", "provider": "Meta (local)", "parameters": "8B", "monthly_cost": "$0 (your hardware)", "speed": "Medium", "quality": 7, "best_use": "Good reasoning, code review, analysis", "data_leaves": "No"},
                    {"model": "Llama 3.1 70B", "provider": "Meta (local)", "parameters": "70B", "monthly_cost": "$0 (GPU server needed)", "speed": "Slow", "quality": 8, "best_use": "Complex analysis, nuanced writing", "data_leaves": "No"},
                    {"model": "Claude Sonnet 4", "provider": "Anthropic", "parameters": "Undisclosed", "monthly_cost": "$20/user (Pro)", "speed": "Fast", "quality": 9, "best_use": "Complex reasoning, coding, long documents", "data_leaves": "Yes"},
                    {"model": "GPT-4o", "provider": "OpenAI", "parameters": "Undisclosed", "monthly_cost": "$20/user (Plus)", "speed": "Fast", "quality": 9, "best_use": "General purpose, multimodal, vision", "data_leaves": "Yes"},
                    {"model": "Gemini 2.0 Pro", "provider": "Google", "parameters": "Undisclosed", "monthly_cost": "$20/user", "speed": "Fast", "quality": 8, "best_use": "Long documents, search integration", "data_leaves": "Yes"},
                    {"model": "Mistral Large", "provider": "Mistral", "parameters": "123B", "monthly_cost": "API pricing", "speed": "Fast", "quality": 7, "best_use": "European data compliance, multilingual", "data_leaves": "Yes"},
                ],
            }
        ],
    },
    3: {
        "title": "Tech Spend Audit",
        "lecture_title": "Finding Your $250K Moment",
        "sections": [
            {
                "key": "vendor_invoices",
                "title": "Top 20 Vendor Invoices — Four-Zone Framework",
                "type": "table",
                "columns": [
                    {"name": "vendor", "label": "Vendor Name", "type": "text"},
                    {"name": "annual_cost", "label": "Annual Cost ($)", "type": "number"},
                    {"name": "category", "label": "Category", "type": "text"},
                    {"name": "zone", "label": "Zone", "type": "select",
                     "options": ["Quick Win", "Strategic", "Optimize", "Keep"]},
                    {"name": "notes", "label": "Notes", "type": "text"},
                ],
                "initial_rows": 10,
                "default_data": [
                    {"vendor": "Accenture Custom Dev", "annual_cost": 250000, "category": "Software Development", "zone": "Quick Win", "notes": "Legacy system maintenance — AI tools could replace 80% of this"},
                    {"vendor": "ServiceNow", "annual_cost": 180000, "category": "IT Service Management", "zone": "Optimize", "notes": "Core platform but only using 40% of modules"},
                    {"vendor": "Salesforce Enterprise", "annual_cost": 144000, "category": "CRM", "zone": "Optimize", "notes": "120 licenses, only 67 active users"},
                    {"vendor": "Offshore QA Team (TCS)", "annual_cost": 96000, "category": "Quality Assurance", "zone": "Quick Win", "notes": "AI testing tools available at fraction of cost"},
                    {"vendor": "Microsoft 365 E5", "annual_cost": 86400, "category": "Productivity Suite", "zone": "Keep", "notes": "Well-utilized, enterprise standard"},
                    {"vendor": "Datadog", "annual_cost": 72000, "category": "Monitoring", "zone": "Optimize", "notes": "Overlaps with CloudWatch — consolidate"},
                    {"vendor": "Tableau Server", "annual_cost": 60000, "category": "Analytics & BI", "zone": "Strategic", "notes": "Evaluate AI-powered dashboards as replacement"},
                    {"vendor": "Custom Report Generator", "annual_cost": 48000, "category": "Internal Reporting", "zone": "Quick Win", "notes": "Monthly reports — CC could build this in a day"},
                    {"vendor": "Jira + Confluence", "annual_cost": 42000, "category": "Project Management", "zone": "Keep", "notes": "Team depends on it, well-adopted"},
                    {"vendor": "Workday Integration", "annual_cost": 36000, "category": "HR Integration", "zone": "Keep", "notes": "Critical HR pipeline, no good alternative"},
                ],
            }
        ],
    },
    4: {
        "title": "Legacy System Assessment",
        "lecture_title": "Legacy Code is Not a Dead End",
        "sections": [
            {
                "key": "legacy_systems",
                "title": "Legacy System Inventory",
                "type": "table",
                "columns": [
                    {"name": "system_name", "label": "System Name", "type": "text"},
                    {"name": "language", "label": "Language/Platform", "type": "text"},
                    {"name": "maintainer", "label": "Maintainer", "type": "text"},
                    {"name": "last_modified", "label": "Last Modified", "type": "text"},
                    {"name": "quadrant", "label": "Quadrant", "type": "select",
                     "options": ["Retire", "Modernize", "Wrap with API", "Leave Alone"]},
                    {"name": "risk_level", "label": "Risk", "type": "select",
                     "options": ["Low", "Medium", "High", "Critical"]},
                ],
                "initial_rows": 5,
                "default_data": [
                    {"system_name": "Accounts Payable", "language": "COBOL/CICS", "maintainer": "Bob (retiring 2027)", "last_modified": "2019", "quadrant": "Modernize", "risk_level": "Critical"},
                    {"system_name": "Inventory Tracker", "language": "Visual Basic 6", "maintainer": "None — original dev left", "last_modified": "2016", "quadrant": "Wrap with API", "risk_level": "High"},
                    {"system_name": "Customer Portal", "language": "Classic ASP", "maintainer": "Contract developer", "last_modified": "2021", "quadrant": "Modernize", "risk_level": "Medium"},
                    {"system_name": "Payroll Calculator", "language": "Fortran", "maintainer": "Finance team (manual)", "last_modified": "2012", "quadrant": "Retire", "risk_level": "High"},
                    {"system_name": "Shipping Integration", "language": "Perl CGI", "maintainer": "IT ops team", "last_modified": "2020", "quadrant": "Wrap with API", "risk_level": "Medium"},
                ],
            },
            {
                "key": "conversion_candidates",
                "title": "Code Conversion Candidates",
                "type": "table",
                "columns": [
                    {"name": "system", "label": "System/Module", "type": "text"},
                    {"name": "language", "label": "Current Language", "type": "text"},
                    {"name": "loc", "label": "Lines of Code", "type": "number"},
                    {"name": "business_logic", "label": "Core Business Logic", "type": "text"},
                    {"name": "target", "label": "Target Language", "type": "text"},
                    {"name": "priority", "label": "Priority", "type": "select",
                     "options": ["Low", "Medium", "High", "Critical"]},
                ],
                "initial_rows": 5,
                "default_data": [
                    {"system": "Accounts Payable", "language": "COBOL", "loc": 12000, "business_logic": "Invoice matching, 3-way PO validation, payment scheduling", "target": "Python + FastAPI", "priority": "Critical"},
                    {"system": "Inventory Tracker", "language": "Visual Basic 6", "loc": 8500, "business_logic": "Stock levels, reorder points, warehouse locations", "target": "Python + React", "priority": "High"},
                    {"system": "Payroll Calculator", "language": "Fortran", "loc": 3200, "business_logic": "Tax brackets, deductions, overtime rules", "target": "Python", "priority": "Medium"},
                ],
            }
        ],
    },
    5: {
        "title": "Shadow IT Inventory",
        "lecture_title": "The Shadow IT Time Bomb",
        "sections": [
            {
                "key": "shadow_it",
                "title": "Shadow IT Discovery",
                "type": "table",
                "columns": [
                    {"name": "tool", "label": "Tool/Spreadsheet", "type": "text"},
                    {"name": "owner", "label": "BU Owner", "type": "text"},
                    {"name": "sensitivity", "label": "Data Sensitivity", "type": "select",
                     "options": ["Public", "Internal", "Confidential", "Restricted"]},
                    {"name": "criticality", "label": "Business Criticality", "type": "select",
                     "options": ["Low", "Medium", "High", "Mission Critical"]},
                    {"name": "action", "label": "Triage Action", "type": "select",
                     "options": ["Accept", "Monitor", "Migrate", "Retire"]},
                ],
                "initial_rows": 8,
                "default_data": [
                    {"tool": "Finance Planning Master.xlsx", "owner": "CFO Office", "sensitivity": "Confidential", "criticality": "Mission Critical", "action": "Migrate"},
                    {"tool": "HR Headcount Tracker.xlsx", "owner": "HR Director", "sensitivity": "Restricted", "criticality": "High", "action": "Migrate"},
                    {"tool": "Marketing Campaign ROI.gsheet", "owner": "Marketing VP", "sensitivity": "Internal", "criticality": "Medium", "action": "Monitor"},
                    {"tool": "Sales Commission Calculator.xlsx", "owner": "Sales Ops", "sensitivity": "Confidential", "criticality": "High", "action": "Migrate"},
                    {"tool": "Vendor Contact Database.accdb", "owner": "Procurement", "sensitivity": "Internal", "criticality": "Medium", "action": "Migrate"},
                    {"tool": "Project Budget Tracker.xlsx", "owner": "PMO", "sensitivity": "Confidential", "criticality": "High", "action": "Monitor"},
                    {"tool": "Customer Escalation Log.gsheet", "owner": "Support Manager", "sensitivity": "Confidential", "criticality": "Medium", "action": "Migrate"},
                    {"tool": "IT Asset Inventory.xlsx", "owner": "IT Ops", "sensitivity": "Internal", "criticality": "High", "action": "Monitor"},
                ],
            }
        ],
    },
    6: {
        "title": "Offshore Cost Analysis",
        "lecture_title": "The Death of Offshore Labor Arbitrage",
        "sections": [
            {
                "key": "offshore_costs",
                "title": "Offshore Vendor True Cost Analysis",
                "type": "table",
                "columns": [
                    {"name": "vendor", "label": "Vendor", "type": "text"},
                    {"name": "monthly_invoice", "label": "Monthly Invoice ($)", "type": "number"},
                    {"name": "coordination_hours", "label": "Internal Coordination (hrs/mo)", "type": "number"},
                    {"name": "rework_pct", "label": "Rework Rate (%)", "type": "number"},
                    {"name": "true_cost", "label": "True Monthly Cost ($)", "type": "number"},
                    {"name": "ai_replacement", "label": "AI Could Replace?", "type": "select",
                     "options": ["Yes", "Partially", "No", "Unsure"]},
                ],
                "initial_rows": 5,
                "default_data": [
                    {"vendor": "TCS Application Support", "monthly_invoice": 8000, "coordination_hours": 15, "rework_pct": 22, "true_cost": 12400, "ai_replacement": "Yes"},
                    {"vendor": "Infosys QA Testing", "monthly_invoice": 6500, "coordination_hours": 10, "rework_pct": 18, "true_cost": 9200, "ai_replacement": "Yes"},
                    {"vendor": "Wipro Data Entry", "monthly_invoice": 4000, "coordination_hours": 8, "rework_pct": 12, "true_cost": 5600, "ai_replacement": "Yes"},
                    {"vendor": "HCL DevOps", "monthly_invoice": 12000, "coordination_hours": 20, "rework_pct": 15, "true_cost": 17000, "ai_replacement": "Partially"},
                    {"vendor": "Cognizant Analytics", "monthly_invoice": 9000, "coordination_hours": 12, "rework_pct": 8, "true_cost": 11000, "ai_replacement": "Partially"},
                ],
            }
        ],
    },
    7: {
        "title": "SaaS Stack Audit",
        "lecture_title": "Renegotiating Your SaaS Stack",
        "sections": [
            {
                "key": "saas_audit",
                "title": "SaaS Stack Review",
                "type": "table",
                "columns": [
                    {"name": "tool", "label": "SaaS Tool", "type": "text"},
                    {"name": "annual_cost", "label": "Annual Cost ($)", "type": "number"},
                    {"name": "active_users", "label": "Active Users", "type": "number"},
                    {"name": "licensed_users", "label": "Licensed Users", "type": "number"},
                    {"name": "renewal_date", "label": "Renewal Date", "type": "text"},
                    {"name": "action", "label": "Action", "type": "select",
                     "options": ["Keep", "Renegotiate", "Replace", "Cut"]},
                ],
                "initial_rows": 25,
                "default_data": [
                    {"tool": "Salesforce Enterprise", "annual_cost": 285000, "active_users": 108, "licensed_users": 150, "renewal_date": "2025-12", "action": "Renegotiate"},
                    {"tool": "HubSpot Marketing Hub", "annual_cost": 72000, "active_users": 22, "licensed_users": 40, "renewal_date": "2025-11", "action": "Cut"},
                    {"tool": "Microsoft 365 E5", "annual_cost": 187200, "active_users": 289, "licensed_users": 300, "renewal_date": "2026-03", "action": "Keep"},
                    {"tool": "Google Workspace", "annual_cost": 43200, "active_users": 45, "licensed_users": 300, "renewal_date": "2025-09", "action": "Cut"},
                    {"tool": "Slack Business+", "annual_cost": 64800, "active_users": 265, "licensed_users": 300, "renewal_date": "2025-09", "action": "Renegotiate"},
                    {"tool": "Zoom Business", "annual_cost": 33600, "active_users": 142, "licensed_users": 300, "renewal_date": "2025-08", "action": "Cut"},
                    {"tool": "Jira Software Premium", "annual_cost": 54000, "active_users": 98, "licensed_users": 150, "renewal_date": "2026-01", "action": "Keep"},
                    {"tool": "Asana Business", "annual_cost": 39600, "active_users": 35, "licensed_users": 80, "renewal_date": "2025-10", "action": "Cut"},
                    {"tool": "Monday.com Enterprise", "annual_cost": 62400, "active_users": 28, "licensed_users": 60, "renewal_date": "2025-07", "action": "Cut"},
                    {"tool": "AWS", "annual_cost": 576000, "active_users": 45, "licensed_users": 45, "renewal_date": "2025-06", "action": "Keep"},
                    {"tool": "Azure", "annual_cost": 192000, "active_users": 18, "licensed_users": 30, "renewal_date": "2026-02", "action": "Renegotiate"},
                    {"tool": "Datadog Pro", "annual_cost": 115200, "active_users": 22, "licensed_users": 25, "renewal_date": "2026-02", "action": "Renegotiate"},
                    {"tool": "Splunk Cloud", "annual_cost": 168000, "active_users": 12, "licensed_users": 15, "renewal_date": "2025-12", "action": "Replace"},
                    {"tool": "ServiceNow ITSM", "annual_cost": 144000, "active_users": 42, "licensed_users": 50, "renewal_date": "2026-06", "action": "Keep"},
                    {"tool": "Zendesk Suite Pro", "annual_cost": 96000, "active_users": 48, "licensed_users": 60, "renewal_date": "2025-11", "action": "Renegotiate"},
                    {"tool": "DocuSign Business Pro", "annual_cost": 21600, "active_users": 35, "licensed_users": 100, "renewal_date": "2025-07", "action": "Renegotiate"},
                    {"tool": "Adobe Creative Cloud", "annual_cost": 28800, "active_users": 14, "licensed_users": 20, "renewal_date": "2025-10", "action": "Keep"},
                    {"tool": "Figma Organization", "annual_cost": 28800, "active_users": 14, "licensed_users": 15, "renewal_date": "2025-10", "action": "Keep"},
                    {"tool": "Snowflake", "annual_cost": 240000, "active_users": 18, "licensed_users": 20, "renewal_date": "2026-01", "action": "Keep"},
                    {"tool": "Tableau Creator", "annual_cost": 84000, "active_users": 22, "licensed_users": 35, "renewal_date": "2025-12", "action": "Replace"},
                    {"tool": "Okta Workforce Identity", "annual_cost": 72000, "active_users": 300, "licensed_users": 300, "renewal_date": "2026-03", "action": "Keep"},
                    {"tool": "CrowdStrike Falcon", "annual_cost": 96000, "active_users": 300, "licensed_users": 300, "renewal_date": "2026-06", "action": "Keep"},
                    {"tool": "Workday HCM", "annual_cost": 180000, "active_users": 45, "licensed_users": 300, "renewal_date": "2026-12", "action": "Renegotiate"},
                    {"tool": "Coupa Procurement", "annual_cost": 120000, "active_users": 28, "licensed_users": 50, "renewal_date": "2025-09", "action": "Renegotiate"},
                    {"tool": "Miro Business", "annual_cost": 18000, "active_users": 12, "licensed_users": 40, "renewal_date": "2025-08", "action": "Cut"},
                ],
            }
        ],
    },
    8: {
        "title": "Strategy Cascade & IT Portfolio",
        "lecture_title": "From Mission to IT Strategy",
        "sections": [
            {
                "key": "mission",
                "title": "Mission Statement & Verb Analysis",
                "fields": [
                    {"name": "company_mission", "label": "Your Company Mission Statement", "type": "textarea",
                     "placeholder": "Paste your company's mission statement here"},
                    {"name": "verbs", "label": "Actionable Verbs (underline each verb in the mission)", "type": "textarea",
                     "placeholder": "e.g., deliver, innovate, protect, sustain, grow..."},
                    {"name": "capabilities", "label": "Capabilities Implied by Each Verb", "type": "textarea",
                     "placeholder": "deliver → project execution systems\ninnovate → R&D/IP tools\nprotect → compliance/safety platforms"},
                ],
            },
            {
                "key": "strategic_pillars",
                "title": "Strategic Pillars & IT Initiatives",
                "type": "table",
                "columns": [
                    {"name": "pillar", "label": "Strategic Pillar", "type": "text"},
                    {"name": "initiative", "label": "Strategic Initiative", "type": "text"},
                    {"name": "it_project", "label": "IT Project", "type": "text"},
                    {"name": "owner", "label": "Business Owner", "type": "text"},
                    {"name": "status", "label": "Status", "type": "select",
                     "options": ["Not Started", "In Progress", "Complete", "Orphan — No Link"]},
                ],
                "initial_rows": 10,
            },
            {
                "key": "portfolio",
                "title": "IT Portfolio & Spend Analysis",
                "fields": [
                    {"name": "annual_revenue", "label": "Company Annual Net Revenue ($)", "type": "number"},
                    {"name": "it_spend", "label": "Total Annual IT Spend ($)", "type": "number"},
                    {"name": "it_pct", "label": "IT Spend as % of Revenue", "type": "text",
                     "placeholder": "Calculate: IT Spend / Revenue × 100"},
                    {"name": "industry_benchmark", "label": "Industry Benchmark Range", "type": "select",
                     "options": ["Manufacturing 1-3%", "Professional Services 3-5%", "Financial Services 7-10%", "Technology 8-15%", "Other"]},
                    {"name": "run_pct", "label": "Run the Business (%)", "type": "number",
                     "placeholder": "60-70% typical"},
                    {"name": "grow_pct", "label": "Grow the Business (%)", "type": "number",
                     "placeholder": "20-30% typical"},
                    {"name": "transform_pct", "label": "Transform the Business (%)", "type": "number",
                     "placeholder": "5-10% typical"},
                    {"name": "orphan_projects", "label": "Orphan Projects (no strategic link)", "type": "textarea",
                     "placeholder": "List any IT projects that can't be traced to a strategic initiative"},
                ],
            },
        ],
    },
    9: {
        "title": "Communication Frameworks",
        "lecture_title": "The CIO as Communicator",
        "sections": [
            {
                "key": "board_rewrite",
                "title": "Tech-to-Business Translation Practice",
                "fields": [
                    {"name": "original_update", "label": "Your Last IT Status Update (paste it here)", "type": "textarea",
                     "placeholder": "Paste a recent IT status update, email, or report — jargon and all"},
                    {"name": "board_version", "label": "Board-Ready Rewrite (no technical jargon)", "type": "textarea",
                     "placeholder": "Rewrite the above for a board of directors — focus on business impact, risk, and cost"},
                    {"name": "elevator_pitch", "label": "60-Second Elevator Pitch for Your Biggest Initiative", "type": "textarea",
                     "placeholder": "Imagine the CEO asks 'What's the one thing I should know about IT right now?' — answer in 60 seconds"},
                ],
            },
            {
                "key": "stakeholder_map",
                "title": "Stakeholder Communication Map",
                "type": "table",
                "columns": [
                    {"name": "stakeholder", "label": "Stakeholder", "type": "text"},
                    {"name": "role", "label": "Role", "type": "text"},
                    {"name": "cares_about", "label": "Cares About", "type": "text"},
                    {"name": "language", "label": "Language to Use", "type": "text"},
                    {"name": "frequency", "label": "Update Frequency", "type": "select",
                     "options": ["Weekly", "Biweekly", "Monthly", "Quarterly", "As Needed"]},
                ],
                "initial_rows": 6,
            },
            {
                "key": "peer_feedback",
                "title": "Presentation Self-Assessment",
                "fields": [
                    {"name": "peer_feedback", "label": "Peer Feedback: 'When I present, the one thing I should change is...'", "type": "textarea"},
                    {"name": "ceo_shadow", "label": "CEO/CFO Shadow Session Notes — What did you observe?", "type": "textarea",
                     "placeholder": "How do they structure updates? What language do they use? How do they handle questions?"},
                ],
            },
        ],
    },
    10: {
        "title": "Build vs Buy Assessment",
        "lecture_title": "Build vs Buy Just Changed",
        "sections": [
            {
                "key": "build_vs_buy",
                "title": "Build vs Buy Decision Framework",
                "fields": [
                    {"name": "tool_name", "label": "SaaS Tool Under Evaluation", "type": "text"},
                    {"name": "annual_cost", "label": "Current Annual Cost ($)", "type": "number"},
                    {"name": "core_features", "label": "Core Features You Actually Use", "type": "textarea",
                     "placeholder": "List the 3-5 features your team actually uses daily"},
                    {"name": "build_feasibility", "label": "Could AI Build This? (1-10)", "type": "number",
                     "min": 1, "max": 10},
                    {"name": "data_sensitivity", "label": "Data Sensitivity Level", "type": "select",
                     "options": ["Public", "Internal", "Confidential", "Restricted"]},
                    {"name": "decision", "label": "Decision", "type": "select",
                     "options": ["Keep SaaS", "Build with AI", "Hybrid", "Needs More Analysis"]},
                    {"name": "rationale", "label": "Rationale", "type": "textarea"},
                ],
            }
        ],
    },
    11: {
        "title": "Team Readiness Conversations",
        "lecture_title": "Leading Teams Through AI Disruption",
        "sections": [
            {
                "key": "team_readiness",
                "title": "Team AI Readiness Assessment",
                "type": "table",
                "columns": [
                    {"name": "name", "label": "Team Member", "type": "text"},
                    {"name": "role", "label": "Current Role", "type": "text"},
                    {"name": "concern", "label": "Concern Noted", "type": "text"},
                    {"name": "skill_gap", "label": "Skill Gap", "type": "text"},
                    {"name": "action", "label": "Development Action", "type": "text"},
                ],
                "initial_rows": 8,
            }
        ],
    },
    12: {
        "title": "AI Governance Checklist",
        "lecture_title": "AI Governance and IP Protection",
        "sections": [
            {
                "key": "governance",
                "title": "Governance Sprint Plan",
                "fields": [
                    {"name": "sprint1", "label": "Sprint 1 (Weeks 1-2): Quick Policies", "type": "textarea",
                     "placeholder": "Acceptable use policy, data classification rules, approved tool list..."},
                    {"name": "sprint2", "label": "Sprint 2 (Weeks 3-4): Access Controls", "type": "textarea",
                     "placeholder": "Who can use which AI tools, approval workflows, monitoring..."},
                    {"name": "sprint3", "label": "Sprint 3 (Weeks 5-6): Audit & Review", "type": "textarea",
                     "placeholder": "Regular review cadence, incident response, compliance checks..."},
                    {"name": "ip_risks", "label": "Top IP/Data Risks Identified", "type": "textarea"},
                    {"name": "approved_tools", "label": "Approved AI Tools List", "type": "textarea",
                     "placeholder": "Tool name — use case — data allowed"},
                ],
            }
        ],
    },
    13: {
        "title": "90-Day AI Roadmap",
        "lecture_title": "Your 90-Day AI Leadership Roadmap",
        "sections": [
            {
                "key": "roadmap",
                "title": "Your 90-Day Plan",
                "fields": [
                    {"name": "week1_2", "label": "Weeks 1-2: Quick Wins", "type": "textarea",
                     "placeholder": "What can you deploy or demonstrate in the first two weeks?"},
                    {"name": "week3_4", "label": "Weeks 3-4: Foundation", "type": "textarea",
                     "placeholder": "Governance policies, team training, tool selection..."},
                    {"name": "week5_8", "label": "Weeks 5-8: Build Momentum", "type": "textarea",
                     "placeholder": "First real project, metrics baseline, stakeholder demos..."},
                    {"name": "week9_12", "label": "Weeks 9-12: Scale", "type": "textarea",
                     "placeholder": "Expand to more teams, measure ROI, present to leadership..."},
                    {"name": "success_metric", "label": "Primary Success Metric", "type": "text",
                     "placeholder": "How will you know this worked?"},
                    {"name": "biggest_risk", "label": "Biggest Risk to This Plan", "type": "textarea"},
                ],
            }
        ],
    },
    14: {
        "title": "AI-Era Team Roles",
        "lecture_title": "Building Your AI-Era IT Team",
        "sections": [
            {
                "key": "role_mapping",
                "title": "Role Evolution Map",
                "type": "table",
                "columns": [
                    {"name": "current_role", "label": "Current Role", "type": "text"},
                    {"name": "person", "label": "Person", "type": "text"},
                    {"name": "ai_era_role", "label": "AI-Era Equivalent", "type": "text"},
                    {"name": "skill_dev", "label": "Skill Development", "type": "text"},
                    {"name": "timeline", "label": "Timeline", "type": "select",
                     "options": ["30 days", "60 days", "90 days", "6 months"]},
                ],
                "initial_rows": 8,
            }
        ],
    },
    15: {
        "title": "Vendor Risk Scorecard",
        "lecture_title": "AI Tools, Dependency, and Vendor Risk",
        "sections": [
            {
                "key": "vendor_scorecard",
                "title": "AI Vendor Risk Assessment",
                "type": "table",
                "columns": [
                    {"name": "vendor", "label": "Vendor", "type": "text"},
                    {"name": "lock_in", "label": "Lock-in Risk (1-5)", "type": "number"},
                    {"name": "data_portability", "label": "Data Portability (1-5)", "type": "number"},
                    {"name": "pricing_risk", "label": "Pricing Risk (1-5)", "type": "number"},
                    {"name": "alternative", "label": "Best Alternative", "type": "text"},
                    {"name": "mitigation", "label": "Mitigation Action", "type": "text"},
                ],
                "initial_rows": 5,
            }
        ],
    },
}
