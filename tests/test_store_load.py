import json
import os
from unittest.mock import mock_open, patch

import pytest

from config import DB_PATH
from data.store import Store


def test_store_load_data_correctly():
    model_name = "TestModel"
    mocked_data = {f"{model_name.lower()}s": [{"id": 1, "name": "Test Item"}]}

    with patch(
        "builtins.open", mock_open(read_data=json.dumps(mocked_data))
    ) as mocked_file:
        with patch("json.load", return_value=mocked_data) as mocked_json_load:
            store = Store(model_name)
            store.load()
            path = os.path.join(DB_PATH, f"{model_name.lower()}s.json")
            mocked_file.assert_called_with(path, "r")
            mocked_json_load.assert_called()

            assert (
                store.objects == mocked_data[f"{model_name.lower()}s"]
            ), "The load() method must correctly set data in store.objects"


def test_store_load_raises_file_not_found_error():
    model_name = "NonExistentModel"
    with patch("builtins.open", side_effect=FileNotFoundError) as mocked_file:
        with pytest.raises(FileNotFoundError):
            store = Store(model_name)
            store.load()
        path = os.path.join(DB_PATH, f"{model_name.lower()}s.json")
        mocked_file.assert_called_with(path, "r")
