import json
import os
from typing import List


def get_transaction_data(path: str) -> List[dict]:
    """Функция читает и возвращает данные о транзакциях из json файла"""
    my_path = os.path.join(os.path.dirname(__file__), path)
    try:
        with open(my_path, encoding="utf-8") as json_data:
            content = json.load(json_data)
        if type(content) is list and len(content) > 1:
            return content
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return []
