# Задание No1
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.
def func_numbers():
    while True:
        try:
            num = input('Введите число! ')
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError as e:
            print('Вы ввели не число, пробуйте еще')


func_numbers()
