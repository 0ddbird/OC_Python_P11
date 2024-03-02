from datetime import datetime

from flask import Response, flash, redirect, render_template, url_for, session, request

from data.store import ClubStore, CompetitionStore, ObjectDoesNotExist
from utils import protected_view


def is_active_competition(competition) -> bool:
    competition_date = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    return competition_date > now


def annotate_is_active(competitions: list[dict]) -> list[dict]:
    annotated_competitions = competitions
    for competition in annotated_competitions:
        competition["is_active"] = is_active_competition(competition)
    return annotated_competitions


@protected_view
def home_view() -> Response:
    if request.method == "POST":
        session["email"] = request.form["email"]

    email = session.get("email")

    ClubStore.load()
    CompetitionStore.load()
    try:
        club = ClubStore.get("email", email)
        competitions = CompetitionStore.get_all()
        competitions = annotate_is_active(competitions)
        return render_template("home.html", club=club, competitions=competitions)
    except ObjectDoesNotExist as e:
        flash(str(e))
        return redirect(url_for("index"))
