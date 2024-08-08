from typing import Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> Optional[str]:
    """Функция принимает имя и номер карты/счета в виде строки и возвращает замаскированный номер"""
    splitted_info = account_card.split()  # разделяем имя и номер
    number = ""
    for item in splitted_info:
        if item.isdigit():
            number = item  # отделенный номер карты/счета
            splitted_info.remove(item)
    info = " ".join(splitted_info)  # имя карты/счета

    if len(number) == 16:
        masked_number = get_mask_card_number(number)
        return f"{info} {masked_number}"
    elif len(number) == 20:
        masked_number = get_mask_account(number)
        return f"{info} {masked_number}"
    return None


def get_date(date: str) -> Optional[str]:
    """Функция принимает строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает отформатированную строку с датой в формате 'ДД.ММ.ГГГГ'"""
    year_month_day = date[:10]
    date_list = year_month_day.split("-")
    if "".join(date_list).isdigit():
        return ".".join(date_list[::-1])
    return None
