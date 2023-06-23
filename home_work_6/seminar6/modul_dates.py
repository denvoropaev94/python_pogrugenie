# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM. YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


def my_date_info(date: str):
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year <= 9999 and 1 <= month < 13 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day < 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            return _leap_year(year) and day <= 29


if __name__ == '__main__':
    print(my_date_info("29.02.2023"))
    print(my_date_info("12.11.1994"))
    print(my_date_info("32.12.2022"))
    print(my_date_info("29.22.1923"))
    print(my_date_info("29.07.10000"))
