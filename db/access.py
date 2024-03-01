import json

from db.exceptions import ClubNotFoundError, CompetitionNotFoundError


def load_clubs() -> list[dict]:
    """Utility function to fetch clubs from a json file.

    Returns:
        list[dict]: A list of Club dictionnaries
    """
    with open("./db/clubs.json") as c:
        clubs_list = json.load(c)["clubs"]
        return clubs_list


def load_competitions() -> list[dict]:
    """Utility function to fetch competitions from a json file.

    Returns:
        list[dict]: A list of Competitions dictionnaries
    """
    with open("./db/competitions.json") as comps:
        competitions_list = json.load(comps)["competitions"]
        return competitions_list


def get_competition_by_name(name: str, competitions: list[dict]) -> dict:
    for competition in competitions:
        if competition["name"] == name:
            return competition
    raise CompetitionNotFoundError(f"Competition not found for name: {name}")


def get_club_by_name(name: str, clubs: list[dict]) -> dict:
    for club in clubs:
        if club["name"] == name:
            return club
    raise ClubNotFoundError(f"Club not found for name: {name}")


def get_club_by_email(email: str, clubs: list[dict]) -> dict:
    for club in clubs:
        if club["email"] == email:
            return club
    raise ClubNotFoundError(f"Club not found for email: {email}")
