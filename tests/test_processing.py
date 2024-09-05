import pytest

from src.processing import count_operation_categories, filter_by_state, get_transactions_by_description, sort_by_date


def test_filter_by_state_executed(processing_data_valid):
    assert filter_by_state(processing_data_valid) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(processing_data_valid):
    assert filter_by_state(processing_data_valid, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_missing(processing_data_invalid):
    assert filter_by_state(processing_data_invalid) == [{"id": 41428829, "state": "EXECUTED"}]


def test_filter_by_date_ascending(processing_data_valid):
    assert sort_by_date(processing_data_valid) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_date_descending(processing_data_valid):
    assert sort_by_date(processing_data_valid, ascending=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_filter_by_date_missing(processing_data_invalid):
    with pytest.raises(KeyError):
        assert sort_by_date(processing_data_invalid)


def test_get_transactions_by_description_not_found(transactions):
    assert get_transactions_by_description(transactions, "Учеба") == []


def test_get_transactions_by_description_success(transactions):
    assert get_transactions_by_description(transactions, "карт") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_count_operation_categories_not_found(transactions):
    assert count_operation_categories(transactions, ["Оплата учебы", "Выплата кредита"]) == {}


def test_count_operation_categories_found(transactions):
    assert count_operation_categories(transactions, ["Перевод организации", "Перевод со счета на счет"]) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
    }
