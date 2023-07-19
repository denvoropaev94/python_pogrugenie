# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

class MyLengtWidthError(Exception):
    def __init__(self, *args):
        self.string = args[0]
        super().__init__(*args)

    def __str__(self):
        return f"Нельзя создавать прямоугольник со сторонами отрицательной длины {self.string}"


class ValueCheck:

    def __init__(self, min_value):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise MyLengtWidthError(f'{self.min_value}')


class Rectangle:
    _length = ValueCheck(1)
    _width = ValueCheck(1)

    def __init__(self, length, width=None):

        self._length = length
        if width:
            self._width = width
        else:
            self._width = length

    @property
    def length(self):
        return self._length

    @property
    def wigth(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise MyLengtWidthError('0')

    @wigth.setter
    def wight(self, value):
        if value > 0:
            self._width = value
        else:
            raise MyLengtWidthError('0')

    def square(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


sq = Rectangle(11, 20)
print(sq.square())
print(sq.perimeter())
sq.length = 0
print(sq.square())
print(sq.perimeter())
