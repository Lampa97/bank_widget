from unittest.mock import Mock, patch

from src.external_api import convert_into_rub


def test_convert_into_rub_usd_or_eur(one_usd_transaction, result):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = result

    with patch("requests.get", return_value=mock_response):
        result = convert_into_rub(one_usd_transaction)
        assert result == 200.00


def test_convert_into_rub_rub(one_rub_transaction):
    assert convert_into_rub(one_rub_transaction) == float(one_rub_transaction["operationAmount"]["amount"])


def test_convert_into_rub_empty():
    assert convert_into_rub({}) == False


def test_convert_into_rub_invalid_currency(one_gbp_transaction):
    assert convert_into_rub(one_gbp_transaction) == False
