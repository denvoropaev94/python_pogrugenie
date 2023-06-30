# Задание No1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
import json

with open('test.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()

new_dict = {}

for line in my_list:
    line = line.strip().split(" ")
    new_dict[line[0].title()] = line[1]
# print(new_dict)
with open('result.json', 'w') as f:
    json.dump(new_dict, f, indent=4, ensure_ascii=False)
