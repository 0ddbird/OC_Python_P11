from datetime import datetime
from random import randint

from data.store import ClubStore, CompetitionStore


def generate_random_date_string(start_year=2023, end_year=2025):
    year = randint(start_year, end_year)
    month = randint(1, 12)
    day = randint(1, 28)
    hour = randint(0, 23)
    minute = randint(0, 59)
    second = randint(0, 59)
    random_date = datetime(year, month, day, hour, minute, second)
    date_string = random_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_string


def populate_clubs():
    ClubStore.objects = [
        {
            "name": f"Club {i}",
            "email": f"secretary@club{i}.com",
            "points": randint(0, 50),
        }
        for i in range(1, 51)
    ]
    ClubStore.save()


def populate_competitions():
    CompetitionStore.objects = [
        {
            "name": f"Competition {i}",
            "date": generate_random_date_string(),
            "available_slots": randint(0, 100),
        }
        for i in range(1, 101)
    ]
    CompetitionStore.save()
