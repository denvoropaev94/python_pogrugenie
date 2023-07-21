# Задание No2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_lowercase
import doctest


def removal_chars(text):
    """
    >>> removal_chars('denis4535 vorop453645:::a3243ev') == ('denis voropaev')
    True
    >>> removal_chars('denis453t5-==-=-435t5g5g4gg 5vorop453645:::a3243ev') == ('denvoropaev')
    False
    """
    result = ''
    for i in text.lower():
        if i in ascii_lowercase + ' ':
            result += i
    return result

if __name__ == "__main__":
    doctest.testmod(verbose=True)
