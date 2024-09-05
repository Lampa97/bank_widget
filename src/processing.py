import re
from collections import Counter
from typing import List


def filter_by_state(transactions: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция принимает список словарей с данными о транзакции и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[dict], ascending: bool = True) -> List[dict]:
    """Функция принимает список словарей с данными о транзакции и возвращает новый список, отсортированный по дате.
    По умолчанию - убывание."""
    return sorted(transactions, key=lambda x: x["date"], reverse=ascending)


def get_transactions_by_description(transactions: List[dict], search_string: str) -> List[dict]:
    """Функция принимает список транзакций и возвращает транзакции
    соответствующие строке поиска по описанию транзакции"""
    pattern = rf"{search_string}"
    return [trans for trans in transactions if re.search(pattern, trans["description"], flags=re.IGNORECASE)]


def count_operation_categories(transactions: List[dict], categories_list: list) -> dict:
    return dict(Counter([x["description"] for x in transactions if x["description"] in categories_list]))
