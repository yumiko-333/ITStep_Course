# Завдання 4

# Створіть нову гілку practice/pizza
# Перейдіть на неї та реалізуйте програму замовлення
# піци в декілька комітів

# Коміт1
# Вивід Меню
#       1. Вибрати піцу
#       2. Вихід
#
# Далі реалізуйте нескінченний цикл
# Якщо користувач обирає 1, то запитати назву піци та
# кількість і вивести повідомлення
# Замовлено [назва піци], [кількість] шт
#
# Коміт2
# Додайте меню з цінами піц
#       Маргарита – 150 грн
#       Пепероні – 180 грн
#       Чотири сири – 200 грн

# Якщо користувач ввів неправильно назву піци то
# повідомити про це
#
# Коміт3
# Додайте третю опцію – показати все замовлення
# Треба вивести які піци були замовлені, їхня вартість та
# загальна вартість

MAX_PIZZA_AMOUNT = 15

MARGHERITA_COST = 150
PEPERONI_COST = 180
FOUR_CHEESE_COST = 200

margherita_amount = 0
peperoni_amount = 0
four_cheese_amount = 0

total = 0

total_amount = 0

while True:
    print()
    print("Виберіть опцію з меню")

    option = int(
        input("\n1. Вибрати піцу \n2. Вихід \n3. Показати все замовлення \nВаш вибір: ")
    )

    if option == 1:
        print(
            "\nПіци: \nМаргарита - 150 грн \nПепероні - 180 грн \nЧотири сири - 200 грн"
        )

        pizza = input("\nЯку піцу бажаєте? ")

        if pizza != "Маргарита" and pizza != "Пепероні" and pizza != "Чотири сири":
            print("Такої піци у нас немає, спробуйте ще раз.")
            continue

        amount = int(input("Скільки штук? "))

        if amount <= 0:
            print("Кількість не може бути 0, або від'ємна! ")
            continue

        if total_amount + amount > MAX_PIZZA_AMOUNT:
            print("Ви не можете замовити більше 15 піц!")
            continue

        if pizza == "Маргарита":
            margherita_amount += amount
            total_amount += amount
            total += MARGHERITA_COST * amount

        elif pizza == "Пепероні":
            peperoni_amount += amount
            total_amount += amount
            total += PEPERONI_COST * amount

        elif pizza == "Чотири сири":
            four_cheese_amount += amount
            total_amount += amount
            total += FOUR_CHEESE_COST * amount

        print(f"Замовлено піцу {pizza} {amount} шт")

    elif option == 2:
        print("Гарного вам дня!")
        break

    elif option == 3:
        print()
        print("==========ВАШЕ ЗАМОВЛЕННЯ==============")
        print("\nПіца  \tКількість \tВартість")

        print("--------------------------------------")

        if margherita_amount > 0:
            print(
                f"Маргарита \t{margherita_amount} \t{margherita_amount * MARGHERITA_COST} грн"
            )

        if peperoni_amount > 0:
            print(
                f"Пепероні \t{peperoni_amount} \t{peperoni_amount * PEPERONI_COST} грн"
            )

        if four_cheese_amount > 0:
            print(
                f"Чотири сири \t{four_cheese_amount} \t{four_cheese_amount * FOUR_CHEESE_COST} грн"
            )

        print("\n---------------------------------------")
        print(f"Загальна вартість: {total} грн")
        print("=========================================")
        print("Дякуємо за замовлення!")

        print("\nГарного дня!")
        break

    else:
        print("Такої опції немає! Спробуйте ще раз. ")
        continue
