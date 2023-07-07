# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if ((self.a + self.b) > self.c) and ((self.a + self.c) > self.b) and ((self.b + self.c) > self.a):
            print(f'Такой трегольник существует!УРА')
            if self.a == self.b == self.c:
                return f'Треугольник равносторонний'
            elif (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) \
                    or (self.b == self.c and self.b != self.a):
                return f'Треугольник равнобедренный'
            else:
                return f'Треугольник разносторонний'
        else:
            return f'Такой треугольник не существует!'


tre = Triangle(5, 5, 15)
print(tre.check_triangle())
