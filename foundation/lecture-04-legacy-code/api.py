"""
Flask REST API for the modernized accounting system.
Provides /balance, /credit, /debit, and /transactions endpoints.
"""

from decimal import Decimal, InvalidOperation
from flask import Flask, jsonify, request
from flask_cors import CORS

from accounting import Account, AccountType, AccountStatus

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# In-memory demo account (pre-loaded for the lecture demo)
# ---------------------------------------------------------------------------
demo_account = Account(
    number="00001234",
    name="Legacy Corp Operating",
    account_type=AccountType.BUSINESS,
    balance=Decimal("125750.00"),
    status=AccountStatus.ACTIVE,
)


def _account_dict(acct: Account) -> dict:
    return {
        "number": acct.number,
        "name": acct.name,
        "type": acct.account_type.name.lower(),
        "balance": str(acct.balance),
        "status": acct.status.name.lower(),
        "last_activity": (
            acct.last_activity.isoformat() if acct.last_activity else None
        ),
    }


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.route("/balance", methods=["GET"])
def balance():
    try:
        bal = demo_account.get_balance()
        return jsonify({
            "account": _account_dict(demo_account),
            "balance": str(bal),
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/credit", methods=["POST"])
def credit():
    data = request.get_json(silent=True) or {}
    raw = data.get("amount")
    if raw is None:
        return jsonify({"error": "amount is required"}), 400
    try:
        amount = Decimal(str(raw))
    except (InvalidOperation, ValueError):
        return jsonify({"error": "Invalid amount"}), 400

    try:
        new_balance = demo_account.credit(amount)
        return jsonify({
            "account": _account_dict(demo_account),
            "credited": str(amount),
            "new_balance": str(new_balance),
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/debit", methods=["POST"])
def debit():
    data = request.get_json(silent=True) or {}
    raw = data.get("amount")
    if raw is None:
        return jsonify({"error": "amount is required"}), 400
    try:
        amount = Decimal(str(raw))
    except (InvalidOperation, ValueError):
        return jsonify({"error": "Invalid amount"}), 400

    try:
        new_balance = demo_account.debit(amount)
        return jsonify({
            "account": _account_dict(demo_account),
            "debited": str(amount),
            "new_balance": str(new_balance),
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/transactions", methods=["GET"])
def transactions():
    txs = [
        {
            "timestamp": tx.timestamp.isoformat(),
            "type": tx.type.name.lower(),
            "amount": str(tx.amount),
            "result": tx.result.name.lower(),
            "new_balance": str(tx.new_balance),
        }
        for tx in demo_account.transactions
    ]
    return jsonify({"transactions": txs, "count": len(txs)})


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(port=5050, debug=True)
