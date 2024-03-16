from flask import Response, flash, redirect, request, session, url_for

from data.store import ClubStore, CompetitionStore, ObjectDoesNotExist
from services.booking_services import purchase_slots


class FormContentError(Exception):
    pass


def get_name_from_form(form, form_key: str) -> str:
    if (name := form.get(form_key, None)) is None:
        raise FormContentError(f"{form_key} missing in form")
    return name


def purchase_slots_view() -> Response:
    ClubStore.load()
    CompetitionStore.load()

    try:
        competition_name = get_name_from_form(request.form, "competition")
        competition = CompetitionStore.get("name", competition_name)

        club_name = get_name_from_form(request.form, "club")
        club = ClubStore.get("name", club_name)

        session["email"] = club["email"]
        slots = request.form["slots"]
        purchase_slots(competition, club, slots)
    except (
        FormContentError,
        ObjectDoesNotExist,
        ValueError,
    ) as e:
        flash(str(e))
        return redirect(f"/book/{competition_name}/{club_name}")

    flash("Great! Booking complete!")
    return redirect(url_for("home_route"))
