from abc import abstractmethod

class IProduct():
    @abstractmethod
    def get_price(self) -> int:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass