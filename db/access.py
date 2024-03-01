import json

from db.exceptions import ClubNotFoundError, CompetitionNotFoundError


def read_clubs() -> list[dict]:
    """Utility function to fetch clubs from a json file.

    Returns:
        list[dict]: A list of Club dictionnaries
    """
    with open("./db/clubs.json") as c:
        clubs_list = json.load(c)["clubs"]
        return clubs_list


def read_competitions() -> list[dict]:
    """Utility function to fetch competitions from a json file.

    Returns:
        list[dict]: A list of Competitions dictionnaries
    """
    with open("./db/competitions.json") as comps:
        competitions_list = json.load(comps)["competitions"]
        return competitions_list


CLUBS = read_clubs()
COMPETITIONS = read_competitions()


def update_clubs():
    with open("./db/clubs.json", "w") as c:
        json.dump({"clubs": CLUBS}, c, indent=4)


def update_competitions():
    with open("./db/competitions.json", "w") as comps:
        json.dump({"competitions": COMPETITIONS}, comps, indent=4)


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


def update_club_points(club, required_slots: int):
    available_points = club["points"]
    if required_slots > available_points:
        raise ValueError(
            f"You do not have enough points to book {required_slots} slots."
        )
    club["points"] -= required_slots


def update_competition_slots(competition, required_slots: int):
    available_slots = competition["available_slots"]
    if required_slots > available_slots:
        raise ValueError(
            f"This competition has less than {required_slots} slots available."
        )
    competition["available_slots"] -= required_slots
