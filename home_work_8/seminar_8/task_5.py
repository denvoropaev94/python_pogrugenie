# Задание No3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
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
def csv_write_users():
    user_list = user_input()
    result_dict = {}
    for user in user_list:
        if user[2] in result_dict:
            result_dict[user[2]].update({user[1]: user[0]})
        else:
            result_dict[user[2]] = {user[1]: user[0]}

    with open('users.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writerow(('name', 'id', 'level'))
        for user in user_list:
            csv_write.writerow(user)


csv_write_users()
