class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return (f'{"Type:":}{type(self).__name__}'
                f'\n{"Name:":}{self.name}'
                f'\n{"Age:":}{self.age} years')


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str, voice: str):
        super().__init__(name, age)
        self.breed = breed
        self.voice = voice

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Breed:":}{self.breed}'
                f'\n{"Voice:":}{self.voice}'
                )


class Bird(Animal):

    def __init__(self, name: str, age: int, breed: str, voice: str, colour: str):
        super().__init__(name, age)
        self.breed = breed
        self.voice = voice
        self.colour = colour

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Breed:":}{self.breed}'
                f'\n{"Voice:":}{self.voice}'
                f'\n{"Colour:":}{self.colour}'
                )


class Fish(Animal):

    def __init__(self, name: str, age: int, breed: str, count_of_fins: int):
        super().__init__(name, age)
        self.breed = breed
        self.count_of_fins = count_of_fins

    def get_info(self) -> str:
        return (super().get_info() +
                f'\n{"Breed:":}{self.breed}'
                f'\n{"Count of fins:":}{self.count_of_fins}'
                )


#
# dog = Dog("Rex", 5, "овчарка", "Гав")
# print(dog.get_info())
# print("-------------------------------")
# ptichka = Bird("Kesha", 10, "Попугай", "яяяя самый умный!", "золотисто-синий")
# print(ptichka.get_info())
# print("-------------------------------")
# fish = Fish("Золотая рыбка", 100, "золотоголовка", 9)
# print(fish.get_info())


class AnimalFabric:
    parameters = {}

    @classmethod
    def create(cls, animal_type: str,
              name: str, age: int,
              breed: str = None,
              voice: str = None,
              colour: str = None,
              count_of_fins: int = None
              ) -> Animal:
        cls.parameters = dict(name=name, age=age,
                              breed=breed,
                              voice=voice,
                              colour=colour,
                              count_of_fins=count_of_fins)
        return cls.choice_type(animal_type)

    @classmethod
    def choice_type(cls, animal_type):
        match animal_type:
            case 'Dog':
                return cls.create_dog(**cls.parameters)
            case 'Bird':
                return cls.create_bird(**cls.parameters)
            case 'Fish':
                return cls.create_fish(**cls.parameters)
            case _:
                return Animal('Hulk', 777)

    @classmethod
    def create_dog(cls, name, age, breed, voice, **_) -> Dog:
        return Dog(name=name, age=age, breed=breed, voice=voice)

    @classmethod
    def create_bird(cls, name, age, breed, voice, colour, **_) -> Bird:
        return Bird(name=name, age=age, breed=breed, voice=voice, colour=colour)

    @classmethod
    def create_fish(cls, name, age, breed, count_of_fins, **_) -> Fish:
        return Fish(name=name, age=age, breed=breed, count_of_fins=count_of_fins)


dog = AnimalFabric.create(animal_type='Dog', name='Rex', age=7, breed='shepherd dog', voice='Гаав!')
fish = AnimalFabric.create(animal_type='Fish', name='Nemo', age=3, breed='gold', count_of_fins=9)
bird = AnimalFabric.create(animal_type='Bird', name='Zina', age=88, breed='Chaika', voice='Скриии', colour='White', )
unidentified = AnimalFabric.create(animal_type='Non-type', name='Test', age=100, breed="HZ", voice='Au', colour='Blue')
print(dog.get_info(), '\n')
print(bird.get_info(), '\n')
print(fish.get_info(), '\n')
print(unidentified.get_info())
