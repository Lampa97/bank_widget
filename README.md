# Bank Widget

## Описание

Статус: *В разработке*

Этот виджет позволяет выполнять несколько задач для работы
с банковским счетом, картами, а также финансовыми операциями.

### *На данный момент реализован следующий функционал:*

1. Модуль **masks.py** со следующими функциями:
    + **get_mask_card_number** - *маскирует номер карты по шаблону*
    + **get_mask_account** - *маскирует номер счета по шаблону*
2. Модуль **widget.py** со следующими функциями:
    + **mask_account_card** - *используя функции из **masks.py** возвращает замаскированный номер счета либо карты*
    + **get_date** - *форматирует строку с датой, возвращая дату формата ДД.ММ.ГГГГ*
3. Модуль **processing.py** со следующими функциями:
    + **filter_by_state** - *фильтрует банкцовские операции по их состоянию*
    + **sort_by_date** - *сортирует банковские операции по дате*


### Структура проекта:

Проект использует виртуальное окружение ***Poetry***. Информация о зависимостях проекта
находится в файле ***pyproject.toml***. 

Для  более простой установки зависимостей рекомендуется использовать виртуальное окружение
Poetry. 

Чтобы установить зависимости используйте  следующую команду:

```
poetry install
```

#### В будущем здесь появится более полная информация о проекте...