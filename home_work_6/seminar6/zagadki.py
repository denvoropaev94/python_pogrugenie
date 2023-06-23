# zagadka = ' '
# list_otvetov = []
# count = 5
def zagad(zagadka: str, list_otvetov: list, count: int = 3):
    print(f'Загадка - {zagadka}')
    popitka = 1
    while count:
        user_answer = input("Ваш ответ: ").lower()
        if user_answer in list_otvetov:
            return f"Вы угадали с {popitka} попытки/попыток"

        else:
            print("Попробуйте еще раз")
            popitka += 1
            count -= 1
    return f"Вы не угадали"


def puzzle():
    puzzles = {'Зимой и летом одним цветом?': ['елка', 'ель', 'ёлка'],
               'Висит груша - нельзя скушать ': ['лампочка', 'лампа'],
               'Не лает, не кусает, а в дом не пускает ': ['замок', 'замочек']
               }

    for puzzle, answer in puzzles.items():
        func_info(puzzle, zagad(puzzle, answer))

    print(_my_dict)


# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число # (номер попытки, з которой она угадана)
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в # удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение
_my_dict = {}


def func_info(text: str, number: int):
    _my_dict[text] = number

