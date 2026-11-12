import os

os.system('cls') 

# ** -- піднесення до степення
# a = 5
# side = a ** 2
# print(side)

# # / -- ділення, результат завжди float!!!!!!!!
# res = 10 / 3
# print(res)

# # // -- цілочисельне ділення, результат завжди int!!!!!!!
# apples_per_person = 17 // 3
# print(apples_per_person)

# # долар у нас по 45.5, у мене 120 грн, скільки цілих долларів можна отримати
# whole_usd = 120 / 45.5
# print(whole_usd)

# # % -- остача від ділення
# rest_apple = 17 % 3
# print(rest_apple)

# # f рядки
# print(f"\nу вас залишилося {rest_apple} яблук")

# Округлення кількості знаків після коми -- :.xf

uah = 180
usd = uah / 45.05
print(f"Ваші {uah} гривень це {usd:.5f} доларів")

# пиріжок коштує 35 грн, користувач вводить свій бюджет. 
# вивести скільки пиріжків він може купити

balance = float(input("Введіть ваш баланс: "))
pastry_price = 35

# кількість пиріжків

pastry_count = balance // pastry_price 
print(f"ви можете купити {pastry_count:.0f} пиріжків")