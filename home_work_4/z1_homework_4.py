# Напишите функцию для транспонирования матрицы
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpon_matrix = [[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
print(matrix)
print(transpon_matrix)

# 2 cпособ
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# zip_rows = zip(*matrix)
# transpose_matrix = [list(row) for row in zip_rows]
# print(transpose_matrix)