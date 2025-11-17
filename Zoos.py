from IZoo import IZoo
from Animals import AnimalFactory
from Animals import AnimalNumbers

class TorontoZoo(IZoo):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Toronto Zoo"
        self.ourItinerary = "Welcome to the Toronto Zoo! Our Itinerary: 1) African Savanna. 2) Tundra Trek"

    def create_animals(self):
        zoo_animal_contents = [AnimalNumbers.LION, AnimalNumbers.ELEPHANT, AnimalNumbers.PENGUIN, AnimalNumbers.WHITE_BEAR]
        for animal_index in zoo_animal_contents:
            self.animals.append(AnimalFactory.create_animal(animal_index))



class CalgaryZoo(IZoo):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Calgary Zoo"
        self.ourItinerary = "Welcome to the Calgary Zoo! Our Itinerary: 1) Penguin Plunge. 2) Wild Canad"

    def create_animals(self):
        zoo_animal_contents = [AnimalNumbers.GRIZZlY_BEAR, AnimalNumbers.MOOSE, AnimalNumbers.PENGUIN]
        for animal_index in zoo_animal_contents:
            self.animals.append(AnimalFactory.create_animal(animal_index))
        