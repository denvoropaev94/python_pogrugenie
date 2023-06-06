# 4. Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

low = 0
high = 1000
while True:
    current = (low+high)//2
    is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
    if is_right.lower() == 'да':
        print('Я его угадал!')
        break
    elif is_right == 'больше':
        low = current + 1
    else:
        high = current - 1