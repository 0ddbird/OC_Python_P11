import pytest

from db.access import get_club_by_email
from mocks.clubs import clubs_mock as clubs
from server import ClubNotFoundError


def test_get_club_by_email_found():
    test_email = clubs[0]["email"]
    club = get_club_by_email(test_email, clubs)
    assert club == clubs[0]


def test_get_club_by_email_not_found():
    unexisting_test_email = "unexisting@email.com"
    with pytest.raises(ClubNotFoundError) as e:
        get_club_by_email(unexisting_test_email, clubs)
    assert str(e.value) == f"Club not found for email: {unexisting_test_email}"
