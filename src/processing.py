from typing import Iterable


def filter_by_state(operation_data: Iterable[dict], state="EXECUTED") -> Iterable[dict]:
    """Функция принимает список словарей с данными о транзакции и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    return [item for item in operation_data if item.get("state") == state]

def sort_by_date(operation_data: Iterable[dict], ascending=True) -> Iterable[dict]:
    """Функция принмает список словарей с данными о транзакции и возвращает новый список, отсортированный по дате.
    По умолчанию - убывание."""
    return sorted(operation_data, key=lambda x: x.get("date"), reverse=ascending)
