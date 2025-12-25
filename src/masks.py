import logging
from typing import Optional

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковской карты в формате 'XXXX XX** **** XXXX'"""
    card_number = str(card_number)
    logger.info(f"Маскируем номер карты {card_number}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция возвращает замаскированный номер банковского счета в формате '**XXXX'"""
    account_number = str(account_number)
    logger.info(f"Маскируем номер счета {account_number}")
    return f"**{account_number[-4:]}"
