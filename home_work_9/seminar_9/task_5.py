# Задание No5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# декораторами для сохранения параметров,
# декоратором контроля значений и
# декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.
import json
import os
from typing import Callable
import random
from functools import wraps

def counter(number: int = 5):
    def doc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return doc

def proverka(func) -> Callable:
    @wraps(func)
    def wrapper(guess: int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
        return func(guess, attempts)
    return wrapper

def writer(file_name) -> Callable:
    def inner_func(func):
        @wraps(func)
        def wrapper(number, tries):
            my_dict = {str(func(number, tries)):(number, tries)}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f,indent=4, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f,indent=4, ensure_ascii=False)
            return func(number,tries)
        return wrapper

    return inner_func


@writer('game.json')
@proverka
@counter(3)
def game_guess(num_sc, attempts):
    """ Game for the clever mens !!!"""
    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            return attempts
        else:
            advice = ['lesser', 'greater']
            print(f'Your number is {advice[num > num_sc]} then right')

    else:
        print(f'You loose. Right number is {num_sc}')
    return attempts


# if __name__ == '__main__':
#     game_guess(123, 231)
help(game_guess)