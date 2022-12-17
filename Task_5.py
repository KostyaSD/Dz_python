import math

aX = float(input('Введите координаты точки A по оси x: '))
aY = float(input('Введите координаты точки A по оси y: '))
bX = float(input('Введите координаты точки B по оси x: '))
bY = float(input('Введите координаты точки B по оси y: '))

distans = round(math.sqrt((aX - bX) ** 2 + (aY - bY) ** 2), 2)

print(f"Растояние между точками A и B = {distans}")
