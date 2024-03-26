import pytest

from data.store import ObjectDoesNotExist, Store


def test_get_found():
    store = Store("TestObject")
    store.objects = [
        {"name": "Object1", "value": 10},
        {"name": "Object2", "value": 20},
        {"name": "Object3", "value": 30},
    ]
    attribute = "name"
    value = "Object2"
    expected = {"name": "Object2", "value": 20}

    result = store.get(attribute, value)
    assert (
        result == expected
    ), "The expected result must be returned when the attribute and the value match an existing object"


def test_get_not_found():
    store = Store("TestObject")
    store.objects = [
        {"name": "Object1", "value": 10},
        {"name": "Object2", "value": 20},
        {"name": "Object3", "value": 30},
    ]
    attribute = "name"
    value = "Object4"

    with pytest.raises(ObjectDoesNotExist) as e_info:
        store.get(attribute, value)
    assert (
        str(e_info.value) == "TestObject not found for name: Object4"
    ), "An ObjectDoesNotExist exception must be raised if the object is not found"
