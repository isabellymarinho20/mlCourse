from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_contains_predict():
    response = client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()

    assert "/predict" in schema["paths"]
    assert "post" in schema["paths"]["/predict"]