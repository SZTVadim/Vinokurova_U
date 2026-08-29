from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


class Zoo:
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.__animals = []

    def add_animals(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals


# полиморфизм потому, что метод make_sound при вызовах
# будет вести себя неодинаково в зависимости от объекта
def animal_sound(animal):
    return animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)
zoo = Zoo("Городской зоопарк")

for animal in [dog1, dog2, cat1]:
    zoo.add_animals(animal)

print(zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# Python не дает создавать объект, тк класс абстрактный
# с абстрактным методом make_sound.
# Можно только через наследников
animal_1 = Animal()
