# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from random import randint as rdt
from typing import Callable


def run_from_file(func) -> Callable:
    generation_csv()

    def wrapper():
        with open('generation_num.csv', 'r', encoding='utf-8') as f:
            numbers = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for number in numbers:
                if number and number[0] != 0:
                    func(*number)

    return wrapper


def json_result(func: Callable):
    result = {}

    def wrapper(*args):
        roots = func(*args)
        my_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        _key = 'home_work_9'
        result[_key] = result.get(_key) + [my_dict] if result.get(_key) else [my_dict]
        with open('result.json', 'w', encoding='UTF-8') as f:
            json.dump(result, f)
        return roots

    return wrapper


def generation_csv():
    with open('generation_num.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(rdt(100, 1000)):
            writer.writerow([rdt(-100, 100), rdt(-100, 100), rdt(-100, 100)])


@run_from_file
@json_result
def find_roots(*args):
    a, b, c = args
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        result = None
    elif discriminant > 0:
        x1 = (-b + pow(discriminant, 0.5)) / (2 * a)
        x2 = (-b - pow(discriminant, 0.5)) / (2 * a)
        result = round(x1, 2), round(x2, 2)
    elif discriminant == 0:
        x = -b / (2 * a)
        result = round(x, 2)
    return result


find_roots()

# generation_csv()
