from abc import ABC
from abc import abstractmethod

class IZoo(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.animals = []
        self.ourItinerary = ""
        self.name = ""

    @abstractmethod
    def create_animals(self):
        pass

    def start_visit(self):
        print(self.ourItinerary)
