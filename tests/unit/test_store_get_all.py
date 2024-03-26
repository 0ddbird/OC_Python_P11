from data.store import Store


def test_get_found():
    store = Store("TestObject")

    objects = [
        {"name": "Object1", "value": 10},
        {"name": "Object2", "value": 20},
        {"name": "Object3", "value": 30},
    ]
    store.objects = objects

    result = store.get_all()
    assert result == objects, "The store must return all its objets"
