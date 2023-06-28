# Задание No5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import os
import random
from random import choice, randint,randbytes,sample
from string import ascii_letters


def random_ext(list_ext: list[str]) -> str:
    return random.choice(list_ext)


def create_files(extension: list[str], min_name: int = 6, max_name: int = 30,
                 min_size: int = 256, max_size: int = 4096, amount: int = 42):
    for _ in range(amount):
        name_size = randint(min_name, max_name)
        ext = random_ext(extension)
        file_name = ''.join(sample(ascii_letters, name_size)) + "." + ext
        file_name = os.path.join('data', file_name)
        with open(file_name, 'ab') as file:
            size = randint(min_size, max_size)
            result = randbytes(size)
            file.write(result)


create_files(['txt', 'md', 'rtf', 'doc'], amount=12)
