from flask import render_template
from data.store import ClubStore
from utils import protected_view


@protected_view
def club_view():
    ClubStore.load()
    clubs = ClubStore.get_all()

    return render_template("clubs.html", clubs=clubs)
