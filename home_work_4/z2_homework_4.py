# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.


def dict_key_parameters(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[value] = key
    return new_dict

print(dict_key_parameters(kirill= 10, nik= 9, oleg=5))