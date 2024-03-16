def test_clubs_route(client):
    rv = client.get("/clubs")

    assert rv.status_code == 200
    assert b"<title>Clubs || GUDLFT</title>" in rv.data
