number = int(input("Введите число: "))

def system_hex(num):
    s = ''
    h = '0123456789ABCDEF'

    while num > 0:
        s = h[num % 16] + s
        num = num // 16
    return "0x" + s

print(system_hex(number))
print(hex(number))