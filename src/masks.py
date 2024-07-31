from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковской карты в формате 'XXXX XX** **** XXXX'"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковского счета в формате '**XXXX'"""
    return f"**{account_number[-4:]}"
