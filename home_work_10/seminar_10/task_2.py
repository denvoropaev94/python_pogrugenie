# Задание No2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def perimeter(self):
        if (self.length and not self.width):
            return self.length * 4
        else:
            return (self.length + self.width) * 2

    def square(self):
        if (self.length and not self.width):
            return self.length ** 2
        else:
            return self.length * self.width


rect1 = Rectangle(5, 10)
rect2 = Rectangle(11)
print("Прямоугольники")
print(rect1.perimeter())
print(rect1.square())
print('квадрат')
print(rect2.perimeter())
print(rect2.square())
