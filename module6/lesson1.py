import os

os.system("cls")

# рядки

# створення

# a = 'hi'        # одинарні

# b = "hi"        # подвійні

# c = """ hi
# here is some text """ # потрійні

# # об'єднання рядків

# name = "John"
# hello = "Hello ", name, "!"

# print(hello)

# множення рядків

# text = "ha" * 4

# print(text)
# print("*" * 5)

# # "text" * 4.3  -- Забороненно


# result = min(3, 7)
# print(result)


# знайти довжину рядка

# text = "Python"
# length = len(text)

# print(f"У слові {text} рівно {length} символів")


# цикл for

# text = "Hello, world!"

# for num in range(3):
#     print(num)

# for symbol in text:
#     print(symbol)


# if -- in

# text = "Мама мила раму"

# if "мила" in text:
#     print("YES!")

# else:
#     print("NO")


# # not in -- заперечення


# if "зброя" not in text:
#     print("Немає")

# else:
#     print("Є")


# функції та методи

# функції

# [назва функції](параметри)

# print("hello")
# input("Введіть число:")
# min(4, 6)

# методи

# [об'єкт].[назва методу](параметри)


# text = "PytHoNt"

# # нижній регістер
# lower_text = text.lower()
# print(f" {lower_text = } ")

# # верхній регістер
# upper_text = text.upper()
# print(f" {upper_text = } ")

# # рахування символів
# count_t = text.count("t")
# print(f" {count_t = } ")

# заміна -- replace

# phrase = "Я люблю чай"
# new = phrase.replace("чай", "каву")

# print(new)
# print("banana".replace("a", "o"))

# print("10".isdigit())

# text = "Python 3.12"

# for ch in text:
#     if ch.isdigit():
#         print(f"{ch} -- цифра")

#     elif ch.isalpha():
#         print(f"{ch} -- літера")

#     else:
#         print(f"{ch} -- щось інше")

# позбутися білих символів (Enter, Space, Tab)
user_text = input("Введіть ваш текст: ")

# позбутись пропусків по краям
user_text = user_text.strip()

if user_text != "":
    print(user_text)

else:
    print("Ви нічого не ввели")
