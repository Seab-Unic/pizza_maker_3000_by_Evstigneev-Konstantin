import re
from datetime import datetime
import asyncio

def update_ingredients(file_path, ingredients_used):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    updated_lines = []
    for line in lines:
        if '-' in line:
            name, *rest = line.split('-', 1)
            name = name.strip()
            if name in ingredients_used:
                try:
                    value = int(rest[0].strip()) - 1
                    updated_lines.append(f"{name} - {value}\n")
                    continue
                except (ValueError, IndexError):
                    pass
        updated_lines.append(line)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

async def fun1(x):
    print("Ждём ответа от сервера")
    await asyncio.sleep(10)

def check_fio(fio):
    pattern = r"^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$"
    return bool(re.fullmatch(pattern, fio.strip()))

def check_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(pattern, email.strip()))

def check_phone(phone):
    pattern = r"^\+\d{11,}$"
    return bool(re.fullmatch(pattern, phone.strip()))

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

def save_user_data(name, email, phone, birth_date, password):
    with open(r"C:\Users\Seab\PycharmProjects\PythonProject1\list_users.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} - {email} - {phone} - {birth_date} - {password}\n")

def check_user_exists(email, password=None):
    try:
        with open(r"C:\Users\Seab\PycharmProjects\PythonProject1\list_users.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) >= 2 and email == parts[1]:
                    if password is not None and len(parts) >= 5 and password == parts[4]:
                        return True
                    elif password is None:
                        return True
    except FileNotFoundError:
        pass
    return False

def login():
    email = input("Введите email для входа: ")
    if not check_email(email):
        print("Ошибка, некорректный формат email")
        return None
    if not check_user_exists(email):
        print("Пользователь с таким email не найден")
        return None
    password = input("Введите пароль: ")
    if not check_user_exists(email, password):
        print("Неверный пароль")
        return None
    print("Вход выполнен успешно")
    return email

def info():
    print("1. Вход")
    print("2. Регистрация")
    choice = input("Выберите действие (1 или 2): ")
    if choice == "1":
        email = login()
        if email is None:
            return None
        try:
            with open(r"C:\Users\Seab\PycharmProjects\PythonProject1\list_users.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if email in line:
                        birth_date = line.split("-")[3].strip()
                        age = datetime.now().year - datetime.strptime(birth_date, "%d.%m.%Y").year
                        return age
        except FileNotFoundError:
            print("Ошибка при чтении данных пользователя")
            return None
    elif choice == "2":
        name = input("Введите ФИО: ")
        if not check_fio(name):
            print("Ошибка, некорректный формат ФИО")
            return None
        email = input("Введите email: ")
        if not check_email(email):
            print("Ошибка, некорректный формат email")
            return None
        phone = input("Введите номер телефона: ")
        if not check_phone(phone):
            print("Ошибка, некорректный формат телефона")
            return None
        birth_date = input("Введите вашу дату рождения (дд.мм.гггг): ")
        try:
            age = datetime.now().year - datetime.strptime(birth_date, "%d.%m.%Y").year
        except ValueError:
            print("Ошибка в формате даты")
            return None
        password = input("Введите пароль: ")
        save_user_data(name, email, phone, birth_date, password)
        return age
    else:
        print("Некорректный выбор")
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
    ingridients_check = [
        "Пепперони", "Салями", "Ветчина", "Бекон", "Куриное филе",
        "Моцарелла", "Чеддер", "Горгонзола", "Пармезан", "Фета",
        "Томатный соус", "Сырный соус", "Барбекю", "Песто", "Сметанный соус",
        "Шампиньоны", "Лук", "Сладкий перец", "Оливки", "Помидоры"
    ]
    total = 0
    order_items = []
    ingredients_used = []
    while True:
        choice = input("Выберите номер (или стоп для остановки): ")
        if choice.lower() == "стоп":
            break
        if choice in menu:
            item, price = menu[choice]
            if item == "Хочу создать пиццу":
                print("Вы выбрали создание кастомной пиццы.")
                print("Список ингредиентов:")
                for i, value in enumerate(ingridients_check, 1):
                    print(f"{i}: {value}")
                ingredients_input = input("Введите номера ингредиентов")
                ingredients_list = ingredients_input.split(',')
                try:
                    ingredients = [ingridients_check[int(num.strip()) - 1] for num in ingredients_list]
                    ingredients_used.extend(ingredients)
                except (ValueError, IndexError):
                    print("Нужно ввести цифру")
                    return
                cp_name = f"Кастомная пицца: {', '.join(ingredients)}"
                cp_price = 450
                print(f"Выбрали: {cp_name} за {cp_price}руб")
                yn = input("Добавить? (да/нет): ")
                if yn.lower() == "да":
                    order_items.append((cp_name, cp_price))
                    total += cp_price
                    print("Добавлено")
                else:
                    print("Отменено")
            else:
                print(f"Выбрали: {item} за {price}руб")
                yn = input("Добавить? (да/нет): ")
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
        confirm = input("Подтвердить? (да/нет): ")
        if confirm.lower() == "да":
            print("Заказ принят")
            check_output(order_items)
            if ingredients_used:
                update_ingredients("C:\\Users\\Seab\\PycharmProjects\\PythonProject1\\baze.txt", ingredients_used)
            return True
        else:
            print("Заказ отменён")
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
    await fun1("something because it's needed")
    order(menu)

asyncio.run(main())






