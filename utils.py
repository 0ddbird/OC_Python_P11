import json


def load_clubs() -> list[dict]:
    """Utility function to fetch clubs from a json file.

    Returns:
        list[dict]: A list of Club dictionnaries
    """
    with open("clubs.json") as c:
        clubs_list = json.load(c)["clubs"]
        return clubs_list


def load_competitions() -> list[dict]:
    """Utility function to fetch competitions from a json file.

    Returns:
        list[dict]: A list of Competitions dictionnaries
    """
    with open("competitions.json") as comps:
        competitions_list = json.load(comps)["competitions"]
        return competitions_list
