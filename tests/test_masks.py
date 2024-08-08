import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("3456897025467435", "3456 89** **** 7435"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("5498335792140867", "5498 33** **** 0867"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [("14359786474614355478", "**5478"), ("12345678123456781234", "**1234"), ("58672436435819576437", "**6437")],
)
def test_get_mask_account_number(number, expected):
    assert get_mask_account(number) == expected
