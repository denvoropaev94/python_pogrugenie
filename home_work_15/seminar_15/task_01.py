# Задание No1
# 📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.
import random
import logging


def by_zero():
    num = int(input("Введите любое число: "))
    if num == 0:
        logging.basicConfig(filename='logi.log', filemode='a', encoding='utf-8', level=logging.INFO)
        logging.info('ZeroDivisionError: division by zero')
    rn = random.randint(1, 1000)
    new_num = rn / num
    return rn, new_num


print(by_zero())
