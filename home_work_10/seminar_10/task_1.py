# Задание No1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Сircle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        return round(math.pi * pow(self.radius, 2), 2)


circle1 = Сircle(70)
print(circle1.circumference())
print(circle1.square())
