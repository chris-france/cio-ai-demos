"""
Flask REST API for the modernized accounting system.

Endpoints:
    POST /login    { "username": "...", "password": "..." }  → JWT token
    GET  /balance/<account_number>       (requires JWT)
    GET  /transactions/<account_number>  (requires JWT)
    POST /credit   { "account_number": "...", "amount": ... }  (requires JWT)
    POST /debit    { "account_number": "...", "amount": ... }  (requires JWT)
"""

import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from functools import wraps

import jwt
from flask import Flask, jsonify, request, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

from accounting import Account, AccountStatus, AccountType

app = Flask(__name__, static_folder=".")

# Swagger UI at /docs
swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs",
    "/swagger.json",
    config={"app_name": "Accounting System API", "tryItOutEnabled": True},
)
app.register_blueprint(swaggerui_blueprint, url_prefix="/docs")

# Secret key for JWT signing (demo only — use env var in production)
JWT_SECRET = os.environ.get("JWT_SECRET", "cio-ai-demo-secret-2026")
JWT_EXPIRY_MINUTES = 30

# Demo user store (plaintext passwords — demo only)
USERS = {
    "admin": {"password": "admin123", "role": "admin", "name": "System Admin"},
    "teller": {"password": "teller123", "role": "teller", "name": "Bank Teller"},
    "auditor": {"password": "auditor123", "role": "auditor", "name": "Compliance Auditor"},
}


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


def require_auth(f):
    """Decorator that validates JWT token from Authorization header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header."}), 401

        token = auth_header[7:]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            request.user = payload
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired. Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token."}), 401

        return f(*args, **kwargs)
    return decorated


# ── Public routes ─────────────────────────────────────────────

@app.route("/")
def serve_ui():
    return send_from_directory(".", "index.html")


@app.route("/swagger.json")
def serve_swagger():
    return send_from_directory(".", "swagger.json")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password."}), 400

    username = data["username"]
    user = USERS.get(username)

    if not user or user["password"] != data["password"]:
        return jsonify({"error": "Invalid credentials."}), 401

    payload = {
        "sub": username,
        "name": user["name"],
        "role": user["role"],
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRY_MINUTES),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return jsonify({
        "token": token,
        "user": username,
        "name": user["name"],
        "role": user["role"],
        "expires_in": JWT_EXPIRY_MINUTES * 60,
    }), 200


# ── In-memory account store (replaces ACCOUNTS.DAT) ──────────

accounts: dict[str, Account] = {
    "00001234": Account(
        number="00001234",
        name="JOHN DOE",
        account_type=AccountType.CHECKING,
        balance=Decimal("5000.00"),
        status=AccountStatus.ACTIVE,
    ),
    "00005678": Account(
        number="00005678",
        name="JANE SMITH",
        account_type=AccountType.SAVINGS,
        balance=Decimal("10000.00"),
        status=AccountStatus.ACTIVE,
    ),
    "00009999": Account(
        number="00009999",
        name="LEGACY CORP",
        account_type=AccountType.BUSINESS,
        balance=Decimal("250000.00"),
        status=AccountStatus.ACTIVE,
    ),
}


def _get_account(account_number: str) -> Account:
    acct = accounts.get(account_number)
    if acct is None:
        raise KeyError("Account not found.")
    return acct


# ── Protected routes ──────────────────────────────────────────

@app.route("/balance/<account_number>", methods=["GET"])
@require_auth
def balance(account_number: str):
    try:
        acct = _get_account(account_number)
        info = acct.view_balance()
        info["balance"] = str(info["balance"])
        return jsonify(info), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/transactions/<account_number>", methods=["GET"])
@require_auth
def transactions(account_number: str):
    try:
        acct = _get_account(account_number)
        last_10 = acct.transaction_log[-10:]
        return jsonify({
            "account_number": acct.number,
            "transactions": [
                {
                    "timestamp": t.timestamp.isoformat(),
                    "type": t.transaction_type.value,
                    "amount": str(t.amount),
                    "result": t.result.value,
                    "new_balance": str(t.new_balance),
                }
                for t in reversed(last_10)
            ],
        }), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404


@app.route("/credit", methods=["POST"])
@require_auth
def credit():
    data = request.get_json()
    if not data or "account_number" not in data or "amount" not in data:
        return jsonify({"error": "Missing account_number or amount."}), 400

    try:
        acct = _get_account(data["account_number"])
        amount = Decimal(str(data["amount"]))
        new_balance = acct.credit(amount)
        return jsonify({
            "account_number": acct.number,
            "credited": str(amount),
            "new_balance": str(new_balance),
        }), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404
    except (ValueError, InvalidOperation) as e:
        return jsonify({"error": str(e)}), 400


@app.route("/debit", methods=["POST"])
@require_auth
def debit():
    data = request.get_json()
    if not data or "account_number" not in data or "amount" not in data:
        return jsonify({"error": "Missing account_number or amount."}), 400

    try:
        acct = _get_account(data["account_number"])
        amount = Decimal(str(data["amount"]))
        new_balance = acct.debit(amount)
        return jsonify({
            "account_number": acct.number,
            "debited": str(amount),
            "new_balance": str(new_balance),
        }), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404
    except (ValueError, InvalidOperation) as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    print("Accounting API running on http://localhost:5050")
    print("Sample accounts: 00001234, 00005678, 00009999")
    print("Demo logins: admin/admin123, teller/teller123, auditor/auditor123")
    app.run(host="0.0.0.0", port=5050, debug=True)
