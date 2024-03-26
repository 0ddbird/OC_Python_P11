def test_logout_route(client):
    with client.session_transaction() as session:
        session["email"] = "user@example.com"

    rv = client.get("/logout", follow_redirects=True)

    assert rv.status_code == 200

    with client.session_transaction() as session:
        assert "email" not in session
