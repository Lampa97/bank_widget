import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_KEY")
headers = {"apikey": API_TOKEN}


def transaction_into_rub(transaction: dict) -> float:
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency == "RUB":
        return float(amount)
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return float(round(result["result"], 2))
        else:
            print('Конвертация не удалась')
    return False
