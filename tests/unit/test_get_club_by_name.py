import pytest

from mocks.clubs import clubs_mock as clubs
from server import ClubNotFoundError, get_club_by_name


def test_get_club_by_name_found():
    test_name = clubs[0]["name"]

    club = get_club_by_name(test_name, clubs)
    assert club == clubs[0]


def test_get_club_by_name_not_found():
    unexisting_test_name = "Unexisting name"
    with pytest.raises(ClubNotFoundError) as e:
        get_club_by_name(unexisting_test_name, clubs)
    assert str(e.value) == f"Club not found for name: {unexisting_test_name}"
