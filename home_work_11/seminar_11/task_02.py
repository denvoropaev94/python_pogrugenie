# Задание No2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
# list-архивы также являются свойствами экземпляра

class Arhive:
    """Архив, который хранит пару свойств. Например, число и строку"""
    _instance = None
    arhive_list = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance:
            cls.arhive_list.append(cls._instance)
        cls._instance = instance
        instance.arhive_list = cls.arhive_list
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'

player1 = Arhive('Den', 28)
print(player1)
print(player1.arhive_list)
player2 = Arhive('Nik', 29)
print(player2)
print(player2.arhive_list)
player3 = Arhive('Sasha', 24)
print(player3)
print(player3.arhive_list)
player4 = Arhive('Serega', 36)
print(player4)
print(player4.arhive_list)
player5 = Arhive('Oleg', 35)
print(player5)
print(player5.arhive_list)
player6 = Arhive('Gleb', 37)
print(player6)
print(player6.arhive_list)