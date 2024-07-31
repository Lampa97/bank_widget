from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковской карты в формате 'XXXX XX** **** XXXX'"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return None


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковского счета в формате '**XXXX'"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    return None
