import pytest

from services.booking_services import update_club_points

club_mock = {
    "name": "Club mock 1",
    "email": "club-mock-1@example.com",
    "points": 5,
}


def test_update_club_points_successful():
    assert update_club_points(club_mock, 4) is None


def test_update_club_points_not_enough_points():
    with pytest.raises(ValueError) as e:
        required_slots = 6
        update_club_points(club_mock, required_slots)
    assert (
        str(e.value) == f"You do not have enough points to book {required_slots} slots."
    )
