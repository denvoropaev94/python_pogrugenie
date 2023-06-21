# ✔Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def bonus_count(names, stavka, procent):
    parsed_bonus_rates = [float(i.split("%")[0]) for i in procent]
    bonuses = list(map(lambda x,y: (x * y)/100 + x, stavka, parsed_bonus_rates))
    return {names[i]: bonuses[i] for i in range(len(names))}


names = ["Денис", "Никита", "Олег"]
stavka = [100_000, 50_000, 10_000]
procent = ["10.25%", "4.25%", "0.15%"]
#
print(bonus_count(names, stavka, procent))
