import json
import os

path = os.getcwd()


def recursive_traversal(path, level=1):
    my_dict = {}
    print('Уровень=', level, 'Содержимое:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isfile(path + '/' + i):
            size = os.path.getsize(path + '/' + i)
            print(i, 'This is file', 'Размер:', size)
            # my_dict[i] = size
        elif os.path.isdir(path + '/' + i):
            size = os.path.getsize(path + '/' + i)
            print(i, 'This is dir', 'Размер:', size)
            # my_dict[i] = size
            print('Спускаемся', path + '/' + i)
            recursive_traversal(path + '/' + i, level + 1)
            print('Возвращаемся в ', path)
    if my_dict:
        with open('my_file.json', 'a', encoding='utf-8') as f:
            json.dump(my_dict, f)
    # print(my_dict)


recursive_traversal(path)
