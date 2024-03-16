def test_purchase_slot_renders_errors_when_invalid_slot_value(client):
    data = {
        "competition": "Competition 2",
        "club": "Club 1",
        "slots": 0,
    }

    rv = client.post(
        "/purchase-slots",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        follow_redirects=True,
    )

    assert rv.status_code == 200
    assert rv.request.path == "/book/Competition 2/Club 1"
    assert b"<li>The number of slots to book must be a positive integer</li>" in rv.data


def test_purchase_slot_renders_when_successful(client):
    data = {
        "competition": "Competition 2",
        "club": "Club 1",
        "slots": 5,
    }

    rv = client.post(
        "/purchase-slots",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        follow_redirects=True,
    )

    assert rv.status_code == 200
    assert rv.request.path == "/home"
    assert b"Great! Booking complete!" in rv.data
