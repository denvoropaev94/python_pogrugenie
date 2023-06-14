# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность.

items = {'Палатка': 5.0,
         'Cпальник': 10.0,
         'Колонка': 6.0,
         'Ролтон': 1.0,
         'Вода': 5.0,
         'Дрова': 7.5,
         'Кружка': 1.0,
         'Аккумулятор': 20.0,
         'Нож': 1.0}


def maximum_load_capacity(things: dict[str, float], capacity: int):
    backpack = [[], 0]
    for item, weight in things.items():
        if backpack[1] + weight <= capacity:
            backpack[0].append(item)
            backpack[1] += weight
        else:
            break
    return backpack


print(maximum_load_capacity(items, 30))