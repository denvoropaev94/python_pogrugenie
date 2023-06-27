# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random


def zapolnenie(count_rows: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count_rows):
            input_random = str(random.randint(-1000, 1001)), str(random.uniform(-1000, 1001))
            f.write("|".join(input_random) + "\n")


zapolnenie(10, "zadanie_1.txt")
