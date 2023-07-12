class Matrix:
    """Матрица, сложение и сравнение"""

    def __init__(self, val):
        if isinstance(val, list):
            if isinstance(val[0], list):
                self.val = val
            else:
                self.val = [val]
        else:
            self.val = [[val]]

    def __add__(self, other):
        m1 = self.val  # матрица 1
        m2 = other.val  # матрица 2
        # соответствие по размеру
        if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
            out = m1
            for row in range(len(m1)):
                for col in range(len(m1[0])):
                    out[row][col] += m2[row][col]
        # матрица 1 скалярная, а вторая нет
        elif len(m1) == 1 and len(m1[0]) == 1:
            out = m2
            for row in range(len(m2)):
                for col in range(len(m2[0])):
                    out[row][col] += m1[0][0]
        # матрица 2 скалярная, а первая нет
        elif len(m2) == 1 and len(m2[0]) == 1:
            out = m1
            for row in range(len(m1)):
                for col in range(len(m1[0])):
                    out[row][col] += m2[0][0]
        else:
            return None

        return Matrix(out)


    def __str__(self) -> str:
        """Для пользователя"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.val]) + '\n'

    def __repr__(self):
        """для программиста"""
        return f'Matrix({self.val})'

    def size(self):
        """Размер матрицы"""
        matrix = self.val
        return f'Матрица размером {len(matrix)} на {len(matrix[0])}'

    def transponse(self):
        """Транспонирование матрицы"""
        matrix = self.val
        transpon_matrix = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]

        return Matrix(transpon_matrix)

    def __mul__(self, other):
        """Перемножение матриц"""
        m1 = self.val
        m2 = other.transponse().val
        out = []
        if len(m1) == len(m2[0]) and len(m1[0]) == len(m2):
            resultant_matrix = [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]
            for r in resultant_matrix:
                out.append(r)
            return Matrix(out)
        else:
            raise ValueError

    def __eq__(self, other):
        """Сравнение матриц"""
        matrix = self.val
        sum_1 = 0
        for line in matrix:
            sum_1 += sum(line)
        sum_2 = 0
        for line in other.val:
            sum_2 += sum(line)
        return sum_1 == sum_2



matrix1 = Matrix([[1, 2, 3], [6, 4, 5]])
matrix2 = Matrix([[7, 8, 9], [5, 1, 7]])
matrix3 = Matrix([10, 15, 30])
matrix4 = Matrix(1)
matrix5 = Matrix([[1, 2, 3], [6, 4, 5]])

# print(matrix3)
# print(matrix3.size())
print(matrix1)
print(matrix2.transponse())
print(matrix1 * matrix2)
# print(matrix1 == matrix5)

# print(matrix2.transponse())
