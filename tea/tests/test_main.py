from fastapi.testclient import TestClient
from main import main_app

client = TestClient(main_app)


def test_main():
    response = client.get("/api/tea")
    assert response.status_code == 200


def test_tea_by_id():
    response = client.get("/api/tea/1")
    assert response.status_code == 200