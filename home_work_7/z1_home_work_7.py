# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение
import os


def group_rename(want_name,
                 old_file_ext,
                 new_file_ext,
                 first_old_lt,
                 last_old_lt,
                 count_of_numbers=4):
    nm_count = "0" * count_of_numbers
    file_count = 1
    for file in (os.listdir()):
        if os.path.isfile(file):
            origin_name, origin_ext = os.path.join(file).split(".")
            if origin_ext == old_file_ext:
                if file_count < 10 ** count_of_numbers:
                    nm_count = nm_count[:-len(str(file_count))] + str(file_count)
                    final_name = origin_name[first_old_lt - 1:last_old_lt] + want_name + nm_count + "." + new_file_ext
                    os.rename(os.path.join(file), final_name)
                    file_count += 1
                else:
                    print("Нет файлов!")
                    break


group_rename("my_file", "txt", "pdf", 1, 4)
