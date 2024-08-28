import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_KEY")
headers = {"apikey": API_TOKEN}


def convert_into_rub(transaction: dict) -> float | bool:
    """Функция конвертирует валюту в рубли по запросу к API"""
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
    except KeyError:
        return False
    if currency == "RUB":
        return float(amount)
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return float(round(result["result"], 2))
    return False
