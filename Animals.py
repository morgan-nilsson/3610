from IAnimal import Animal
from enum import Enum

class Lion(Animal):
    def say_something(self) -> str:
        return "Roar"

class Elephant(Animal):
    def say_something(self) -> str:
        return "trumpet"
    
class Penguin(Animal):
    def say_something(self) -> str:
        return "I am a Penguin"

class WhiteBear(Animal):
    def say_something(self) -> str:
        return "I am a white bear"

class GrizzlyBear(Animal):
    def say_something(self) -> str:
        return "I am a grizzly bear"

class Moose(Animal):
    def say_something(self) -> str:
        return "I am a moose"

class AnimalFactory():
    @staticmethod
    def create_animal(animal_number: AnimalNumbers) -> Animal:
        match(animal_number):
            case AnimalNumbers.LION:
                return Lion()
            case AnimalNumbers.ELEPHANT:
                return Elephant()
            case AnimalNumbers.PENGUIN:
                return Penguin()
            case AnimalNumbers.WHITE_BEAR:
                return WhiteBear()
            case AnimalNumbers.GRIZZlY_BEAR:
                return GrizzlyBear()
            case AnimalNumbers.MOOSE:
                return Moose()
            case _:
                raise ValueError

class AnimalNumbers(Enum):
    LION = 1
    ELEPHANT = 2
    PENGUIN = 3
    WHITE_BEAR = 4
    GRIZZlY_BEAR = 5
    MOOSE = 6
