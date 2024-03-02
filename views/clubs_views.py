from flask import render_template

from data.store import ClubStore


def club_view():
    ClubStore.load()
    return render_template("clubs.html", clubs=ClubStore.get_all())
