from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "FastAPI GitHub Actions Demo"
    }


def test_hello():
    response = client.get("/api/hello")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Hello from my DEV branch!"
    assert data["version"] == "999.0.0"


def test_status():
    response = client.get("/api/status")

    assert response.status_code == 200

    assert response.json()["status"] == "ok"
