from flask import Response, flash, redirect, render_template, url_for

from data.store import ClubStore, CompetitionStore, ObjectDoesNotExist
from utils import protected_view


@protected_view
def booking_view(competition_name: str, club_name: str) -> Response:
    ClubStore.load()
    CompetitionStore.load()
    try:
        club = ClubStore.get("name", club_name)
        competition = CompetitionStore.get("name", competition_name)
    except ObjectDoesNotExist as e:
        flash(str(e))
        return redirect(url_for("home_route"))

    max_bookable_slots = min(club["points"], competition["available_slots"], 12)
    return render_template(
        "booking.html",
        club=club,
        competition=competition,
        max_bookable_slots=max_bookable_slots,
    )
