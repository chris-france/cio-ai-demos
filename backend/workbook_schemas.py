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
            }
        ],
    },
    2: {
        "title": "Tech Spend Audit",
        "lecture_title": "LLMs Demystified",
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
            }
        ],
    },
    3: {
        "title": "Legacy System Inventory",
        "lecture_title": "Finding Your $250K Moment",
        "sections": [
            {
                "key": "legacy_systems",
                "title": "Legacy System Inventory — Four-Quadrant Assessment",
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
            }
        ],
    },
    4: {
        "title": "Legacy Code Conversion Plan",
        "lecture_title": "Legacy Code is Not a Dead End",
        "sections": [
            {
                "key": "conversion_candidates",
                "title": "COBOL/Legacy Code Conversion Candidates",
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
                "initial_rows": 10,
            }
        ],
    },
    8: {
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
    9: {
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
    10: {
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
    11: {
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
    12: {
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
    13: {
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
