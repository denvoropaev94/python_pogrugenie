class Rectangle:
    """Класс прямоугольник """
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

    def __add__(self, other):
        new_l = self.length + other.length
        new_w = self.width + other.width
        return Rectangle(new_l, new_w)

    def __sub__(self, other):
        if self.length - other.length < 0 or self.width - other.width < 0:
            raise ValueError
        new_l = self.length - other.length
        new_w = self.width - other.width
        return Rectangle(new_l, new_w)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()


rect1 = Rectangle(11, 14)
rect2 = Rectangle(11, 14)
# print("Прямоугольники")
# print(rect1.perimeter())
# print(rect1.square())
# print('квадрат')
# print(rect2.perimeter())
# print(rect2.square())
rect3 = rect1 + rect2
rect4 = rect2 - rect1
# print(rect3.perimeter())
# print(rect4.perimeter())
#
# rect5 = rect1 - rect2
print(rect1 == rect2)
help(Rectangle)
