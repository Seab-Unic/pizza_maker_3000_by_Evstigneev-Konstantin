import re
from datetime import datetime
import asyncio
import time

async def fun1(x):
    print("ждем ответа от сервера")
    await asyncio.sleep(10)

def check_fio(fio):
    pattern = r"^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$"
    return bool(re.fullmatch(pattern, fio.strip()))

def check_email(email):
    pattern = r"@"
    return bool(re.search(pattern, email.strip()))

def check_phone(phone):
    pattern = r"+7"
    return bool(re.search(pattern, phone.strip()))

def decorator_menu(func):
    def wrapper(age):
        print("********** МЕНЮ **********")
        result = func(age)
        print("**************************")
        return result
    return wrapper

def decorator_check(func):
    def wrapper(order_items):
        print("********** ЧЕК **********")
        result = func(order_items)
        print("**************************")
        return result
    return wrapper

def info():
    name = input("Введите ФИО ")
    if not check_fio(name):
        print("Ошибка, некорректный формат фио")
        return None
    email = input("Введите email ")
    if not check_email(email):
        print("Ошибка")
        return None
    phone = input("введите номер телефона ")
    print(f"Привет, {name}")
    try:
        age = input("Введите вашу дату рождения (дд.мм.гггг) ")
        age2 = datetime.strptime(age, "%d.%m.%Y")
        return age2.year
    except ValueError:
        print("Ошибка в формате даты")
        return None

@decorator_menu
def agecheck(age):
    if age > 2007:
        print("Пиццы:")
        print("1. Пеперони - 400руб")
        print("2. Сырная - 350руб")
        print("3. Цезарь - 390руб")
        print("Напитки:")
        print("4. Сок(злой мультифрукт) - 100руб")
        print("5. Газировка - 120руб")
        print("6. Хочу создать пиццу")
        return {
            "1": ("Пеперони", 400),
            "2": ("Сырная", 350),
            "3": ("Цезарь", 390),
            "4": ("Сок", 100),
            "5": ("Газировка", 120),
            "6": ("Хочу создать пиццу", 0)
        }
    else:
        print("Пиццы:")
        print("1. Пеперони - 400руб")
        print("2. Пеперони большая - 500руб")
        print("3. Сырная - 350руб")
        print("4. Сырная большая - 450руб")
        print("5. Цезарь - 390руб")
        print("6. Цезарь большой - 490руб")
        print("Напитки:")
        print("7. Сок(злой мультифрукт) - 100руб")
        print("8. Газировка - 120руб")
        print("9. Хочу создать пиццу")
        return {
            "1": ("Пеперони", 400),
            "2": ("Пеперони большая", 500),
            "3": ("Сырная", 350),
            "4": ("Сырная большая", 450),
            "5": ("Цезарь", 390),
            "6": ("Цезарь большой", 490),
            "7": ("Сок (злой мультифрукт)", 100),
            "8": ("Газировка", 120),
            "9": ("Хочу создать пиццу", 0)
        }

def order(menu):
    ingridients_check = {
        "1": "Пепперони", "2": "Салями", "3": "Ветчина", "4": "Бекон", "5": "Куриное филе",
        "6": "Моцарелла", "7": "Чеддер", "8": "Горгонзола", "9": "Пармезан", "10": "Фета",
        "11": "Томатный соус", "12": "Сырный соус", "13": "Барбекю", "14": "Песто", "15": "Сметанный соус",
        "16": "Шампиньоны", "17": "Лук", "18": "Сладкий перец", "19": "Оливки", "20": "Помидоры"
    }
    total = 0
    order_items = []
    while True:
        choice = input("Выберите номер (или стоп для остановки) ")
        if choice.lower() == "стоп":
            break
        if choice in menu:
            item, price = menu[choice]
            if item == "Хочу создать пиццу":
                print("Вы выбрали создание кастомной пиццы.")
                print("Список ингредиентов:")
                for key, value in ingridients_check.items():
                    print(f"{key}: {value}")
                ingredients_input = input("Введите номера ингредиентов через запятую: ")
                ingredients_list = ingredients_input.split(',')
                try:
                    ingredients = [ingridients_check[num.strip()] for num in ingredients_list]
                except KeyError:
                    print("надо ввести цифру")
                    return
                cp_name = f"Кастомная пицца: {', '.join(ingredients)}"
                cp_price = 450
                print(f"Выбрали: {cp_name} за {cp_price}руб")
                yn = input("Добавить? (да/нет) ")
                if yn.lower() == "да":
                    order_items.append((cp_name, cp_price))
                    total += cp_price
                    print("Добавлено")
                else:
                    print("Отменено")
            else:
                print(f"Выбрали: {item} за {price}руб")
                yn = input("Добавить? (да/нет) ")
                if yn.lower() == "да":
                    order_items.append((item, price))
                    total += price
                    print("Добавлено")
        else:
            print("Нет такого")
    if order_items:
        print("\nВаш заказ:")
        for item, price in order_items:
            print(f"{item} - {price}руб")
        print(f"Всего: {total}руб")
        confirm = input("Подтвердить? (да/нет) ")
        if confirm.lower() == "да":
            print("Заказ принят")
            check_output(order_items)
            return True
        else:
            print("Заказ отменен")
            return False
    else:
        print("Ничего не заказано")
        return False

@decorator_check
def check_output(order_items):
    print("Ваш заказ:")
    for item, price in order_items:
        print(f"{item} - {price}руб")
    total = sum(price for item, price in order_items)
    print(f"Всего: {total}руб")
    return True

async def main():
    age = info()
    if age is None:
        return
    menu = agecheck(age)
    await fun1("something because it`s need to be")
    order(menu)

asyncio.run(main())


