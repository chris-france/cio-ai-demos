"""Basic tests for the registration app.

Students will ask Claude Code to add validation tests.
These initial tests verify the app works WITHOUT validation.
"""

import sys
from pathlib import Path

# Add parent dir to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app import app, DB_PATH


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


def test_register_user(client):
    """Can register a new user."""
    response = client.post("/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration successful" in response.data


def test_duplicate_user(client):
    """Cannot register with duplicate username."""
    data = {
        "username": "duplicate",
        "email": "dup@example.com",
        "password": "password123",
    }
    client.post("/register", data=data)
    response = client.post("/register", data=data, follow_redirects=True)
    assert b"already exists" in response.data


def test_user_appears_in_list(client):
    """Registered user appears on the home page."""
    client.post("/register", data={
        "username": "visible_user",
        "email": "visible@example.com",
        "password": "password123",
    })
    response = client.get("/")
    assert b"visible_user" in response.data
