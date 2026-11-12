import os

os.system('cls')

# Користувач вводить суму в гривнях поки не введе 0
# вивести скільки це доларів

# USD_RATE = 45.49

# while True:
#     uah = float(input("Введіть суму в гривнях: "))

#     # якщо ввели 0 
#     if uah == 0:
#         break

#     # користувач ввів неправильне число
#     if uah < 0:
#         print("Ви ввели від'ємне число!")
#         continue

#     # основна програма
#     usd = uah / USD_RATE

#     print(f" {uah:.2f} грн це {usd:.2f}$ ")
#     print()

# --------------------------------------------------

# Початковий вклад в банк -- 1000 грн 

# balance = 1000
# target_balance = 1100

# percent = 10 # 10% нарахувань щомісяця
# months = 0

# while balance < target_balance:
#     # нараховуємо
#     balance *= 1 + percent / 100

#     # оновлюємо лічильник місяців
#     months += 1

#     print(f"Після {months} місяців, ваш вклад буде {balance:.2f} грн")


# ----------------------------------------------------------

# те саме з циклом for

# for months in range(1, 1000000):
#     balance *= 1 + percent / 100

#     if balance > target_balance:
#         break

#     print(f"Після {months} місяців, ваш вклад буде {balance:.2f} грн")

# --------------------------------------------------------

USD_RATE = 45.49
EURO_RATE = 50.2646
JPY_RATE = 0.27198

while True:
    print("1. доллар")
    print("2. євро")
    print("3. єни")
    print("4. вихід")

    command = int(input("виберіть номер команди: "))

    if command == 4:
        print("програма завершена")
        break

    if command < 1 or command > 4:
        print("Неправильне число")
        continue

    uah = float(input("Введіть суму у гривнях: "))

    if uah < 0:
        print("Неправильне число")
        continue

    if command == 1:
        rate = USD_RATE
        symbol = "долларів"

    elif command == 2:
        rate = EURO_RATE
        symbol = "євро"
    else:
        rate = JPY_RATE
        symbol = "єн"

    result = uah / rate
    print(f"Це буде {result:.2f} {symbol} ")
    print()