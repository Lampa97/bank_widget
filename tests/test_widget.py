import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Master Card 3456897025467435", "Master Card 3456 89** **** 7435"),
        ("Visa 1111222233334444", "Visa 1111 22** **** 4444"),
        ("Счет 47658724596735475867", "Счет **5867"),
    ],
)
def test_mask_account_card_valid(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card, expected",
    [("Master Card 34568970254674", None), ("Visa 111122223df33344", None), ("Счет 4765872459673547586755665", None)],
)
def test_mask_account_card_invalid(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-10-21T01:12:20.676547", "21.10.2022"),
        ("1997-03-01T06:55:33.421467", "01.03.1997"),
    ],
)
def test_get_date_valid(date, expected):
    assert get_date(date) == expected


@pytest.mark.parametrize(
    "date, expected",
    [("2O24-03-11T02:26:18.671407", None), ("2022-10-2lT01:12:20.676547", None), ("1997-0З-01T06:55:33.421467", None)],
)
def test_get_date_invalid(date, expected):
    assert get_date(date) == expected
