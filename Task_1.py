
number = int(input("Введите число от 1 до 7: "))

if number < 1 or number > 7:
    print("Вы ввели не верное число!")
elif number > 5:
    print("Ура!! Выходной день")
else:
    print("Рабочий день!")
