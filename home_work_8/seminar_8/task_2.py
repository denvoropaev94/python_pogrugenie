# Zадание No6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import os
import pickle
import csv

ext = 'pickle'

def pickle_to_csv(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            origin_name, origin_ext = os.path.join(file).split(".")
            if origin_ext == ext:
                with open(file, 'rb') as f:
                    my_dict = pickle.load(f)
                    origin_name = origin_name + '.csv'
                    with open(origin_name, 'w',) as f:
                        csv_file = csv.DictWriter(f, fieldnames=[value for value in my_dict],
                                                  dialect='excel', quoting=csv.QUOTE_ALL)
                       csv_file.writeheader()
                    # print(f'{my_dict = }')


pickle_to_csv(os.path.join(os.getcwd()))



