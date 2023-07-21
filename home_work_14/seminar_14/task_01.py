# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.
from string import ascii_lowercase


def removal_chars(text):
    result = ''
    for i in text.lower():
        if i in ascii_lowercase + ' ':
            result += i
    return result

print(removal_chars('denis453t5-==-=-435t5g5g4gg 5vorop453645:::a3243ev'))