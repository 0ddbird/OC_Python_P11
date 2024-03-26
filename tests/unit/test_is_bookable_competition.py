from datetime import datetime, timedelta

from views.home_views import is_active_competition


def test_book_open_competition_successful():
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%Y-%m-%d %H:%M:%S")

    competition = {
        "name": "Fall Classic",
        "date": tomorrow_str,
        "available_slots": 5,
    }
    assert is_active_competition(competition) is True


def test_book_ended_competition_forbidden():
    competition = {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "available_slots": 5,
    }
    assert is_active_competition(competition) is False
