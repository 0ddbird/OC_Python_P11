from random import randint

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 1)
    host = "http://localhost:5000"

    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def load_home(self):
        self.client.get("/home", headers={"email": "a@b.c"})

    @task
    def load_clubs(self):
        self.client.get("/clubs")

    @task
    def load_booking(self):
        competition_name = f"Competition {randint(1, 10)}"
        club_id = randint(1, 50)
        club_name = f"Club {club_id}"
        self.client.get(
            f"/book/{competition_name}/{club_name}",
            headers={"email": f"secretary@club{club_id}.com"},
        )

    @task
    def purchase_slot(self):
        competition_name = f"Competition {randint(1, 10)}"
        club_name = f"Club {randint(1, 5)}"
        slots = randint(1, 5)

        data = {"competition": competition_name, "club": club_name, "slots": slots}

        self.client.post(
            "/purchase-slots",
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
