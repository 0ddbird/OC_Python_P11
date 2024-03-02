from views.booking_views import get_max_bookable_slots


def test_get_max_bookable_slots_returns_min_value():
    club_points = 10
    competition_slots = 5
    assert get_max_bookable_slots(club_points, competition_slots) == 5


def test_get_max_bookable_slots_is_under_thirteen():
    club_points = 14
    competition_slots = 14
    assert get_max_bookable_slots(club_points, competition_slots) < 13
