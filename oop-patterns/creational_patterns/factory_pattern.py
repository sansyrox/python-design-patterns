from abc import ABC, abstractclassmethod
from enum import Enum


class AnimalType(Enum):
    Cat = 1
    Dog = 2


class Animal(ABC):
    @abstractclassmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("bruh")


class Dog(Animal):
    def make_sound(self):
        print("dude")


class Factory:
    @staticmethod
    def get_animal_type(animal_type):
        if animal_type == AnimalType.Cat:
            return Cat()
        raise Exception("Type Error: Enter a vaild type")


if __name__ == "__main__":
    print(Factory.get_animal_type(AnimalType.Cat))
