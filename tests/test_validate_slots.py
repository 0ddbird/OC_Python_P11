import pytest

from services.booking_services import validate_slots_is_pos_int


def test_validate_required_slots_value_when_valid_int():
    assert validate_slots_is_pos_int(4) == 4


def test_validate_required_slots_value_when_null_value():
    with pytest.raises(ValueError) as e:
        validate_slots_is_pos_int(0)
    assert str(e.value) == "The number of slots to book must be a positive integer"


def test_validate_required_slots_value_when_float_value():
    with pytest.raises(ValueError) as e:
        validate_slots_is_pos_int(1.2)
    assert str(e.value) == "The number of slots to book must be a positive integer"


def test_validate_required_slots_value_when_str_value():
    with pytest.raises(ValueError) as e:
        validate_slots_is_pos_int("4")
    assert str(e.value) == "The number of slots to book must be a positive integer"


def test_validate_required_slots_value_when_none_value():
    with pytest.raises(ValueError) as e:
        validate_slots_is_pos_int(None)
    assert str(e.value) == "The number of slots to book must be a positive integer"


def test_validate_required_slots_value_when_negative_int():
    with pytest.raises(ValueError) as e:
        validate_slots_is_pos_int(-1)
    assert str(e.value) == "The number of slots to book must be a positive integer"
