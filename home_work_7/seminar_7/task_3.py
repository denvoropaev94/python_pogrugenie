# Задание No3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
def something_strange(new_file):
    list_multiplied_numbers = []
    list_names = []
    length_of_first_file = 0
    length_of_second_file = 0
    with (
        open('zadanie_1.txt', 'r', encoding='utf-8') as f1,
        open('new.txt', 'r', encoding='utf-8') as f2,
        open(new_file, 'w', encoding='utf-8') as f3
    ):
        while numbers := f1.readline():
            int_number, float_number = numbers.strip().split("|")
            list_multiplied_numbers.append(int(int_number) * float(float_number))
            length_of_first_file += 1
        while name := f2.readline():
            list_names.append(name[:-1])
            length_of_second_file += 1
        lengths = sorted([length_of_first_file, length_of_second_file])
        for i in range(lengths[0]):
            if list_multiplied_numbers[i] < 0:
                f3.write(list_names[i].lower() + " " + str(abs(list_multiplied_numbers[i])) + "\n")
            else:
                f3.write(list_names[i].upper() + " " + str(round(list_multiplied_numbers[i])) + "\n")
        for i in range(lengths[1] - lengths[0]):
            if list_multiplied_numbers[i] < 0:
                f3.write(list_names[i].lower() + " " + str(abs(list_multiplied_numbers[i])) + "\n")
            else:
                f3.write(list_names[i].upper() + " " + str(round(list_multiplied_numbers[i])) + "\n")


something_strange("appended_file.txt")
