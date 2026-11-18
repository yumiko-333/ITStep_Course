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

margherita_cost = 150
peperoni_cost = 180
four_cheese_cost = 200

margherita_amount = 0
peperoni_amount = 0
four_cheese_amount = 0

total = 0

while True:
    print()
    print("Виберіть опцію з меню")

    option = int(
        input(
            "\n1. Вибрати піццу \n2. Вихід \n3. Показати все замовлення \nВаш вибір: "
        )
    )

    if option == 1:
        print(
            "\nПіцци: \nМаргарита - 150 грн \nПепероні - 180 грн \nЧотири сири - 200 грн"
        )

        pizza = input("\nЯку піццу бажаєте? ")

        if pizza == "Маргарита":
            amount = int(input("Скільки штук? "))

            margherita_amount += amount
            total += margherita_cost * amount

        elif pizza == "Пепероні":
            amount = int(input("Скільки штук? "))

            peperoni_amount += amount
            total += peperoni_cost * amount

        elif pizza == "Чотири сири":
            amount = int(input("Скільки штук? "))

            four_cheese_amount += amount
            total += four_cheese_cost * amount

        else:
            print("Такої піцци у нас немає, спробуйте ще раз.")
            continue

        print(f"Замовлено піццу {pizza} {amount} шт")

    elif option == 2:
        print("Гарного вам дня!")
        break

    elif option == 3:
        print()
        print("==========ВАШЕ ЗАМОВЛЕННЯ==============")
        print("\nПіцца  \tКількість \tВартість")

        print("--------------------------------------")

        if margherita_amount > 0:
            print(
                f"Маргарита \t{margherita_amount} \t{margherita_amount * margherita_cost} грн"
            )

        if peperoni_amount > 0:
            print(
                f"Пепероні \t{peperoni_amount} \t{peperoni_amount * peperoni_cost} грн"
            )

        if four_cheese_amount > 0:
            print(
                f"Чотири сири \t{four_cheese_amount} \t{four_cheese_amount * four_cheese_cost} грн"
            )

        print("\n---------------------------------------")
        print(f"Загальна вартість: {total} грн")
        print("=========================================")
        print("Дякуємо за замовлення!")
