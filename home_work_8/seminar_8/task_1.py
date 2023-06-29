# Напишите функцию, которая ищет json файлы в указанной директории и
# сохраняет их содержимое в виде одноимённых pickle файлов.
import os
import json
import pickle

ext = "json"


def json_to_pickle(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            origin_name, origin_ext = os.path.join(file).split(".")
            if origin_ext == ext:
                with open(file, 'r', encoding='utf-8') as f:
                    my_dict = json.load(f)
                    origin_name = origin_name + '.pickle'
                    with open(origin_name, 'wb') as f2:
                        pickle.dump(my_dict, f2)


json_to_pickle(os.path.join(os.getcwd()))

# new_dict = {
#   "id": 2,
#   "name": "Ervin Howell",
# "username": "Antonette",
#   "email": [
#     "Shanna@melissa.tv",
#     "antonette@howel.com"
#   ],
#   "address": {
#     "street": "Victor Plains",
#     "suite": "Suite 879",
#     "city": "Wisokyburgh",
#     "zipcode": "90566-7771",
#     "geo": {
#       "lat": "-43.9509",
#       "lng": "-34.4618"
#     }
#   },
#   "phone": "010-692-6593 x09125",
#   "website": "anastasia.net",
#   "company": {
#     "name": "Deckow-Crist",
#     "catchPhrase": "Proactive didactic contingency",
#     "bs": "synergize scalable supply-chains"
# } }
# with open('new_file.json', 'w', encoding='utf-8') as f:
#     json.dump(new_dict, f, indent=4)