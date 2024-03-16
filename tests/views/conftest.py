import pytest

from server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def auth_client(client):
    with client.session_transaction() as session:
        session["email"] = "secretary@club1.com"
    return client
