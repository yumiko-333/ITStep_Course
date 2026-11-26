import os

os.system("cls")

# Завдання 1
#
#  Створіть список чисел [1, 8, -5, 9]
#
# ● Виведіть на екран елементи цього списку
#   ● Збільшіть кожне число в 3 рази та виведіть результат
#       ● Замініть усі числа більші 10 на 0 та виведіть результат

# numbers = [1, 8, -5, 9]

# for number in range(len(numbers)):
#     numbers[number] *= 3

# print(f"Числа помноженні на 3 -- {numbers}")

# for number in range(len(numbers)):
#     if numbers[number] > 10:
#         numbers[number] = 0

# print(f"Числа більше 10 -- 0: {numbers}")

# ----------------------------------------------------------------------------------------

# Завдання 2
#
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
#
#  Скористайтесь функціями min, max, sum, len

# numbers = []

# while True:
#     number = int(input("Введіть ваше число (-1 для завершення): "))

#     if number == -1:
#         print("Програму завершено!")
#         break

#     numbers.append(number)

# min_numbers = min(numbers)
# max_numbers = max(numbers)
# sum_numbers = sum(numbers)
# len_numbers = len(numbers)

# average = sum_numbers / len_numbers

# print(f"\n Мінімальне: {min_numbers} \nМаксимальне: {max_numbers}")
# print(f"Кількість: {len_numbers} \nСума: {sum_numbers} \nСереднє: {average}")

# --------------------------------------------------------------------------------------

# Завдання 3
#
#  Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
#
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#     # тут має бути перевірка чи не ввів користувач 0, якщо ввів, завершити програму
#     # з цим кодом програму завершити не можливо
#     positive = []       # списки мають бути створені до циклу, тому що вони постійно оновлюються через цикл
#     negative = []

#     if number < 0:
#         positive.append(number)     # тут переплутано місцями positive.append та negative.append, треба замінити їх місцями щоб все було правильно
#     else:
#         negative.append(number)

# print("Додатні числа:", positive)       # цей блок коду взагалі не працює тому що цикл нескінченний
# print("Від'ємні числа:", negative)

# ПРАВИЛЬНИЙ ВАРІАНТ КОДУ \/\/\/

# positive = []
# negative = []


# while True:
#     number = int(input("Введіть число (0 для завершення): "))

#     if number == 0:
#         break

#     if number < 0:
#         negative.append(number)
#     else:
#         positive.append(number)

# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

# -----------------------------------------------------------------------------------

# Завдання 4
#
#   Користувач вводить зарплати співробітників, поки не
#   введе -1. Після чого вводить відсоток на який треба
#   збільшити усім зарплату.
#
#       Виведіть нові зарплати

# salaries = []

# while True:
#     salary = int(input("Введіть зарплати співробітників: "))

#     if salary == 0:
#         break

#     salaries.append(salary)

# percent = int(input("\nВведіть відсоток на який потрібно підняти зарплати: "))

# for i in range(len(salaries)):
#     salaries[i] = salaries[i] * (1 + percent / 100)

# print(f"Нові зарплати: {salaries}")

# ----------------------------------------------------------------------------------

# Завдання 5
#
#  Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
#
#   Збережіть температури у список
#
#       Для кожного дня порахуйте різницю температур з
#       попереднім днем.
#
#           Виправіть помилку в коді

# days = int(input("Введіть кількість днів: "))

# for i in range(days):
#     temperatures = []               # список створюється в циклі, тому весь час обнуляється
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)

# print("Температури:", temperatures)

# for i in range(days):           # тут має бути не days а len(temperatures), тому що далі йдуть обчислення саме з цим списком та індексом
#     difference = temperatures[i] - temperatures[i - 1]
#     print(f"Різниця температур за {i + 1}-й день: {difference}")


# temperatures = []

# days = int(input("Введіть кількість днів: "))

# for i in range(days):
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)

# print("\nТемператури:", temperatures)
# print()

# for i in range(len(temperatures)):
#     difference = temperatures[i] - temperatures[i - 1]

#     print(f"Різниця температур за {i + 1}-й день: {difference}")

# -----------------------------------------------------------------------------------------

# Завдання 6
#
#  Створіть застосунок банк. Є список з рахунками
# клієнтів.
#
# Користувач вибирає одну з команд
#
# ● Додати клієнта
# ● Видалити клієнта
# ● Поповнити рахунок
# ● Зняти кошти
# ● Вихід
#
#  При додаванні клієнта, добавте рахунок в 0грн в
#  кінець списку.
#
#  В інших випадках запросіть ID(індекс) клієнта і якщо
# він вірний, то проведіть операцію

clients_balance = []

print(
    "1. Додати клієнта \n2. Видалити клієнта \n3. Поповнити рахунок \n4. Зняти кошти \n5. Вихід"
)

while True:
    choise = int(input("\nВиберіть команду: "))

    if choise == 5:
        print("Вихід..")
        break

    if choise == 1:
        print("Клієнта додано!")
        clients_balance.append(0)

    elif choise == 2:
        print("Клієнта видалено!")
        clients_balance.pop()

    elif choise == 3:
        ask_id = int(input("Ваш ID: "))

        if 0 < ask_id < len(clients_balance):
            print("Клієнта знайдено!")

            income = int(input("Скільки грошей поповнити: "))
            clients_balance[ask_id] += income

            print("Рахунок поповнено!")

        else:
            print("Клієнта не знайдено.")

    elif choise == 4:
        ask_id = int(input("Ваш ID: "))

        if 0 < ask_id < len(clients_balance):
            print("Клієнта знайдено!")

            outcome = int(input("Скільки грошей зняти: "))

            if clients_balance[ask_id] >= outcome:
                print("Гроші знято!")
                clients_balance[ask_id] -= outcome

            else:
                print("Недостатньо коштів на рахунку.")

        else:
            print("Клієнта не знайдено.")

    else:
        print("Такої команди немає. Спробуйте ще раз. ")

print(f"Рахунки клієнтів: {clients_balance}")
