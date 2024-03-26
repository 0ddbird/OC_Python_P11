import pytest

from views.purchase_slots import FormContentError, get_name_from_form


def test_valid_name_value():
    form = {"club": "Club name"}
    assert get_name_from_form(form, "club") == "Club name"


def test_missing_dict_main_key():
    form = {}
    form_key = "club"
    with pytest.raises(FormContentError) as e:
        get_name_from_form(form, form_key)
    assert str(e.value) == f"{form_key} missing in form"
