from functools import wraps

from flask import flash, redirect, request, session, url_for


def inject_user_status():
    is_logged_in = "email" in session
    return dict(is_logged_in=is_logged_in)


def protected_view(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        email = session.get("email") or request.form.get("email")
        if not email:
            flash("You must be logged in to access this page.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function
