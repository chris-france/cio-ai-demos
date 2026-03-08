"""Simple Flask user registration app — the sprint ticket target.

Students will ask Claude Code to add input validation.
This deliberately has NO validation — that's the feature request.
"""

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

        # NO VALIDATION — this is the sprint ticket
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
