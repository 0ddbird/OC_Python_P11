import os

from dotenv import load_dotenv

from flask import Flask, Response, flash, redirect, render_template, request, url_for

from db.access import (
    get_club_by_email,
    get_club_by_name,
    get_competition_by_name,
    update_club_points,
    update_clubs,
    update_competition_slots,
    update_competitions,
    CLUBS,
    COMPETITIONS,
)
from db.exceptions import ClubNotFoundError, CompetitionNotFoundError

from utils import FormContentError, get_name_from_form

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


def get_max_bookable_slots(available_points: int, available_slots: int) -> int:
    return min(available_points, available_slots)


@app.route("/showSummary", methods=["POST"])
def show_summary() -> Response:
    email = request.form["email"]
    try:
        club = get_club_by_email(email, CLUBS)
        return render_template("welcome.html", club=club, competitions=COMPETITIONS)
    except ClubNotFoundError as e:
        flash(str(e))
        return redirect(url_for("index"))


@app.route("/book/<competition_name>/<club_name>")
def book(competition_name: str, club_name: str) -> Response:
    try:
        club = get_club_by_name(club_name, CLUBS)
        competition = get_competition_by_name(competition_name, COMPETITIONS)
    except (ClubNotFoundError, CompetitionNotFoundError) as e:
        flash(str(e))
        return render_template("welcome.html", club=club, competitions=COMPETITIONS)

    max_bookable_slots = get_max_bookable_slots(
        club["points"], competition["available_slots"]
    )
    return render_template(
        "booking.html",
        club=club,
        competition=competition,
        max_bookable_slots=max_bookable_slots,
    )


def validate_required_slots(required_slots: any) -> int:
    try:
        return int(required_slots)
    except ValueError:
        raise ValueError("The number of slots to book must be an integer")


@app.route("/purchaseSlots", methods=["POST"])
def purchase_slots() -> Response:
    try:
        competition_name = get_name_from_form(request.form, "competition")
        club_name = get_name_from_form(request.form, "club")
        club = get_club_by_name(club_name, CLUBS)
        competition = get_competition_by_name(competition_name, COMPETITIONS)
        required_slots = validate_required_slots(request.form["slots"])
        update_club_points(club, required_slots)
        update_competition_slots(competition, required_slots)
        update_clubs()
        update_competitions()
    except (
        FormContentError,
        ClubNotFoundError,
        CompetitionNotFoundError,
        ValueError,
    ) as e:
        flash(str(e))
        return redirect(f"/book/{competition_name}/{club_name}")

    flash("Great! Booking complete!")
    return render_template("welcome.html", club=club, competitions=COMPETITIONS)


# TODO: Add route for points display


@app.route("/logout")
def logout() -> Response:
    return redirect(url_for("index"))
