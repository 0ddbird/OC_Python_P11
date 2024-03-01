import pytest

from mocks.competitions import competitions_mock as competitions
from server import CompetitionNotFoundError, get_competition_by_name


def test_get_competition_by_name_found():
    test_name = competitions[0]["name"]
    competition = get_competition_by_name(test_name, competitions)
    assert competition == competitions[0]


def test_get_competition_by_name_not_found():
    unexisting_competition_name = "Unexisting name"

    with pytest.raises(CompetitionNotFoundError) as e:
        get_competition_by_name(unexisting_competition_name, competitions)
    assert (
        str(e.value) == f"Competition not found for name: {unexisting_competition_name}"
    )
