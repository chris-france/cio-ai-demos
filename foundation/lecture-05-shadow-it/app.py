"""
Financial Planning Application — replaces sample-workbook.xlsx

All business logic that was buried in spreadsheet formulas is now:
- Explicit Python code with type hints
- Testable and version-controlled
- Served via REST API
- Connected to a dashboard

CIO AI Curriculum — Lecture 05: Shadow IT → Real Application
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder=".")


# ═══ Domain Models ════════════════════════════════════════════

class AccountType(Enum):
    CHECKING = "C"
    SAVINGS = "S"
    BUSINESS = "B"


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class Assumption:
    parameter: str
    value: float
    last_updated: date
    updated_by: str
    description: str

    @property
    def age_years(self) -> float:
        return round((date.today() - self.last_updated).days / 365.25, 1)

    @property
    def is_stale(self) -> bool:
        return self.age_years >= 2.0

    @property
    def severity(self) -> str:
        if self.age_years >= 4:
            return "CRITICAL"
        if self.age_years >= 2:
            return "HIGH"
        return "OK"

    def to_dict(self) -> dict:
        return {
            "parameter": self.parameter,
            "value": self.value,
            "last_updated": self.last_updated.isoformat(),
            "updated_by": self.updated_by,
            "description": self.description,
            "age_years": self.age_years,
            "is_stale": self.is_stale,
            "severity": self.severity,
        }


@dataclass
class MonthlyRevenue:
    month: str
    product_a: float
    product_b: float
    product_c: float
    prior_year_total: Optional[float] = None

    @property
    def total(self) -> float:
        return self.product_a + self.product_b + self.product_c

    @property
    def yoy_growth(self) -> Optional[float]:
        """Calculated from actual data — NOT hardcoded like the spreadsheet."""
        if self.prior_year_total and self.prior_year_total > 0:
            return (self.total - self.prior_year_total) / self.prior_year_total
        return None

    def to_dict(self) -> dict:
        return {
            "month": self.month,
            "product_a": self.product_a,
            "product_b": self.product_b,
            "product_c": self.product_c,
            "total": self.total,
            "yoy_growth": round(self.yoy_growth, 4) if self.yoy_growth is not None else None,
            "prior_year_total": self.prior_year_total,
        }


@dataclass
class Department:
    name: str
    headcount: int
    avg_salary: float
    benefits_rate: float
    actual_overhead: float  # From GL data, not hardcoded

    @property
    def total_comp(self) -> float:
        return self.headcount * self.avg_salary * (1 + self.benefits_rate)

    @property
    def fully_loaded(self) -> float:
        return self.total_comp * (1 + self.actual_overhead)

    def revenue_share(self, total_revenue: float) -> float:
        if total_revenue <= 0:
            return 0
        return self.fully_loaded / total_revenue

    def to_dict(self, total_revenue: float) -> dict:
        return {
            "name": self.name,
            "headcount": self.headcount,
            "avg_salary": self.avg_salary,
            "benefits_rate": self.benefits_rate,
            "total_comp": round(self.total_comp, 2),
            "overhead_pct": self.actual_overhead,
            "fully_loaded": round(self.fully_loaded, 2),
            "revenue_share": round(self.revenue_share(total_revenue), 4),
        }


@dataclass
class VendorContract:
    name: str
    annual_cost: float
    users: int
    contract_end: date
    auto_renew: bool
    utilization: float

    @property
    def cost_per_user(self) -> float:
        return self.annual_cost / self.users if self.users > 0 else 0

    @property
    def days_to_expiry(self) -> int:
        return (self.contract_end - date.today()).days

    @property
    def risk_score(self) -> RiskLevel:
        """Business rule — extracted from nested IF formula, now readable and testable."""
        if self.utilization < 0.5 and self.auto_renew:
            return RiskLevel.HIGH
        if self.utilization < 0.5:
            return RiskLevel.MEDIUM
        if self.utilization > 0.8 and self.annual_cost < 50000:
            return RiskLevel.LOW
        return RiskLevel.MEDIUM

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "annual_cost": self.annual_cost,
            "users": self.users,
            "cost_per_user": round(self.cost_per_user, 2),
            "contract_end": self.contract_end.isoformat(),
            "days_to_expiry": self.days_to_expiry,
            "auto_renew": self.auto_renew,
            "utilization": self.utilization,
            "risk_score": self.risk_score.value,
        }


# ═══ Data Layer (replaces spreadsheet cells) ═════════════════

assumptions = [
    Assumption("Tax Rate", 0.21, date(2022, 1, 15), "jsmith", "Federal corporate tax rate"),
    Assumption("Discount Rate", 0.08, date(2021, 6, 30), "UNKNOWN", "DCF discount rate for NPV calculations"),
    Assumption("Growth Target", 0.15, date(2023, 3, 1), "cfo_direct", "Annual revenue growth target"),
    Assumption("Inflation Adj", 0.035, date(2020, 12, 1), "UNKNOWN", "Cost inflation adjustment factor"),
    Assumption("FX Rate EUR/USD", 1.08, date(2024, 2, 15), "treasury", "Euro to USD exchange rate"),
    Assumption("Benefits Load", 0.30, date(2019, 8, 22), "hr_admin", "Benefits as % of salary"),
    Assumption("Contingency %", 0.10, date(2021, 11, 1), "UNKNOWN", "Budget contingency reserve"),
]

# Prior year actuals — the spreadsheet had NONE of this, growth was hardcoded
prior_year = [220000, 240000, 225000, 210000, 230000, 260000,
              235000, 245000, 265000, 280000, 275000, 310000]

revenue_data = [
    MonthlyRevenue("Jan", 120000, 85000, 45000, prior_year[0]),
    MonthlyRevenue("Feb", 135000, 92000, 52000, prior_year[1]),
    MonthlyRevenue("Mar", 142000, 78000, 48000, prior_year[2]),
    MonthlyRevenue("Apr", 128000, 95000, 55000, prior_year[3]),
    MonthlyRevenue("May", 155000, 88000, 62000, prior_year[4]),
    MonthlyRevenue("Jun", 168000, 102000, 58000, prior_year[5]),
    MonthlyRevenue("Jul", 145000, 97000, 67000, prior_year[6]),
    MonthlyRevenue("Aug", 152000, 105000, 72000, prior_year[7]),
    MonthlyRevenue("Sep", 178000, 112000, 68000, prior_year[8]),
    MonthlyRevenue("Oct", 192000, 98000, 75000, prior_year[9]),
    MonthlyRevenue("Nov", 185000, 115000, 82000, prior_year[10]),
    MonthlyRevenue("Dec", 210000, 125000, 95000, prior_year[11]),
]

departments = [
    Department("Engineering", 45, 142000, 0.32, 0.15),
    Department("Sales", 28, 95000, 0.28, 0.22),
    Department("Marketing", 15, 88000, 0.25, 0.18),
    Department("Finance", 8, 105000, 0.30, 0.10),
    Department("HR", 6, 92000, 0.28, 0.08),
    Department("Operations", 18, 85000, 0.25, 0.20),
    Department("Executive", 4, 225000, 0.35, 0.05),
]

vendors = [
    VendorContract("Salesforce", 285000, 28, date(2025, 12, 31), True, 0.72),
    VendorContract("Microsoft 365", 156000, 124, date(2026, 3, 15), True, 0.91),
    VendorContract("AWS", 480000, 45, date(2025, 6, 30), False, 0.65),
    VendorContract("Slack", 42000, 124, date(2025, 9, 30), True, 0.88),
    VendorContract("Jira", 36000, 65, date(2026, 1, 31), True, 0.78),
    VendorContract("Zoom", 28000, 124, date(2025, 8, 15), True, 0.45),
    VendorContract("HubSpot", 72000, 15, date(2025, 11, 30), True, 0.52),
    VendorContract("Datadog", 96000, 12, date(2026, 2, 28), False, 0.83),
    VendorContract("DocuSign", 18000, 35, date(2025, 7, 31), True, 0.35),
    VendorContract("Figma", 24000, 8, date(2025, 10, 31), True, 0.90),
]


# ═══ Computed Summary (replaces Summary sheet) ═══════════════

def compute_summary() -> dict:
    total_revenue = sum(r.total for r in revenue_data)
    total_costs = sum(d.fully_loaded for d in departments)
    gross_margin = total_revenue - total_costs
    margin_pct = gross_margin / total_revenue if total_revenue > 0 else 0
    vendor_spend = sum(v.annual_cost for v in vendors)
    vendor_pct = vendor_spend / total_revenue if total_revenue > 0 else 0

    # Get assumption values
    contingency = next((a.value for a in assumptions if a.parameter == "Contingency %"), 0.10)
    discount_rate = next((a.value for a in assumptions if a.parameter == "Discount Rate"), 0.08)
    adjusted_margin = gross_margin * (1 - contingency) * (1 + discount_rate)

    cumulative = []
    running = 0
    for r in revenue_data:
        running += r.total
        cumulative.append(running)

    return {
        "total_revenue": round(total_revenue, 2),
        "total_costs": round(total_costs, 2),
        "gross_margin": round(gross_margin, 2),
        "margin_pct": round(margin_pct, 4),
        "vendor_spend": round(vendor_spend, 2),
        "vendor_pct": round(vendor_pct, 4),
        "adjusted_margin": round(adjusted_margin, 2),
        "headcount": sum(d.headcount for d in departments),
        "stale_assumptions": sum(1 for a in assumptions if a.is_stale),
        "high_risk_vendors": sum(1 for v in vendors if v.risk_score == RiskLevel.HIGH),
        "cumulative_revenue": cumulative,
    }


# ═══ API Routes ═══════════════════════════════════════════════

@app.route("/")
def serve_ui():
    return send_from_directory(".", "dashboard.html")


@app.route("/api/summary")
def api_summary():
    return jsonify(compute_summary())


@app.route("/api/revenue")
def api_revenue():
    return jsonify([r.to_dict() for r in revenue_data])


@app.route("/api/departments")
def api_departments():
    total_rev = sum(r.total for r in revenue_data)
    return jsonify([d.to_dict(total_rev) for d in departments])


@app.route("/api/vendors")
def api_vendors():
    return jsonify([v.to_dict() for v in vendors])


@app.route("/api/assumptions")
def api_assumptions():
    return jsonify([a.to_dict() for a in assumptions])


if __name__ == "__main__":
    print("Financial Planning Dashboard on http://localhost:5055")
    print("Replaces: sample-workbook.xlsx (5 sheets → 5 API endpoints)")
    app.run(host="0.0.0.0", port=5055, debug=True)
