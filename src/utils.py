import json
import logging
import os
from typing import List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transaction_data(path: str) -> List[dict]:
    """Функция читает и возвращает данные о транзакциях из json файла"""
    my_path = os.path.join(os.path.dirname(__file__), path)
    logger.info(f"Получили абсолютный путь к файлу - {my_path}")
    try:
        with open(my_path, encoding="utf-8") as json_data:
            content = json.load(json_data)
        if type(content) is list and len(content) > 1:
            logger.info("Успешно загрузили и преобразовали json файл")
            return content
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    logger.warning("Файл пуст")
    return []
