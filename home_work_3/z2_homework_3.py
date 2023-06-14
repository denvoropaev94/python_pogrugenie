# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
my_list = [11, 12.34, True, "HELLLO", 77, False, "Mine", False, 11, 12.34, "Mine", 34, 12, 11]

def list_with_duplicate_elements(input_list):
    result = []
    for i in my_list:
        if my_list.count(i) > 1:
            result.append(i)
    return set(result)


print(list_with_duplicate_elements(my_list))