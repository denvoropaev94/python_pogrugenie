# a. Написать программу, которая будет выводить в консоль ёлочку заданной высоты
number = int(input("Задайте высоту для елочки: "))
for i in range(1, number*2, 2):
    print(number * " " + i * "*")
    number -= 1