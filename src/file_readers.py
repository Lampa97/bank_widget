import csv
from typing import List

import pandas as pd


def read_csv_file(path: str) -> List[dict]:
    """Функция позволяет читать информацию из csv-файла"""
    info = pd.read_csv(path, delimiter=";")
    result = info.to_dict(orient="records")
    return result


def read_excel_file(path: str) -> List[dict]:
    """Функция позволяет читать информацию из excel-файла"""
    info = pd.read_excel(path)
    result = info.to_dict(orient="records")
    return result
