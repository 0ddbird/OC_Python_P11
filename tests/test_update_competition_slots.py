import pytest

from services.booking_services import update_competition_slots

competition_mock = {
    "name": "Competition mock 1",
    "date": "2020-03-27 10:00:00",
    "available_slots": 5,
}


def test_update_club_points_successful():
    assert update_competition_slots(competition_mock, 4) is None


def test_update_club_points_not_enough_slots():
    with pytest.raises(ValueError) as e:
        required_slots = 6
        update_competition_slots(competition_mock, required_slots)
    assert (
        str(e.value)
        == f"This competition has less than {required_slots} slots available."
    )
