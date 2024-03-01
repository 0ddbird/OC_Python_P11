class FormContentError(Exception):
    pass


def get_name_from_form(form, form_key: str) -> str:
    if (name := form.get(form_key, None)) is None:
        raise FormContentError(f"{form_key} missing in form")
    return name
