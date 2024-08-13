from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest

def test_filter_by_currency_usd(transactions, usd_transactions):
    expected = usd_transactions
    result = list(filter_by_currency(transactions, 'USD'))
    assert result == expected


def test_filter_by_currency_rub(transactions, rub_transactions):
    expected = rub_transactions
    result = list(filter_by_currency(transactions, 'RUB'))
    assert result == expected





def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(StopIteration):
        assert next(generator)



def test_card_number_generator():
    generator = card_number_generator(12345005, 12345010)
    assert next(generator) == '0000 0000 1234 5005'
    assert next(generator) == '0000 0000 1234 5006'
    assert next(generator) == '0000 0000 1234 5007'
