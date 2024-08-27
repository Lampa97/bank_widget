from src.utils import get_transaction_data


def test_get_transaction_data_error():
    assert get_transaction_data("") == []


def test_get_transaction_data(json_data):
    assert get_transaction_data("../tests/test_operations.json") == json_data


def test_get_transaction_data_empty():
    assert get_transaction_data("../tests/test_empty_operations.json") == []
