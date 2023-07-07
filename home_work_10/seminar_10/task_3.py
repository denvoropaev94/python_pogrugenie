# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


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

person1 = Person('Den','Voropaev',777,28)
print(person1.full_name())
print(person1.have_age())
person1.birthday()
print(person1.have_age())
