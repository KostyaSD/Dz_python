
number = int(input("Введите номер четверти: "))
if number < 1 or number > 4:
    print("Вы указали не верную четверть!")
elif number == 1:
    print("x > 0 and y > 0")
elif number == 2:
    print("x < 0 and y > 0")
elif number == 3:
    print("x < 0 and y < 0")
elif number == 4:
    print("x > 0 and y < 0")
