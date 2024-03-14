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


class TestBookingRoute:
    def test_book_route_redirects_when_user_not_authenticated(self, client):
        rv = client.get(
            "/book/Competition%204/Club%201",
            follow_redirects=True,
        )
        assert rv.status_code == 200
        assert rv.request.path == "/"

    def test_book_route_redirects_when_club_not_found(self, auth_client):
        rv = auth_client.get(
            "/book/Competition%204/WrongClubName",
            follow_redirects=True,
        )
        assert rv.status_code == 200
        assert rv.request.path == "/home"

    def test_book_route_redirects_when_competition_not_found(self, auth_client):
        rv = auth_client.get(
            "/book/WrongCompetitionName/Club%201",
            follow_redirects=True,
        )
        assert rv.status_code == 200
        assert rv.request.path == "/home"

    def test_book_route_renders_when_correct_path(self, auth_client):
        rv = auth_client.get("/book/Competition%204/Club%201")
        assert rv.status_code == 200
