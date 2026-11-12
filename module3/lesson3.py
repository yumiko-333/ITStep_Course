import os

os.system('cls')

# константи
# BALL_PRICE = 30
# SYRUP_CARAMEL = 5
# SYRUP_CHOCOLATE = 4
# SYRUP_STRAWBERRY = 7

# DISCOUNT = 10

# ice_cream_balls = int(input("Скільки кульок морозива бажаєте: "))
# with_syrup = input("Ви бажаєте сироп(так, ні)? ")

# syrup = None

# if with_syrup == "так":
#     syrup = input("Який сироп бажаєте (карамельний чи шоколадний чи полуничний) ? ")

# total = ice_cream_balls * BALL_PRICE

# if syrup == "карамельний":
#     total += SYRUP_CARAMEL
# elif syrup == "шоколадний":
#     total += SYRUP_CHOCOLATE
# elif syrup == "полуничний":
#     total += SYRUP_STRAWBERRY


# if with_syrup == "так" and ice_cream_balls >= 3:
#     discount = total * DISCOUNT / 100
#     total -= discount

# print(f"за  {ice_cream_balls} кульок ")

# if with_syrup == 'так':
#     print(f"разом з {syrup} сиропом")

# print(f"з вас {total} гривень")

# -------------------------------------------------------------------

# ведіння авто

age = int(input("Введіть ваш вік: "))

if age < 18:  # неповнолітній
    print("Надто малі")
else:
    has_license = input("В вас є водійські права? (так, ні)")

    if has_license == "так":
        print("Можна водити авто")
    else:
        print("В вас немає ліцензії, отримуйте права")