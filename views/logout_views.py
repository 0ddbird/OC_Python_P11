from flask import redirect, session, url_for


def logout_view():
    if session.get("email"):
        session.pop("email", None)
    return redirect(url_for("index"))
