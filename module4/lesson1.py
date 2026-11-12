import os

os.system('cls')

# Цикл for

# for house in 1,2,3:
#     print("\nЛистоноша прийшов")
#     print(f"листи для будинку №{house}")


# щоб легко задати послідовність є функція range

#range(stop) -- 0, 1, 2, ... stop-1 (початок з 0, кінець не включно)

# for num in range(5):
#     print(num)

# range(start, stop) -- start, start+1, ... stop-1 (початок та кінець (навколо діапазону))

# for num in range(4, 10):
#     print(num)

# range(start, stop, step) -- початок start, кінець stop-1, step

# for i in range(4, 56, 4):
#     print(i)

# рахувати задом наперед

# for i in range(5, 0, -1):
#     print(i)

# змінні у циклі
# порахувати суму чисел та їхню кількість

# total = 0 
# count = 0

# for num in range(10,20):
#     total += num
#     count += 1

# print(f"Сума {total} \nКількість {count}") 


count = int(input("скільки разів: "))
for i in range(count):
    print("hi", i)
