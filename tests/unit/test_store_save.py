import os
from unittest.mock import mock_open, patch

import pytest

from config import DB_PATH
from data.store import Store


def test_save_writes_to_file_correctly():
    model_name = "TestModel"
    objects = [{"id": 1, "name": "Test Item"}]
    store = Store(model_name)
    store.objects = objects

    mocked_file = mock_open()
    with patch("builtins.open", mocked_file) as mocked_open:
        with patch("json.dump") as mocked_json_dump:
            store.save()
            path = os.path.join(DB_PATH, f"{model_name.lower()}s.json")
            mocked_open.assert_called_once_with(path, "w")

            mocked_json_dump.assert_called_once_with(
                {f"{model_name.lower()}s": objects}, mocked_file(), indent=4
            )


def test_save_raises_exception_on_file_open_failure():
    store = Store("TestModel")
    store.objects = [{"id": 1, "name": "Test Item"}]

    with patch("builtins.open", side_effect=PermissionError):
        with pytest.raises(PermissionError):
            store.save()


def test_save_raises_exception_on_serialization_failure():
    store = Store("TestModel")
    store.objects = [set([1, 2, 3])]

    with patch("builtins.open", mock_open()):
        with pytest.raises(TypeError):
            store.save()
