from typing import Iterable


def filter_by_state(operation_data: Iterable[dict], state="EXECUTED") -> Iterable[dict]:
    """Функция принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению."""
    return [item for item in operation_data if item["state"] == state]
