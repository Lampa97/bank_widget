import os
from typing import List

import pandas as pd


def read_csv_file(path: str) -> List[dict]:
    """Функция позволяет читаь информацию из csv-файла"""
    my_path = os.path.join(os.path.dirname(__file__), path)
    info = pd.read_csv(my_path, delimiter=";")
    return info.to_dict(orient="records")


def read_excel_file(path: str) -> List[dict]:
    """Функция позволяет читать информацию из excel-файла"""
    my_path = os.path.join(os.path.dirname(__file__), path)
    info = pd.read_excel(my_path)
    return info.to_dict(orient="records")


print(read_excel_file("../data/transactions_excel.xlsx"))
