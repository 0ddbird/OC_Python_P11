import os

from dotenv import load_dotenv

from flask import Flask, Response, flash, redirect, render_template, request, url_for

from db.access import (
    get_club_by_email,
    get_club_by_name,
    get_competition_by_name,
    load_clubs,
    load_competitions,
)
from db.exceptions import ClubNotFoundError, CompetitionNotFoundError

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


def get_max_bookable_slots(available_points: int, available_slots: int) -> int:
    return min(available_points, available_slots)


competitions = load_competitions()
clubs = load_clubs()


@app.route("/showSummary", methods=["POST"])
def show_summary() -> Response:
    email = request.form["email"]
    try:
        club = get_club_by_email(email, clubs)
        return render_template("welcome.html", club=club, competitions=competitions)
    except ClubNotFoundError as e:
        flash(str(e))
        return redirect(url_for("index"))


@app.route("/book/<competition>/<club>")
def book(competition: dict, club: dict) -> Response:
    try:
        club = get_club_by_name(club["name"], clubs)
        competition = get_competition_by_name(competition["name"], competitions)
    except (ClubNotFoundError, CompetitionNotFoundError) as e:
        flash(str(e))
        return render_template("welcome.html", club=club, competitions=competitions)

    max_bookable_slots = get_max_bookable_slots(
        club["points"], competition["available_slots"]
    )
    return render_template(
        "booking.html",
        club=club,
        competition=competition,
        max_bookable_slots=max_bookable_slots,
    )


@app.route("/purchaseSlots", methods=["POST"])
def purchase_slots() -> Response:
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    required_slots = int(request.form["slots"])
    competition["available_slots"] = (
        int(competition["available_slots"]) - required_slots
    )
    flash("Great! Booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display


@app.route("/logout")
def logout() -> Response:
    return redirect(url_for("index"))
