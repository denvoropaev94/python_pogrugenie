# Вывести случайное число в диапазоне от 1 до 100 включительно
import random as rnd
from sys import argv


# # num = random.randint(1,100)
# # print(num)
# print(random.uniform(int(argv[1]), int(argv [2])))
# print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
# print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))

def guess(tries=3,end=10 ,start=1 ):
    random_number = rnd.randint(start, end)

    while tries:
        answer = int(input("Какое число загадано? "))
        if answer == random_number:
            print("вы угадали!")
            break
        else:
            if answer > random_number:
                print("Попробуйте взять меньше")
            else:
                print("Попробуйте взять больше")
        tries -= 1

    else:
        print("Вы не угадали(")
        print("Было загадано ", random_number)


if __name__ == "__main__":
    guess(1, 100, 3)
