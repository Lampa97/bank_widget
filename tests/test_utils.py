import json
from unittest.mock import Mock

from src.utils import get_transaction_data


def test_get_transaction_data_error():
    assert get_transaction_data("") == []


def test_get_transaction_data(path_to_file, test_json_data):
    mock_json = Mock(return_value=test_json_data)
    json.load = mock_json
    assert get_transaction_data(path_to_file) == test_json_data
    mock_json.assert_called()


def test_get_transaction_data_empty(path_to_file):
    mock_json = Mock(return_value=[{}])
    json.load = mock_json
    assert get_transaction_data(path_to_file) == []
    mock_json.assert_called()
