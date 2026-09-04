"""Simple Flask user registration app with input validation.

Validation rules:
- Username: 3-20 characters, alphanumeric only
- Email: must contain @ with a domain part
- Password: 8+ characters with at least one digit
"""

import re
import time
from collections import defaultdict
from threading import Lock

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "demo-secret-key"

DB_PATH = Path(__file__).parent / "users.db"

# ── Rate Limiting ─────────────────────────────────────────────
# Max 5 registration attempts per IP per 60-second window

RATE_LIMIT = 5
RATE_WINDOW = 60  # seconds

_rate_store: dict[str, list[float]] = defaultdict(list)
_rate_lock = Lock()


def check_rate_limit(ip: str) -> tuple[bool, int]:
    """Check if IP has exceeded the rate limit.

    Returns (allowed, remaining_attempts).
    """
    now = time.time()
    cutoff = now - RATE_WINDOW

    with _rate_lock:
        # Prune old entries
        _rate_store[ip] = [t for t in _rate_store[ip] if t > cutoff]
        count = len(_rate_store[ip])

        if count >= RATE_LIMIT:
            return False, 0

        _rate_store[ip].append(now)
        return True, RATE_LIMIT - count - 1


def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    conn.row_factory = sqlite3.Row
    return conn


def validate_registration(username: str, email: str, password: str) -> list[str]:
    """Validate registration fields. Returns a list of error messages (empty = valid)."""
    errors = []

    # Username: 3-20 characters, alphanumeric only
    if len(username) < 3 or len(username) > 20:
        errors.append("Username must be between 3 and 20 characters.")
    elif not username.isalnum():
        errors.append("Username must contain only letters and numbers.")

    # Email: must contain @ with something before and after
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        errors.append("Please enter a valid email address.")

    # Password: 8+ characters with at least one digit
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    elif not re.search(r"\d", password):
        errors.append("Password must contain at least one number.")

    return errors


@app.route("/")
def index():
    db = get_db()
    users = db.execute("SELECT id, username, email, created_at FROM users ORDER BY id DESC").fetchall()
    db.close()
    return render_template("index.html", users=users)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ip = request.remote_addr or "unknown"
        allowed, remaining = check_rate_limit(ip)
        if not allowed:
            flash("Too many registration attempts. Please wait 60 seconds.", "error")
            return render_template("register.html"), 429

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        errors = validate_registration(username, email, password)
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("register.html")

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password),
            )
            db.commit()
            flash("Registration successful!", "success")
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            flash("Username or email already exists.", "error")
        finally:
            db.close()

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
