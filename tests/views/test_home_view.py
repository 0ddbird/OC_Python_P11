class TestHomeRoute:
    def test_home_route_redirects_when_unauthenticated(self, client):
        rv = client.get("/home")

        assert rv.status_code == 302

    def test_home_route_is_rendered_when_authenticated(self, client):
        rv = client.post(
            "/home",
            data={"email": "secretary@club1.com"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert rv.status_code == 200
        assert b"<title>Home || GUDLFT</title>" in rv.data

    def test_home_route_is_rendered_when_club_does_not_exist(self, client):
        rv = client.post(
            "/home",
            data={"email": "unexisting@email.com"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        assert rv.status_code == 302
