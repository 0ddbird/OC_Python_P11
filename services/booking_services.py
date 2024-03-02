from data.store import ClubStore, CompetitionStore


def validate_required_slots(required_slots: any) -> int:
    try:
        return int(required_slots)
    except ValueError:
        raise ValueError("The number of slots to book must be an integer")


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


def purchase_slots(competition, club, slots):
    required_slots = validate_required_slots(slots)
    update_club_points(club, required_slots)
    update_competition_slots(competition, required_slots)
    ClubStore.save()
    CompetitionStore.save()
