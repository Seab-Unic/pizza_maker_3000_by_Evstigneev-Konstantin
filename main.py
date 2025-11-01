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
    name = input('Введите имя ')
    print(f"Привет, {name}")
    try:
        age = int(input("Введите ваш возраст "))
        return name, age
    except:
        print("Ошибка в возрасте")
        return None, None

@decorator_menu
def agecheck(age):
    if age < 18:
        print("Пиццы:")
        print("1. Пеперони - 400руб")
        print("2. Сырная - 350руб")
        print("3. Цезарь - 390руб")
        print("Напитки:")
        print("4. Сок(злой мультифрукт) - 100руб")
        print("5. Газировка - 120руб")
        return {'1': ('Пеперони', 400), '2': ('Сырная', 350), '3': ('Цезарь', 390), '4': ('Сок', 100),
                '5': ('Апельсин', 120)}
    else:
        print("Пиццы:")
        print("1. Пипперони - 400руб")
        print("2. Пипперони большая - 500руб")
        print("3. Сырная - 350руб")
        print("4. Сырная большая - 450руб")
        print("5. Цезарь - 390руб")
        print("6. Цезарь большой - 490руб")
        print("Напитки:")
        print("7. Сок(злой мультифрукт) - 100руб")
        print("8. Газировка - 120руб")
        return {'1': ('Пеперони', 400), '2': ('Пеперони большая', 500), '3': ('Сырная', 350),
                '4': ('Сырная большая', 450), '5': ('Цезарь', 390), '6': ('Цезарь большой', 490),
                '7': ('Сок (злой мультифрукт)', 100),
                '8': ('Апельсин', 120)}

def order(menu):
    total = 0
    order_items = []

    while True:
        choice = input("Выберите номер (или стоп для остановки): ")

        if choice == 'стоп':
            break

        if choice in menu:
            item, price = menu[choice]
            print(f"Выбрали: {item} за {price}руб")

            yn = input("Добавить? (да/нет): ")
            if yn == 'да':
                order_items.append((item, price))
                total += price
                print("Добавлено!")
        else:
            print("Нет такого")

    if order_items:
        print("\nВаш заказ:")
        for item, price in order_items:
            print(f"{item} - {price}руб")
        print(f"Всего: {total}руб")

        confirm = input("Подтвердить? (да/нет): ")
        if confirm == 'да':
            print("Заказ принят!")
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

def main():
    name, age = info()
    if name is None:
        return
    menu = agecheck(age)
    order(menu)
main()