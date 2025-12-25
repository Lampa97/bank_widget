from typing import List

from src.file_readers import read_csv_file, read_excel_file
from src.generators import filter_by_currency, filter_by_currency_for_csv_excel
from src.processing import filter_by_state, get_transactions_by_description, sort_by_date
from src.utils import get_transaction_data
from src.widget import get_date, mask_account_card


def file_choice() -> List[dict]:
    """Функция предоставляет пользователю выбор файла из которого будет считываться информация о транзакциях"""
    while True:
        user_choice = input(
            """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
        if user_choice == "1":
            print("Для обработки выбран JSON-файл.\n")
            transaction_info = get_transaction_data("../data/operations.json")
        elif user_choice == "2":
            print("Для обработки выбран CSV-файл.\n")
            transaction_info = read_csv_file("../data/transactions.csv")
        elif user_choice == "3":
            print("Для обработки выбран XLSX-файл.\n")
            transaction_info = read_excel_file("../data/transactions_excel.xlsx")
        else:
            print("Такого варианта нет, пожалуйста, попробуйте снова\n")
            continue
        return transaction_info


def choose_status(transactions: List[dict]) -> List[dict]:
    """Функция предоставляет пользователю выбор статуса по которому будут фильтроваться транзакции"""
    user_choice = input(
        """
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )
    choice_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        if user_choice.upper() in choice_list:
            status = user_choice.upper()
            print(f'Операции отфильтрованы по статусу "{status}"\n')
            return filter_by_state(transactions, status)
        else:
            print(f'Статус операции "{user_choice}" недоступен.\n')
            continue


def choose_operations(transactions: List[dict]) -> List[dict]:
    """Функция предоставляет пользователю инструменты сортировки и фильтрации транзакций"""
    choose_date_sort = input("Отсортировать операции по дате? Да/Нет\n")
    if choose_date_sort.lower() == "да":
        sort_order_choice = input("Отсортировать по возрастанию или по убыванию?\n")
        if sort_order_choice.lower() == "по возрастанию":
            sorted_transactions = sort_by_date(transactions)
        elif sort_order_choice.lower() == "по убыванию":
            sorted_transactions = sort_by_date(transactions, ascending=False)
        else:
            print("Не получилось обработать ввод. Транзакции будут отсортированы по возрастанию")
            sorted_transactions = sort_by_date(transactions)
    else:
        sorted_transactions = transactions
    choose_currency = input("Выводить только рублевые транзакции? Да/Нет\n")
    if choose_currency.lower() == "да":
        try:
            currency_filtered_transactions = list(filter_by_currency(sorted_transactions, "RUB"))
        except KeyError:
            currency_filtered_transactions = list(filter_by_currency_for_csv_excel(sorted_transactions, "RUB"))
    else:
        currency_filtered_transactions = list(sorted_transactions)
    description_filter_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if description_filter_choice.lower() == "да":
        search_word = input("По какому слову вы хотите отфильтровать транзакции?\n")
        filtered_transactions = get_transactions_by_description(currency_filtered_transactions, search_word)
    else:
        filtered_transactions = currency_filtered_transactions
    return list(filtered_transactions)


def print_transactions(transactions: List[dict]) -> None:
    """Функция выводит в консоль итоговый список транзакций"""
    print("Распечатываю итоговый список транзакций...\n")
    if len(transactions) > 0:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")
        for transaction in transactions:
            date = get_date(transaction["date"])
            description = transaction["description"]
            try:
                account_card_number_from = mask_account_card(transaction["from"])
            except KeyError:
                account_card_number_from = None
            account_card_number_to = mask_account_card(transaction["to"])
            try:
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]
            except KeyError:
                amount = transaction["amount"]
                currency = transaction["currency_name"]
            print(date, description)
            if account_card_number_from is None:
                print(account_card_number_to)
            else:
                print(f"{account_card_number_from} -> {account_card_number_to}")

            print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями\n")
    transactions_info = file_choice()
    filtered_info = choose_status(transactions_info)
    chosen_operations = choose_operations(filtered_info)
    print_transactions(chosen_operations)


if __name__ == "__main__":
    main()
