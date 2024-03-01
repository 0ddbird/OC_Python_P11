from unittest.mock import patch

import pytest

from mocks.clubs import clubs_mock
from server import ClubNotFoundError, get_club_by_email


def test_get_club_by_email_found():
    test_email = clubs_mock[0]["email"]
    with patch("server.clubs", clubs_mock):
        club = get_club_by_email(test_email)
        assert club == clubs_mock[0]


def test_get_club_by_email_not_found():
    test_email = "unregistered@email.com"
    with patch("server.clubs", clubs_mock):
        with pytest.raises(ClubNotFoundError) as e:
            get_club_by_email(test_email)
        assert str(e.value) == f"Club not found for email: {test_email}"
