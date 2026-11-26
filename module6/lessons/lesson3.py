import os

os.system("cls")

# списки

# створення через list

# послідовності -- range, str, list

# num = "123456"
# num_list = list(num)

# print(num_list)

# nums = list(range(10, 20))
# print(nums)

# порожній список

# users = []

# animals = ["кіт", "пес", "мишка"]
# ages = [18, 45, 48, 60]

# for animal in animals:
#     print(animal)

# print("кіт" in animals)
# print(18 in ages)
# print(19 in ages)

# colours = ["green", "red", "blue", "purple", "yellow"]

# print(colours[1])

# print(colours[2:4])

# colours[0] = "purple"
# print(colours)

# colours_copy = colours.copy()

# colours[0] = "purple"
# print(f"{colours = }")

# print(f"{colours_copy = }")

# списко зарплат

# треьа додати по 200

salaries = [800, 1000, 1500]

# for salary in salaries:
#     salary += 200
#     print(salary)

# print(salaries)

# for i in range(len(salaries)):
#     salaries[i] += 10

# print(f"{salaries =}")

# salaries.append("Peter")        ДОДАТИ
last = salaries.pop(0)

names = ["Ivan", "Оля", "Bob"]

if "Ivan" in names:
    names.remove("Ivan")

print(names)

names.uppend("Богдан")

print(names)
