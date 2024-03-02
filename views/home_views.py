from datetime import datetime

from flask import Response, flash, redirect, render_template, request, session, url_for

from data.store import ClubStore, CompetitionStore, ObjectDoesNotExist


def is_active_competition(competition) -> bool:
    competition_date = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    return competition_date > now


def annotate_is_active(competitions: list[dict]) -> list[dict]:
    annotated_competitions = competitions
    for competition in annotated_competitions:
        competition["is_active"] = is_active_competition(competition)
    return annotated_competitions


def home_view() -> Response:
    email = session.get("email", None) or request.form.get("email", None)

    if not email:
        flash("You must be logged in to access this page.")
        return redirect(url_for("index"))

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
