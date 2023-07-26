import argparse


def system_hex(num):
    s = ''
    h = '0123456789ABCDEF'

    while num > 0:
        s = h[num % 16] + s
        num = num // 16
    return "0x" + s


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert to hex')
    parser.add_argument('number', type=int, help='press integer number')
    args = parser.parse_args()
    print(system_hex(args.number))
