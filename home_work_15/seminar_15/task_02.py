import logging
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='logi_2.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
        logging.info(f'Запуск функции {func.__name__} с аргументом {args}')
        result = func(*args, **kwargs)
        logging.info(f'Результат функции {func.__name__}: {result}')
        logging.info(f'Завершение функции {func.__name__}')
        return result

    return wrapper


@main
def my_factorial(number: int):
    if number == 1:
        return 1
    else:
        return number * my_factorial(number - 1)


print(my_factorial(14))
