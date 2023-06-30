# Задание No2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import random


def user_input():
    list_users = []
    while True:
        name = input("Input name: ").title()
        if not name:
            return list_users
        while True:
            user_id = random.randint(10_000, 100_000)
            if user_id not in [uid[2] for uid in list_users]:
                break
        while True:
            level = input("Input level: ")
            if level.isdigit() and 0 < int(level) < 8:
                list_users.append((name, user_id, level))
                break


# print(user_input())
def json_write():
    user_list = user_input()
    result_dict = {}
    for user in user_list:
        # print(user[2])
        if user[2] in result_dict:
            result_dict[user[2]].update({user[1]: user[0]})
        else:
            result_dict[user[2]] = {user[1]: user[0]}

    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)


json_write()
