# tests/test_app.py
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_meals_page(client):
    rv = client.get("/meals")
    assert rv.status_code == 200


def test_create_plan_page(client):
    rv = client.get("/create_plan")
    assert rv.status_code == 200


def test_generate_plan(client):
    rv = client.post("/generate_plan", data={"days": "3"})
    assert rv.status_code == 200
