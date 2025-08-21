import importlib
import pytest
from fastapi.testclient import TestClient
import app.main as main


@pytest.fixture
def client():
    importlib.reload(main)
    return TestClient(main.app)


def test_create_and_get_course(client):
    response = client.post("/courses", json={"title": "Test Course", "description": "Desc"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Course"

    response = client.get("/courses/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Course"


def test_list_courses(client):
    client.post("/courses", json={"title": "Course1", "description": "Desc"})
    client.post("/courses", json={"title": "Course2", "description": "Desc"})
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_homepage_lists_courses(client):
    client.post("/courses", json={"title": "HTML Course", "description": "Desc"})
    response = client.get("/")
    assert response.status_code == 200
    assert "HTML Course" in response.text
