import os

from dotenv import load_dotenv

from flask import Flask, Response, flash, redirect, render_template, request, url_for

from utils import load_clubs, load_competitions

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

competitions = load_competitions()
clubs = load_clubs()


@app.route("/")
def index():
    return render_template("index.html")


class ClubNotFoundError(Exception):
    pass


def get_club_by_email(email: str) -> dict:
    for club in clubs:
        if club["email"] == email:
            return club
    raise ClubNotFoundError(f"Club not found for email: {email}")


@app.route("/showSummary", methods=["POST"])
def show_summary() -> Response:
    email = request.form["email"]
    try:
        club = get_club_by_email(email)
        return render_template("welcome.html", club=club, competitions=competitions)
    except ClubNotFoundError as e:
        flash(str(e))
        return redirect(url_for("index"))


@app.route("/book/<competition>/<club>")
def book(competition: str, club: str) -> Response:
    found_club = [c for c in clubs if c["name"] == club][0]
    found_competition = [c for c in competitions if c["name"] == competition][0]
    if found_club and found_competition:
        return render_template(
            "booking.html", club=found_club, competition=found_competition
        )
    else:
        flash("Something went wrong, please try again.")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places() -> Response:
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    required_places = int(request.form["places"])
    competition["number_of_places"] = (
        int(competition["number_of_places"]) - required_places
    )
    flash("Great! Booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display


@app.route("/logout")
def logout() -> Response:
    return redirect(url_for("index"))
