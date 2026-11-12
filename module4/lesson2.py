import os

os.system('cls')


# цикл while

# water = 0

# while water < 200:
#     water += 50

#     print(f"{water = }")
#     print(f"{water < 200 = }")
#     print()

# print("цикл закінчився")
# print(f"{water < 200 = }")


# спеціально нескінченний цикл \/\/

# while True:
#     print("цей цикл працює вічно") 

#     # якщо тут можна перевірити чи треба зупинити цикл то робимо тут



# while True:
#     key = input("Ви знайшли ключ?")

#     if key == "так":
#         break

#     print("Продовжуємо шукати")

# print("Пошук завершено")

# підрахунок кілометражу

# total_dist = 0

# while True:
#     is_driven = input("Авто ще їде?")

#     if is_driven == "ні":
#         break

#     dist = int(input("Сккільки проїхали кілометрів?"))

#     total_dist += dist

#     print(f"Ви проїхали {total_dist} км")



# перевірка чи ввів користувач щось правильно
# так/ні

while True:
    answer = input("Введіть так/ні ")

    # коли закінчуємо цикл 
    if answer == "так" or answer == "ні":
        break

    print("Ви ввели неправильну відповідь")
    print()

print(f"ви ввели відповідь -- {answer}")

