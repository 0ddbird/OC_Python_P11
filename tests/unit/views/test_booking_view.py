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
        assert b"<li>Club not found for name: WrongClubName</li>" in rv.data

    def test_book_route_redirects_when_competition_not_found(self, auth_client):
        rv = auth_client.get(
            "/book/WrongCompetitionName/Club%201",
            follow_redirects=True,
        )

        assert rv.status_code == 200
        assert rv.request.path == "/home"
        assert (
            b"<li>Competition not found for name: WrongCompetitionName</li>" in rv.data
        )

    def test_book_route_renders_when_correct_path(self, auth_client):
        rv = auth_client.get("/book/Competition%204/Club%201")

        assert rv.status_code == 200
        assert b"<title>Booking for Competition 4 || GUDLFT</title>" in rv.data
        # assert the value of competition slots is correct
