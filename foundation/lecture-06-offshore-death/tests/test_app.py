"""Tests for the registration app with input validation.

Covers:
- Page loading (index, register)
- Successful registration
- Duplicate prevention
- Username validation (length, alphanumeric)
- Email validation (format)
- Password validation (length, digit requirement)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, DB_PATH, validate_registration, _rate_store


@pytest.fixture
def client():
    app.config["TESTING"] = True
    test_db = DB_PATH.parent / "test_users.db"
    import app as app_module
    app_module.DB_PATH = test_db

    # Clear rate limit state between tests
    _rate_store.clear()

    with app.test_client() as client:
        yield client

    if test_db.exists():
        test_db.unlink()


VALID_DATA = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
}


# ── Page Loading ──────────────────────────────────────────────

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


# ── Successful Registration ──────────────────────────────────

def test_register_user(client):
    """Can register a new user with valid data."""
    response = client.post("/register", data=VALID_DATA, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration successful" in response.data


def test_user_appears_in_list(client):
    """Registered user appears on the home page."""
    client.post("/register", data=VALID_DATA)
    response = client.get("/")
    assert b"testuser" in response.data


def test_duplicate_user(client):
    """Cannot register with duplicate username."""
    client.post("/register", data=VALID_DATA)
    response = client.post("/register", data=VALID_DATA, follow_redirects=True)
    assert b"already exists" in response.data


# ── Username Validation ──────────────────────────────────────

def test_username_too_short(client):
    """Username under 3 characters is rejected."""
    data = {**VALID_DATA, "username": "ab"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"between 3 and 20" in response.data


def test_username_too_long(client):
    """Username over 20 characters is rejected."""
    data = {**VALID_DATA, "username": "a" * 21}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"between 3 and 20" in response.data


def test_username_with_spaces(client):
    """Username with spaces is rejected."""
    data = {**VALID_DATA, "username": "bad user"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"letters and numbers" in response.data


def test_username_with_special_chars(client):
    """Username with special characters is rejected."""
    data = {**VALID_DATA, "username": "user@name!"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"letters and numbers" in response.data


def test_username_exactly_3_chars(client):
    """Username at minimum length (3) is accepted."""
    data = {**VALID_DATA, "username": "abc"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"Registration successful" in response.data


def test_username_exactly_20_chars(client):
    """Username at maximum length (20) is accepted."""
    data = {**VALID_DATA, "username": "a" * 20, "email": "long@example.com"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"Registration successful" in response.data


def test_username_empty(client):
    """Empty username is rejected."""
    data = {**VALID_DATA, "username": ""}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"between 3 and 20" in response.data


# ── Email Validation ─────────────────────────────────────────

def test_email_no_at_sign(client):
    """Email without @ is rejected."""
    data = {**VALID_DATA, "email": "bademail.com"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_no_domain(client):
    """Email without domain is rejected."""
    data = {**VALID_DATA, "email": "user@"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_no_tld(client):
    """Email without TLD is rejected."""
    data = {**VALID_DATA, "email": "user@domain"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_empty(client):
    """Empty email is rejected."""
    data = {**VALID_DATA, "email": ""}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_with_spaces(client):
    """Email with spaces is rejected."""
    data = {**VALID_DATA, "email": "user @example.com"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"valid email" in response.data


def test_email_valid_format(client):
    """Standard email format is accepted."""
    data = {**VALID_DATA, "username": "emailtest", "email": "user@company.co.uk"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"Registration successful" in response.data


# ── Password Validation ──────────────────────────────────────

def test_password_too_short(client):
    """Password under 8 characters is rejected."""
    data = {**VALID_DATA, "password": "short1"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"at least 8 characters" in response.data


def test_password_no_digit(client):
    """Password without a digit is rejected."""
    data = {**VALID_DATA, "password": "abcdefghij"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"at least one number" in response.data


def test_password_exactly_8_chars_with_digit(client):
    """Password at minimum length with digit is accepted."""
    data = {**VALID_DATA, "username": "pwtest", "email": "pw@example.com", "password": "abcdefg1"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"Registration successful" in response.data


def test_password_empty(client):
    """Empty password is rejected."""
    data = {**VALID_DATA, "password": ""}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"at least 8 characters" in response.data


def test_password_all_digits(client):
    """All-digit password is accepted (meets both rules)."""
    data = {**VALID_DATA, "username": "digitpw", "email": "digit@example.com", "password": "12345678"}
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"Registration successful" in response.data


# ── Unit Tests for validate_registration() ────────────────────

class TestValidateFunction:
    """Direct unit tests for the validation function."""

    def test_valid_input_returns_empty(self):
        assert validate_registration("gooduser", "user@test.com", "password1") == []

    def test_all_invalid_returns_multiple_errors(self):
        errors = validate_registration("x", "bad", "short")
        assert len(errors) == 3

    def test_username_boundary_3(self):
        assert validate_registration("abc", "a@b.c", "password1") == []

    def test_username_boundary_20(self):
        assert validate_registration("a" * 20, "a@b.c", "password1") == []

    def test_username_boundary_2(self):
        errors = validate_registration("ab", "a@b.c", "password1")
        assert any("3 and 20" in e for e in errors)

    def test_username_boundary_21(self):
        errors = validate_registration("a" * 21, "a@b.c", "password1")
        assert any("3 and 20" in e for e in errors)

    def test_username_underscore_rejected(self):
        errors = validate_registration("user_name", "a@b.c", "password1")
        assert any("letters and numbers" in e for e in errors)

    def test_email_double_at_rejected(self):
        errors = validate_registration("user", "a@@b.c", "password1")
        assert any("valid email" in e for e in errors)

    def test_password_7_chars_rejected(self):
        errors = validate_registration("user", "a@b.c", "passwor")
        assert any("8 characters" in e for e in errors)

    def test_password_8_chars_no_digit_rejected(self):
        errors = validate_registration("user", "a@b.c", "abcdefgh")
        assert any("one number" in e for e in errors)


# ── Rate Limiting ─────────────────────────────────────────────

def test_rate_limit_allows_5(client):
    """First 5 attempts are allowed."""
    for i in range(5):
        data = {**VALID_DATA, "username": f"user{i}", "email": f"u{i}@test.com"}
        response = client.post("/register", data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b"Registration successful" in response.data


def test_rate_limit_blocks_6th(client):
    """6th attempt within 60 seconds is blocked."""
    for i in range(5):
        data = {**VALID_DATA, "username": f"rl{i}", "email": f"rl{i}@test.com"}
        client.post("/register", data=data)

    data = {**VALID_DATA, "username": "blocked", "email": "blocked@test.com"}
    response = client.post("/register", data=data)
    assert response.status_code == 429
    assert b"Too many registration attempts" in response.data


def test_rate_limit_blocks_invalid_attempts_too(client):
    """Invalid submissions also count toward the rate limit."""
    bad_data = {"username": "x", "email": "bad", "password": "1"}
    for _ in range(5):
        client.post("/register", data=bad_data)

    response = client.post("/register", data=VALID_DATA)
    assert response.status_code == 429


def test_rate_limit_resets_after_window(client):
    """After the window expires, attempts are allowed again."""
    import app as app_module
    old_window = app_module.RATE_WINDOW
    app_module.RATE_WINDOW = 0  # expire immediately

    for i in range(6):
        data = {**VALID_DATA, "username": f"reset{i}", "email": f"reset{i}@test.com"}
        response = client.post("/register", data=data, follow_redirects=True)
        assert response.status_code == 200

    app_module.RATE_WINDOW = old_window
