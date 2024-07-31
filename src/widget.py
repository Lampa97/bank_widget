from typing import Optional

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> Optional[str]:
    """Функция принимает имя и номер карты/счета в виде строки и возвращает замаскированный номер"""
    splitted_info = card.split()  # разделяем имя и номер
    number = ""
    for item in splitted_info:
        if item.isdigit():
            number = item  # отделенный номер карты/счета
            splitted_info.remove(item)
    info = " ".join(splitted_info)  # имя карты/счета

    if len(number) == 16:
        return f"{info} {get_mask_card_number(number)}"
    elif len(number) == 20:
        return f"{info} {get_mask_account(number)}"
    return None


print(mask_account_card("Счет 35383033474447895560"))
