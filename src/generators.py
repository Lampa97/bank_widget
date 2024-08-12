from typing import List, Iterator, Generator

def filter_by_currency(transactions: List[dict], currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает транзакции отфильтрованные по заданной валюте."""
    return filter(lambda x: x['operationAmount']['currency']['code'] == currency, transactions)

def transaction_descriptions(transactions: List[dict]) -> Generator:
    """Функция принимает на вход список словарей с транзакциями.
    Возвращает описание каждой операции."""
    return (x['description'] for x in transactions)
        

def card_number_generator(start: int, stop: int) -> Generator:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    base_number = 10000000000000000
    for n in range(start, stop+1):
        new_number = base_number + n
        card_number = str(new_number)
        yield f'{card_number[1:5]} {card_number[5:9]} {card_number[9:13]} {card_number[13:]}'


