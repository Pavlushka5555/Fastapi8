# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app
from db.session import engine
from app.models import Base
from app.main import SessionLocal

# ������� ��������� ������� ��� ������������ API
client = TestClient(app)



# ���������� �������� ��� ������� � ���� ������
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ���� �������� ������ ������������
def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"

# ���� ��������� ������ ���� ���������
def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 0

# ���� ���������� ��������
def test_create_item(session):
    response = client.post("/items/", json={"title": "Test Item", "description": "This is a test item"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"
    assert response.json()["description"] == "This is a test item"
