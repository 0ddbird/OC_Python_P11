from mocks.clubs import club_mock_1 as club_mock
from mocks.competitions import competition_mock_1 as competition_mock
from server import get_max_bookable_slots


def test_get_max_bookable_slots_returns_min_value():
    club_points = club_mock["points"]
    competition_slots = competition_mock["available_slots"]
    assert get_max_bookable_slots(club_points, competition_slots) == min(
        club_points, competition_slots
    )
