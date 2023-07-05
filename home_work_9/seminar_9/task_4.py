# Задание No4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.


def counter(number: int = 5):
    def doc(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return doc


@counter(7)
def func_sum(a, b):
    return a + b


print(func_sum(13, 4))
