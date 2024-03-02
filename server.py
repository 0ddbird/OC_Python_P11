import os

from dotenv import load_dotenv

from flask import Flask, Response, render_template

from utils import inject_user_status
from views.booking_views import booking_view
from views.clubs_views import club_view
from views.home_views import home_view
from views.logout_views import logout_view
from views.purchase_slots import purchase_slots_view

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.context_processor(inject_user_status)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET", "POST"])
def home_route() -> Response:
    return home_view()


@app.route("/book/<competition_name>/<club_name>")
def book_route(competition_name: str, club_name: str) -> Response:
    return booking_view(competition_name, club_name)


@app.route("/purchase-slots", methods=["POST"])
def purchase_slots_route() -> Response:
    return purchase_slots_view()


@app.route("/clubs", methods=["GET"])
def clubs_route() -> Response:
    return club_view()


@app.route("/logout")
def logout() -> Response:
    return logout_view()
