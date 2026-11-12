import os

os.system('cls')

# age = 20
# has_ticket = True

# if age >= 18 and has_ticket:
#     print("Прохід дозволено!")
# else:
#     print("Прохід заборонено!")

day = "неділя"

if day == "неділя" or day == "субота":
    print("вихідний")
else:
    print("робочій")

# перетворення у тип даних bool

# text = "3.6"
# cond = bool(text)

# print(cond)

# 0 -- False, всі інші -- True
# порожній рядок -- False, якщо написано хоч щось -- True

# по номеру місяця виводиться пора року

month_num = 7

if month_num == 12 or month_num == 1 or month_num == 2:
    print("зима")
elif month_num >= 3 or month_num <= 5:
    print("весна")
elif month_num >= 6 or month_num <= 8:
    print("літо")
else:
    print("осінь")