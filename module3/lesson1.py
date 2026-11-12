import os

os.system('cls')


# temperature = 5

# if temperature < 10:
#     print("Вдягни куртку")
# else:
#     print("нормалди")

# temperature = 20

# if temperature < 0:
#     print("Мороз")
# elif temperature < 15:
#     print("Прохолодно")
# else:
#     print("Жарко")


# користувач вводить назву товару, вивести інфу про товар

is_purchased = False 


product = str(input("Введіть назву товару: "))

if product == "Пиріжок":
    is_purchased = True
    print("З вишнею?")
elif product == "Морозиво":
    is_purchased = True
    print("Пломбір?")
else:
    print("Немає у наявності")

if is_purchased:
    print("Дякуємо за покупку")
else:
    print(f"Можливо ви знайдете {product} в іншому магазині!")

print("Гарного дня!")