# Задание No2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.
def get_dict_val(dict, key, val):
    try:
        return dict[key]
    except Exception:
        return val


d = {1: 2, 3: 654, 6: 'hi'}
print(get_dict_val(d, 6, 99))
