#!/usr/bin/env python3
"""SaaS Audit Dashboard Generator — CIO AI Foundation Course, Lecture 7"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import base64
import io
import os

# ── Load data ──
csv_path = os.path.join(os.path.dirname(__file__), 'saas-inventory.csv')
df = pd.read_csv(csv_path)

# ── Analysis ──
df['cost_per_user_month'] = (df['annual_cost'] / df['licensed_users'] / 12).round(2)
df['utilization_pct'] = ((df['active_users'] / df['licensed_users']) * 100).round(1)
df['overpriced'] = df['cost_per_user_month'] > 50
df['underutilized'] = df['utilization_pct'] < 40

# Overlap detection
overlap_groups = {
    'Productivity & Messaging': ['Microsoft 365 E5', 'Google Workspace', 'Slack Business+'],
    'Project Management': ['Jira Software Premium', 'Asana Business', 'Monday.com Enterprise'],
    'Monitoring & Logging': ['Datadog Pro', 'Splunk Cloud'],
    'Design Tools': ['Adobe Creative Cloud', 'Figma Organization'],
    'Cloud Infrastructure': ['AWS', 'Azure'],
    'IT Support / Helpdesk': ['ServiceNow ITSM', 'Zendesk Suite Pro'],
    'CRM & Marketing': ['Salesforce Enterprise', 'HubSpot Marketing Hub'],
}

# Savings calculations
savings = []

# 1. Underutilized: rightsize to active users
for _, row in df[df['underutilized']].iterrows():
    current = row['annual_cost']
    rightsized = row['annual_cost'] * (row['active_users'] / row['licensed_users'])
    save = current - rightsized
    savings.append({'tool': row['tool_name'], 'type': 'Rightsize (low utilization)', 'current': current, 'proposed': rightsized, 'savings': save})

# 2. Overlap eliminations (recommend dropping weaker tool)
overlap_cuts = {
    'Google Workspace': 43200,       # most on M365
    'Monday.com Enterprise': 62400,  # consolidate to Jira
    'Asana Business': 39600,         # consolidate to Jira
    'Slack Business+': 64800,        # consolidate to Teams
    'Splunk Cloud': 168000,          # consolidate to Datadog + open-source
    'Zendesk Suite Pro': 96000,      # consolidate to ServiceNow
}
for tool, save in overlap_cuts.items():
    savings.append({'tool': tool, 'type': 'Eliminate overlap', 'current': save, 'proposed': 0, 'savings': save})

savings_df = pd.DataFrame(savings)
# Deduplicate (if a tool is both underutilized AND an overlap cut, keep the larger savings)
savings_df = savings_df.sort_values('savings', ascending=False).drop_duplicates(subset='tool', keep='first')
total_savings = savings_df['savings'].sum()

# Open-source alternatives for top 5 most expensive
top5 = df.nlargest(5, 'annual_cost')
oss_alternatives = {
    'AWS': {'alt': 'Hetzner / OVH / On-Prem K8s', 'notes': 'Hybrid cloud for non-critical workloads; reserved instances for committed use'},
    'Salesforce Enterprise': {'alt': 'SuiteCRM / ERPNext CRM', 'notes': 'Open-source CRM; covers 80% of features for orgs not using deep Salesforce ecosystem'},
    'Snowflake': {'alt': 'Apache Iceberg + DuckDB / ClickHouse', 'notes': 'Open lakehouse stack; strong for analytics-heavy workloads'},
    'Azure': {'alt': 'Consolidate to AWS / OpenStack', 'notes': 'Eliminate dual-cloud overhead; migrate legacy workloads'},
    'Microsoft 365 E5': {'alt': 'LibreOffice + Nextcloud + Jitsi', 'notes': 'Viable for some roles; E5→E3 downgrade saves ~40% for users not needing security suite'},
}

# ── Charts ──
plt.rcParams.update({'font.family': 'sans-serif', 'font.size': 10, 'figure.facecolor': 'white'})

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    plt.close(fig)
    return b64

# Chart 1: Cost per user/month bar chart with $50 threshold line
fig1, ax1 = plt.subplots(figsize=(12, 5))
sorted_df = df.sort_values('cost_per_user_month', ascending=True)
colors = ['#ef4444' if v > 50 else '#3b82f6' for v in sorted_df['cost_per_user_month']]
bars = ax1.barh(sorted_df['tool_name'], sorted_df['cost_per_user_month'], color=colors, edgecolor='white', height=0.7)
ax1.axvline(x=50, color='#ef4444', linestyle='--', linewidth=1.5, label='$50/user/mo threshold')
ax1.set_xlabel('Cost per User per Month ($)')
ax1.set_title('Cost per User per Month — Tools Over $50 Flagged Red', fontweight='bold', fontsize=12)
ax1.legend(loc='lower right')
for bar, val in zip(bars, sorted_df['cost_per_user_month']):
    ax1.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'${val:.0f}', va='center', fontsize=8, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
plt.tight_layout()
chart1_b64 = fig_to_base64(fig1)

# Chart 2: Utilization scatter with quadrants
fig2, ax2 = plt.subplots(figsize=(10, 6))
scatter_colors = []
for _, row in df.iterrows():
    if row['overpriced'] and row['underutilized']:
        scatter_colors.append('#ef4444')  # red: both
    elif row['overpriced']:
        scatter_colors.append('#f59e0b')  # amber: overpriced
    elif row['underutilized']:
        scatter_colors.append('#f59e0b')  # amber: underutilized
    else:
        scatter_colors.append('#22c55e')  # green: ok

ax2.scatter(df['utilization_pct'], df['cost_per_user_month'], c=scatter_colors, s=df['annual_cost']/2000, alpha=0.8, edgecolors='white', linewidth=1.5, zorder=5)
ax2.axhline(y=50, color='#ef4444', linestyle='--', linewidth=1, alpha=0.5)
ax2.axvline(x=40, color='#f59e0b', linestyle='--', linewidth=1, alpha=0.5)

# Quadrant labels
ax2.text(15, 800, 'DANGER ZONE\nOverpriced + Underutilized', fontsize=9, color='#ef4444', fontweight='bold', ha='center', alpha=0.7)
ax2.text(80, 800, 'OVERPRICED\nbut Well-Used', fontsize=9, color='#f59e0b', fontweight='bold', ha='center', alpha=0.7)
ax2.text(15, 5, 'UNDERUTILIZED\nbut Affordable', fontsize=9, color='#f59e0b', fontweight='bold', ha='center', alpha=0.7)
ax2.text(80, 5, 'HEALTHY\nGood Value', fontsize=9, color='#22c55e', fontweight='bold', ha='center', alpha=0.7)

for _, row in df.iterrows():
    if row['overpriced'] or row['underutilized']:
        ax2.annotate(row['tool_name'].split(' ')[0], (row['utilization_pct'], row['cost_per_user_month']),
                     fontsize=7, ha='left', va='bottom', xytext=(5, 5), textcoords='offset points')

ax2.set_xlabel('Utilization (%)')
ax2.set_ylabel('Cost per User per Month ($)')
ax2.set_title('SaaS Portfolio Health — Utilization vs Cost (bubble size = annual spend)', fontweight='bold', fontsize=12)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.tight_layout()
chart2_b64 = fig_to_base64(fig2)

# Chart 3: Annual spend by category (donut)
fig3, ax3 = plt.subplots(figsize=(7, 7))
cat_spend = df.groupby('category')['annual_cost'].sum().sort_values(ascending=False)
color_palette = ['#1e3a5f', '#3b82f6', '#60a5fa', '#93c5fd', '#c084fc', '#f59e0b', '#22c55e', '#6b7280', '#ef4444', '#14b8a6', '#e879f9', '#f97316']
wedges, texts, autotexts = ax3.pie(cat_spend, labels=cat_spend.index, autopct=lambda p: f'${p*cat_spend.sum()/100/1000:.0f}K' if p > 3 else '',
                                    colors=color_palette[:len(cat_spend)], pctdistance=0.8, startangle=90,
                                    wedgeprops={'edgecolor': 'white', 'linewidth': 2})
centre = plt.Circle((0, 0), 0.55, fc='white')
ax3.add_artist(centre)
ax3.text(0, 0.05, f'${cat_spend.sum()/1000:.0f}K', ha='center', va='center', fontsize=20, fontweight='bold', color='#1e293b')
ax3.text(0, -0.12, 'Total Annual', ha='center', va='center', fontsize=10, color='#64748b')
for t in texts:
    t.set_fontsize(8)
for t in autotexts:
    t.set_fontsize(7)
    t.set_fontweight('bold')
ax3.set_title('Annual SaaS Spend by Category', fontweight='bold', fontsize=12, pad=20)
plt.tight_layout()
chart3_b64 = fig_to_base64(fig3)

# Chart 4: Savings waterfall
fig4, ax4 = plt.subplots(figsize=(11, 5))
savings_sorted = savings_df.sort_values('savings', ascending=False).head(10)
bar_colors = ['#ef4444' if t == 'Eliminate overlap' else '#f59e0b' for t in savings_sorted['type']]
ax4.barh(savings_sorted['tool'], savings_sorted['savings']/1000, color=bar_colors, edgecolor='white', height=0.65)
for i, (_, row) in enumerate(savings_sorted.iterrows()):
    ax4.text(row['savings']/1000 + 2, i, f"${row['savings']/1000:.0f}K — {row['type']}", va='center', fontsize=8)
ax4.set_xlabel('Potential Annual Savings ($K)')
ax4.set_title(f'Top Savings Opportunities — Total: ${total_savings/1000:.0f}K/year', fontweight='bold', fontsize=12)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:.0f}K'))
plt.tight_layout()
chart4_b64 = fig_to_base64(fig4)

# ── Build HTML ──
# Prepare table rows
table_rows = ''
for _, row in df.sort_values('annual_cost', ascending=False).iterrows():
    flags = []
    if row['overpriced']:
        flags.append('<span class="flag-red">OVERPRICED</span>')
    if row['underutilized']:
        flags.append('<span class="flag-amber">UNDERUTILIZED</span>')
    if not flags:
        flags.append('<span class="flag-green">OK</span>')

    util_color = '#ef4444' if row['utilization_pct'] < 40 else '#22c55e' if row['utilization_pct'] >= 70 else '#f59e0b'
    cost_color = '#ef4444' if row['cost_per_user_month'] > 50 else '#1e293b'

    table_rows += f'''
        <tr>
            <td class="font-semibold text-gray-900">{row['tool_name']}</td>
            <td class="text-gray-500">{row['category']}</td>
            <td class="text-right font-semibold">${row['annual_cost']:,.0f}</td>
            <td class="text-center">{row['active_users']}/{row['licensed_users']}</td>
            <td class="text-center">
                <div class="util-bar-bg"><div class="util-bar-fill" style="width:{min(row['utilization_pct'],100)}%;background:{util_color}"></div></div>
                <span class="text-xs" style="color:{util_color}">{row['utilization_pct']}%</span>
            </td>
            <td class="text-right font-bold" style="color:{cost_color}">${row['cost_per_user_month']:.0f}</td>
            <td class="text-center">{''.join(flags)}</td>
            <td class="text-center text-xs text-gray-500">{row['contract_end']}</td>
        </tr>'''

# Overlap section
overlap_html = ''
for group, tools in overlap_groups.items():
    tool_list = ''.join(f'<span class="overlap-tool">{t}</span>' for t in tools)
    group_cost = df[df['tool_name'].isin(tools)]['annual_cost'].sum()
    overlap_html += f'''
        <div class="overlap-card">
            <div class="overlap-header">
                <span class="overlap-group">{group}</span>
                <span class="overlap-cost">${group_cost:,.0f}/yr combined</span>
            </div>
            <div class="overlap-tools">{tool_list}</div>
        </div>'''

# OSS alternatives
oss_html = ''
for _, row in top5.iterrows():
    alt_info = oss_alternatives.get(row['tool_name'], {'alt': 'N/A', 'notes': ''})
    oss_html += f'''
        <tr>
            <td class="font-semibold text-gray-900">{row['tool_name']}</td>
            <td class="text-right font-semibold">${row['annual_cost']:,.0f}</td>
            <td class="font-medium text-emerald-700">{alt_info['alt']}</td>
            <td class="text-xs text-gray-500">{alt_info['notes']}</td>
        </tr>'''

# Stats
total_spend = df['annual_cost'].sum()
overpriced_count = df['overpriced'].sum()
underutilized_count = df['underutilized'].sum()
avg_util = df['utilization_pct'].mean()

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SaaS Audit Dashboard — Meridian Health Systems</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        .flag-red {{ background: #fef2f2; color: #dc2626; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 9999px; border: 1px solid #fecaca; }}
        .flag-amber {{ background: #fffbeb; color: #d97706; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 9999px; border: 1px solid #fde68a; }}
        .flag-green {{ background: #f0fdf4; color: #16a34a; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 9999px; border: 1px solid #bbf7d0; }}
        .util-bar-bg {{ width: 100%; background: #f1f5f9; border-radius: 9999px; height: 6px; margin-bottom: 2px; }}
        .util-bar-fill {{ height: 6px; border-radius: 9999px; transition: width 0.3s; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th {{ text-align: left; padding: 10px 12px; font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 2px solid #e2e8f0; }}
        td {{ padding: 10px 12px; font-size: 13px; border-bottom: 1px solid #f1f5f9; }}
        tr:hover {{ background: #f8fafc; }}
        .overlap-card {{ border: 1px solid #e2e8f0; border-radius: 12px; padding: 14px; }}
        .overlap-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
        .overlap-group {{ font-weight: 700; font-size: 13px; color: #1e293b; }}
        .overlap-cost {{ font-size: 12px; font-weight: 600; color: #dc2626; }}
        .overlap-tools {{ display: flex; gap: 6px; flex-wrap: wrap; }}
        .overlap-tool {{ background: #f1f5f9; color: #475569; font-size: 11px; font-weight: 500; padding: 4px 10px; border-radius: 6px; }}
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <div class="bg-gradient-to-r from-slate-900 via-blue-900 to-indigo-900 text-white">
        <div class="max-w-7xl mx-auto px-6 py-8">
            <div class="flex items-center justify-between">
                <div>
                    <p class="text-blue-300 text-sm font-medium tracking-wider uppercase">CIO AI Foundation — Lecture 7 Demo</p>
                    <h1 class="text-3xl font-bold mt-1">SaaS Audit Dashboard</h1>
                    <p class="text-slate-300 text-sm mt-1">25 tools analyzed — find the waste, consolidate, renegotiate</p>
                </div>
                <div class="flex gap-3">
                    <div class="bg-white/10 backdrop-blur px-4 py-2 rounded-lg text-center">
                        <p class="text-2xl font-bold text-red-400">${total_spend/1000000:.1f}M</p>
                        <p class="text-xs text-slate-300">Annual SaaS Spend</p>
                    </div>
                    <div class="bg-white/10 backdrop-blur px-4 py-2 rounded-lg text-center">
                        <p class="text-2xl font-bold text-emerald-400">${total_savings/1000:.0f}K</p>
                        <p class="text-xs text-slate-300">Potential Savings</p>
                    </div>
                    <div class="bg-white/10 backdrop-blur px-4 py-2 rounded-lg text-center">
                        <p class="text-2xl font-bold text-amber-400">{total_savings/total_spend*100:.0f}%</p>
                        <p class="text-xs text-slate-300">Savings Rate</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-6 space-y-6">

        <!-- KPI Strip -->
        <div class="grid grid-cols-6 gap-4">
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-slate-800">25</p>
                <p class="text-xs text-gray-500 mt-1">SaaS Tools</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-red-600">{int(overpriced_count)}</p>
                <p class="text-xs text-gray-500 mt-1">Overpriced (&gt;$50/user/mo)</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-amber-600">{int(underutilized_count)}</p>
                <p class="text-xs text-gray-500 mt-1">Underutilized (&lt;40%)</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-slate-800">{avg_util:.0f}%</p>
                <p class="text-xs text-gray-500 mt-1">Avg Utilization</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-red-600">7</p>
                <p class="text-xs text-gray-500 mt-1">Overlap Groups</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 text-center">
                <p class="text-2xl font-bold text-emerald-600">6</p>
                <p class="text-xs text-gray-500 mt-1">Contracts Expiring &lt;6mo</p>
            </div>
        </div>

        <!-- Charts: Spend by Category + Utilization Scatter -->
        <div class="grid grid-cols-2 gap-6">
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4">Annual Spend by Category</h2>
                <img src="data:image/png;base64,{chart3_b64}" class="w-full" alt="Spend by category donut chart">
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
                <h2 class="text-lg font-bold text-gray-900 mb-4">Portfolio Health — Utilization vs Cost</h2>
                <img src="data:image/png;base64,{chart2_b64}" class="w-full" alt="Utilization vs cost scatter">
            </div>
        </div>

        <!-- Cost per User chart -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-4">Cost per User per Month — Overpriced Tools Flagged</h2>
            <img src="data:image/png;base64,{chart1_b64}" class="w-full" alt="Cost per user bar chart">
        </div>

        <!-- Full Table -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-1">Complete SaaS Inventory — 25 Tools</h2>
            <p class="text-sm text-gray-500 mb-4">Sorted by annual cost. Flags: <span class="flag-red">OVERPRICED</span> = &gt;$50/user/mo &nbsp; <span class="flag-amber">UNDERUTILIZED</span> = &lt;40% active users</p>
            <div class="overflow-x-auto">
                <table>
                    <thead>
                        <tr>
                            <th>Tool</th>
                            <th>Category</th>
                            <th style="text-align:right">Annual Cost</th>
                            <th style="text-align:center">Active / Licensed</th>
                            <th style="text-align:center">Utilization</th>
                            <th style="text-align:right">$/User/Mo</th>
                            <th style="text-align:center">Status</th>
                            <th style="text-align:center">Renewal</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Overlap Detection -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-1">Overlap Detection — 7 Groups Found</h2>
            <p class="text-sm text-gray-500 mb-4">Tools with redundant capabilities. Each group is a consolidation opportunity.</p>
            <div class="grid grid-cols-2 gap-4">
                {overlap_html}
            </div>
        </div>

        <!-- Savings Opportunities -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-4">Top Savings Opportunities — ${total_savings/1000:.0f}K/year Potential</h2>
            <img src="data:image/png;base64,{chart4_b64}" class="w-full" alt="Savings waterfall chart">
        </div>

        <!-- Open-Source Alternatives -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-1">Open-Source Alternatives — Top 5 Most Expensive Tools</h2>
            <p class="text-sm text-gray-500 mb-4">Not every tool should be replaced — but every renewal should be benchmarked against open-source options</p>
            <table>
                <thead>
                    <tr>
                        <th>Current Tool</th>
                        <th style="text-align:right">Annual Cost</th>
                        <th>Open-Source / Lower-Cost Alternative</th>
                        <th>Notes</th>
                    </tr>
                </thead>
                <tbody>
                    {oss_html}
                </tbody>
            </table>
        </div>

        <!-- Executive Summary -->
        <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
            <h2 class="text-lg font-bold text-gray-900 mb-4">Executive Summary</h2>
            <div class="grid grid-cols-3 gap-4">
                <div class="border border-red-200 bg-red-50 rounded-xl p-4">
                    <h3 class="font-bold text-red-900 text-sm mb-2">Immediate Actions (0-3 months)</h3>
                    <ul class="text-xs text-red-800 space-y-1.5 list-disc ml-4">
                        <li>Cancel Google Workspace ($43K) — 85% of users already on M365</li>
                        <li>Cancel Monday.com ($62K) and Asana ($40K) — consolidate to Jira</li>
                        <li>Begin Splunk→Datadog consolidation ($168K savings)</li>
                        <li>Rightsize DocuSign licenses (100→35 active users)</li>
                    </ul>
                </div>
                <div class="border border-amber-200 bg-amber-50 rounded-xl p-4">
                    <h3 class="font-bold text-amber-900 text-sm mb-2">Near-Term (3-6 months)</h3>
                    <ul class="text-xs text-amber-800 space-y-1.5 list-disc ml-4">
                        <li>Consolidate Slack→Teams ($65K) at contract renewal</li>
                        <li>Merge Zendesk→ServiceNow ($96K) for unified ITSM</li>
                        <li>Renegotiate Workday — paying for 300 licenses, 45 active users</li>
                        <li>Audit Coupa — 28/50 users active, expiring Sep 2025</li>
                    </ul>
                </div>
                <div class="border border-emerald-200 bg-emerald-50 rounded-xl p-4">
                    <h3 class="font-bold text-emerald-900 text-sm mb-2">Strategic (6-12 months)</h3>
                    <ul class="text-xs text-emerald-800 space-y-1.5 list-disc ml-4">
                        <li>Evaluate cloud consolidation (AWS+Azure = $768K)</li>
                        <li>Pilot open-source monitoring to pressure Datadog pricing</li>
                        <li>Implement SaaS governance policy — no tool purchase without IT approval</li>
                        <li>Build SaaS management dashboard for ongoing tracking</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="text-center text-xs text-gray-400 py-4">
            AI-generated demo for CIO AI Foundation Course — Lecture 7: SaaS Renegotiation
        </div>
    </div>
</body>
</html>'''

# Write output
output_path = os.path.join(os.path.dirname(__file__), 'saas-audit.html')
with open(output_path, 'w') as f:
    f.write(html)

print(f"Dashboard generated: {output_path}")
print(f"Total SaaS spend: ${total_spend:,.0f}")
print(f"Tools flagged overpriced: {int(overpriced_count)}")
print(f"Tools flagged underutilized: {int(underutilized_count)}")
print(f"Overlap groups: {len(overlap_groups)}")
print(f"Total potential savings: ${total_savings:,.0f}/year")
