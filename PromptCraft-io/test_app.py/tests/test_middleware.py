import pytest
from flask import Flask
from middlewares import register_middlewares


@pytest.fixture
def client():
    app = Flask(__name__)
    register_middlewares(app)

    @app.route("/secure-endpoint")
    def secure():
        return "Access granted"

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_access_denied_without_token(client):
    response = client.get("/secure-endpoint")
    assert response.status_code == 403
    assert response.get_json() == {"error": "Access denied"}


def test_access_granted_with_token(client):
    response = client.get(
        "/secure-endpoint",
        headers={"X-Auth-Token": "valid-token"}
    )
    assert response.status_code == 200
    assert response.data.decode() == "Access granted"
