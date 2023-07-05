# Задание No3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.
import json
import os
from typing import Callable


def outer(file_name) -> Callable:
    def inner_func(func):
        def wrapper(*args, **kwargs):
            my_dict = {func(*args, **kwargs): [arg for arg in args] + [(key, value) for key, value in kwargs.items()]}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f,indent=4, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f,indent=4, ensure_ascii=False)
            return func(*args, **kwargs)

        return wrapper

    return inner_func


@outer('new_file.json')
def func_json(*args, **kwargs) -> str:
    list_args = []
    list_kwargs = []
    if args:
        for i in args:
            list_args.append(i)
    if kwargs:
        for key, value in kwargs.items():
            list_kwargs.append(f'{key} = {value}')
    res_str = " ".join(list(map(str, list_args))) + " ".join(list(map(str, list_kwargs)))
    return res_str


print(func_json(43324, 32543, 234532, 124))
print(func_json(den='python', nik='java', oleg='nion'))
