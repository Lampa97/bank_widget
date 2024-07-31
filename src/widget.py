from typing import Optional

from masks import get_mask_card_number, get_mask_account

def mask_account_card(card: str) -> Optional[str]:
    splitted_info = card.split()
    number = ''
    for item in splitted_info:
        if item.isdigit():
            number = item
            splitted_info.remove(item)
    info = ' '.join(splitted_info)

    if len(number) == 16:
        return f"{info} {get_mask_card_number(number)}"
    elif len(number) == 20:
        return f"{info} {get_mask_account(number)}"
    return None
