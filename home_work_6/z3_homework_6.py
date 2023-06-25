import random


# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
def queen_attack(input_data: str, size: int):
    x = []
    y = []
    my_list = list(map(int, input_data.split(",")))
    for i in range(len(my_list)):
        if i % 2 == 0:
            x.append(my_list[i])
        else:
            y.append(my_list[i])

    correct = True
    for i in range(size):
        for j in range(i + 1, size):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        print('Ферзи не бьют друг друга! ')
    else:
        print('Ферзи бьют друг друга! ')


# queen_attack("0,3,1,5,2,7,3,1,4,6,5,0,6,2,7,4", 8)

def queen_sample():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    count = 0
    new_string = ""
    axe_x = random.sample(numbers, 8)
    axe_y = random.sample(numbers, 8)
    print(axe_y)
    print(axe_x)
    for x in axe_x:
        new_string += str(x) + ","
    for y in axe_y:
        new_string += str(y) + ","
    new_string = new_string[:-1]

    while count < 4:
        if not queen_attack(new_string, 8):
            count += 1
            print("Координаты:  ", new_string)


queen_sample()

# queen_attack(new_string, 8)
