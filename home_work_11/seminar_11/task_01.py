# Задание No1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
import datetime
import time


class MyStr(str):
    """Класс моя строка, где будут доступны все возможности str"""
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

first = MyStr('Real Madrid', 'Voropaev')
print(f'Название: {first}, автор: {first.name}, time: {first.date}')