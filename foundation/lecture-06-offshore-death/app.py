"""Simple Flask user registration app — the sprint ticket target.

Input validation added per sprint ticket DEMO-042:
- Email: must contain @ and a valid domain
- Password: 8+ characters with at least one number
- Username: 3-20 characters, alphanumeric only
"""

import re
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "demo-secret-key"

DB_PATH = Path(__file__).parent / "users.db"


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


def validate_registration(username, email, password):
    """Validate registration fields. Returns list of error messages."""
    errors = []

    # Username: 3-20 characters, alphanumeric only
    if not username:
        errors.append("Username is required.")
    elif not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        errors.append("Username must be 3-20 characters and contain only letters and numbers.")

    # Email: must contain @ with a domain
    if not email:
        errors.append("Email is required.")
    elif '@' not in email or '.' not in email.split('@')[-1]:
        errors.append("Please enter a valid email address (e.g., user@example.com).")

    # Password: 8+ characters with at least one number
    if not password:
        errors.append("Password is required.")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    elif not re.search(r'\d', password):
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
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Validate inputs
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
