from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_unknown_endpoint():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_method_not_allowed():
    response = client.post("/health")
    assert response.status_code == 405
