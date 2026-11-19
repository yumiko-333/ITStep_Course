import os

os.system("cls")

# Завдання 1

# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:

# ● з методом count
# ● з циклом for

# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази

# метод count \/\/

# text = "it is amazing"
# count_i = text.count("i")

# print(f"B {text} символ 'i' зустрічається {count_i} рази")

# метод for \/\/

# text = "it is amazing"
# count_i = 0

# for symbol in text:
#     if symbol == "i":
#         count_i += 1

# print(f"B {text} символ 'i' зустрічається {count_i} рази")

# ---------------------------------------------------------------------------------------------

# Завдання 2

# Користувач вводить рядок. Виведіть наступну
# інформацію:

# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

user_line = input("Write down your line: ")
length = len(user_line)

secret_word = "python"

if secret_word in user_line:
    print(f"{secret_word} є у вашому рядку!")

else:
    print(f"{secret_word} немає у вашому рядку")
