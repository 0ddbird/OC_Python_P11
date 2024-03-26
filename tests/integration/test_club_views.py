from flask.testing import FlaskClient
from pytest import fixture
from unittest.mock import patch
from server import app


@fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("data.store.ClubStore.load")
def test_club_view(mock_load, client: FlaskClient):
    rv = client.get("/clubs")

    # Assert the inner function of club_view is called
    mock_load.assert_called_once()

    # Assert the status code and the page content
    assert rv.status_code == 200
    assert b"<title>Clubs || GUDLFT</title>" in rv.data
