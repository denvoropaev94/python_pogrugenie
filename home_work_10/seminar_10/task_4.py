# Задание No4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
import random


class Person:

    def __init__(self, first_name, second_name, phone, age):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.first_name} {self.second_name}'

    def have_age(self):
        return self._age


class Worker(Person):
    def __init__(self, *args, **kwargs):
        self.id = random.randint(100_000, 999_999)
        super().__init__(*args, **kwargs)

    @property  # Защита от изменений, делает из метода атрибут
    def accses_level(self):
        str_id = str(self.id)
        list_id_numbers = sum(list(map(int, str_id)))
        return list_id_numbers % 7


sotr1 = Worker("Nik", "Bondarenko", 213214, 29)
print(f'{sotr1.id = }, {sotr1.accses_level= }')
