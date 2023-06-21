# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def Fibonacci_generate(input_number):
    if input_number == 1:
        yield 1
    elif input_number == 2:
        yield 1
    else:
        yield next(iter(Fibonacci_generate(input_number - 1))) + next(
            iter(Fibonacci_generate(input_number - 2)))


number = 15
for i in range(1, number + 1):
    print(next(iter(Fibonacci_generate(i))))
