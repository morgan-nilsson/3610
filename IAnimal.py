from abc import abstractmethod
from abc import ABC

class Animal(ABC):
        
    @abstractmethod
    def say_something(self) -> str:
        pass