"""Tests for the registration app WITH input validation.

Covers all validation rules:
- Email: must contain @ and a valid domain
- Password: 8+ characters with at least one number
- Username: 3-20 characters, alphanumeric only
"""

import sys
from pathlib import Path

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, DB_PATH, validate_registration


@pytest.fixture
def client():
    app.config["TESTING"] = True
    # Use a test database
    test_db = DB_PATH.parent / "test_users.db"
    import app as app_module
    app_module.DB_PATH = test_db

    with app.test_client() as client:
        yield client

    # Cleanup
    if test_db.exists():
        test_db.unlink()


# ── Page load tests ──────────────────────────────────────────

def test_index_page(client):
    """Home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"User Management" in response.data


def test_register_page(client):
    """Registration form loads successfully."""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


# ── Successful registration ──────────────────────────────────

def test_register_valid_user(client):
    """Can register a user with valid inputs."""
    response = client.post("/register", data={
        "username": "testuser1",
        "email": "test@example.com",
        "password": "securepass1",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration successful" in response.data


def test_user_appears_in_list(client):
    """Registered user appears on the home page."""
    client.post("/register", data={
        "username": "visible1",
        "email": "visible@example.com",
        "password": "password1",
    })
    response = client.get("/")
    assert b"visible1" in response.data


def test_duplicate_user(client):
    """Cannot register with duplicate username."""
    data = {
        "username": "duplicate1",
        "email": "dup@example.com",
        "password": "password1",
    }
    client.post("/register", data=data)
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"already exists" in response.data


# ── Username validation ──────────────────────────────────────

def test_username_too_short(client):
    """Username under 3 characters is rejected."""
    response = client.post("/register", data={
        "username": "ab",
        "email": "short@example.com",
        "password": "password1",
    }, follow_redirects=True)
    assert b"3-20 characters" in response.data


def test_username_too_long(client):
    """Username over 20 characters is rejected."""
    response = client.post("/register", data={
        "username": "a" * 21,
        "email": "long@example.com",
        "password": "password1",
    }, follow_redirects=True)
    assert b"3-20 characters" in response.data


def test_username_special_chars(client):
    """Username with special characters is rejected."""
    response = client.post("/register", data={
        "username": "user@name!",
        "email": "special@example.com",
        "password": "password1",
    }, follow_redirects=True)
    assert b"letters and numbers" in response.data


def test_username_empty(client):
    """Empty username is rejected."""
    response = client.post("/register", data={
        "username": "",
        "email": "empty@example.com",
        "password": "password1",
    }, follow_redirects=True)
    assert b"Username is required" in response.data


# ── Email validation ─────────────────────────────────────────

def test_email_no_at_sign(client):
    """Email without @ is rejected."""
    response = client.post("/register", data={
        "username": "testuser2",
        "email": "bademail.com",
        "password": "password1",
    }, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_no_domain(client):
    """Email without domain part is rejected."""
    response = client.post("/register", data={
        "username": "testuser3",
        "email": "user@",
        "password": "password1",
    }, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_no_dot_in_domain(client):
    """Email with domain missing dot is rejected."""
    response = client.post("/register", data={
        "username": "testuser4",
        "email": "user@localhost",
        "password": "password1",
    }, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_empty(client):
    """Empty email is rejected."""
    response = client.post("/register", data={
        "username": "testuser5",
        "email": "",
        "password": "password1",
    }, follow_redirects=True)
    assert b"Email is required" in response.data


# ── Password validation ──────────────────────────────────────

def test_password_too_short(client):
    """Password under 8 characters is rejected."""
    response = client.post("/register", data={
        "username": "testuser6",
        "email": "short@example.com",
        "password": "pass1",
    }, follow_redirects=True)
    assert b"at least 8 characters" in response.data


def test_password_no_number(client):
    """Password without a number is rejected."""
    response = client.post("/register", data={
        "username": "testuser7",
        "email": "nonum@example.com",
        "password": "password",
    }, follow_redirects=True)
    assert b"at least one number" in response.data


def test_password_empty(client):
    """Empty password is rejected."""
    response = client.post("/register", data={
        "username": "testuser8",
        "email": "nopw@example.com",
        "password": "",
    }, follow_redirects=True)
    assert b"Password is required" in response.data


# ── Unit tests for validate_registration ─────────────────────

def test_validate_all_valid():
    """No errors for valid input."""
    errors = validate_registration("gooduser", "user@example.com", "password1")
    assert errors == []


def test_validate_multiple_errors():
    """Multiple invalid fields return multiple errors."""
    errors = validate_registration("x", "bad", "short")
    assert len(errors) == 3
