from abc import abstractmethod

class Observer:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self, subject) -> None:
        pass