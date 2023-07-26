# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
import logging


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if ((self.a + self.b) > self.c) and ((self.a + self.c) > self.b) and ((self.b + self.c) > self.a):
            logging.basicConfig(filename='log_tr.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
            logging.info('Треугольник существует! УРА!')
            if self.a == self.b == self.c:
                logging.info('Треугольник равносторонний!')
                return f'Треугольник равносторонний'
            elif (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) \
                    or (self.b == self.c and self.b != self.a):
                logging.info('Треугольник равнобедренный!')
                return f'Треугольник равнобедренный'
            else:
                logging.info('Треугольник разносторонний!')
                return f'Треугольник разносторонний'
        else:
            logging.basicConfig(filename='log_tr.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
            logging.info('Такой треугольник не существует!')
            return f'Такой треугольник не существует!'


tre = Triangle(5, 5, 5)
print(tre.check_triangle())
