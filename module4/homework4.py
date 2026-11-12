import os

os.system('cls')

# Завдання 1

# Напишіть програму для роботи онлайн магазину.

# Товари:

# ● подушка – 650 грн
# ● ковдра – 1700 грн
# ● лампа – 500 грн
# ● брелок – 60 грн

# Меню дій:

# ● додати товар
# ● видалити товар
# ● очистити кошик
# ● показати вміст кошики та суму покупки
# ● вихід

# Користувачу показується меню один раз на початку
# програми

#   Користувач вибирає номер дії після чого за потреби
#   вводить назву товару то його кількість

# У випадку неправильно введених даних повідомити про
# це та повернутись до вибору номера дії

#   Створіть для кожного товару змінну з кількістю цього
#   товару у кошику для подальшої роботи

print("Товари: \n● подушка – 650 грн \n● ковдра – 1700 грн \n● лампа – 500 грн \n● брелок – 60 грн")
print("\nМеню дій: \n● додати товар \n● видалити товар \n● очистити кошик \n● показати вміст кошики та суму покупки \n● вихід")

print()

pillow = 0
blanket = 0
lamp = 0
keychain = 0

while True:
    choise = int(input("\nВиберіть дію з меню (1, 2, 3, 4, 5): "))

    if choise < 1 or choise > 5:
        print("Неправильно вибрана дія!")
        continue

    if choise == 1:
        item = input("Виберіть потрібний вам товар: ")
        amount = int(input("Скільки штук? "))

        if amount <= 0:
            print("Кількість не може бути 0, або меньше!")

        if item == "подушка":
            pillow += amount

        elif item == "ковдра":
            blanket += amount
    
        elif item == "лампа":
                lamp += amount
    
        elif item == "брелок":
                keychain += amount
    
        else:
            print("Немає у наявності")
            continue
    
    elif choise == 2:
        item = input("Виберіть потрібний вам товар: ")
        amount = int(input("Скільки штук? "))

        if amount <= 0:
            print("Кількість не може бути 0, або меньше!")

        if item == "подушка":
            pillow -= amount
            
            if pillow < 0:
                pillow = 0

        elif item == "ковдра":
            blanket -= amount
    
            if blanket < 0:
                 blanket = 0

        elif item == "лампа":
                lamp -= amount
    
                if lamp < 0:
                     lamp = 0

        elif item == "брелок":
                keychain -= amount

                if keychain < 0:
                     keychain = 0

        else:
            print("Немає у наявності")
            continue

    elif choise == 3:
        pillow = 0 
        blanket = 0
        lamp = 0
        keychain = 0

        print("Кошик очищено!")
    
    elif choise == 4:
        total = (pillow * 650 + blanket * 1700 + lamp * 500 + keychain * 60)

        print("\nВМІСТ КОШИКА")
        print(f"Подушка: {pillow}")
        print(f"Ковдра: {blanket}")
        print(f"Лампа: {lamp}")
        print(f"Брелок: {keychain}")

        print(f"\nСума покупок: {total} грн")

    elif choise == 5:
         print("До побачення")
         break
    
    
         