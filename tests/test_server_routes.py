from random import randint

import pytest

from server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_home_route_redirects_when_unauthenticated(client):
    rv = client.get("/home")
    assert rv.status_code == 302


def test_home_route_is_rendered_when_authenticated(client):
    rv = client.post(
        "/home",
        data={"email": "secretary@club1.com"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert rv.status_code == 200


def test_home_route_is_rendered_when_club_does_not_exist(client):
    rv = client.post(
        "/home",
        data={"email": "unexisting@email.com"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert rv.status_code == 302


def test_book_route_redirects_when_unauthenticated(client):
    rv = client.get("/book/Competition%201/Club%201")
    assert rv.status_code == 302


def test_clubs_route(client):
    rv = client.get("/clubs")
    assert rv.status_code == 200


def test_purchase_slot(client):
    competition_name = f"Competition {randint(1, 10)}"
    club_name = f"Club {randint(1, 5)}"
    slots = randint(1, 5)
    data = {
        "competition": competition_name,
        "club": club_name,
        "slots": slots,
    }
    rv = client.post(
        "/purchase-slots",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert rv.status_code == 302


def test_logout_route(client):
    with client.session_transaction() as session:
        session["email"] = "user@example.com"
    rv = client.get("/logout", follow_redirects=True)

    assert rv.status_code == 200

    with client.session_transaction() as session:
        assert "email" not in session
