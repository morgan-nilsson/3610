from abc import ABC
from abc import abstractmethod

from Burger import Burger
from Burger import VegBurger
from Burger import NonVegBurger

from Pizza import Pizza
from Pizza import VegPizza
from Pizza import NonVegPizza

from Noodles_cutlet import Noodles
from Noodles_cutlet import VegNoodles
from Noodles_cutlet import NonVegNoodles

from Noodles_cutlet import Cutlet
from Noodles_cutlet import NonVegCutlet



class ProductFactory(ABC):
    @abstractmethod
    def create_burger(self, price: int, calories: int, description: str) -> Burger:
        pass
    @abstractmethod
    def create_pizza(self, price: int, calories: int, description: str, size: str) -> Pizza:
        pass
    @abstractmethod
    def create_noodles(self, price: int, calories: int, description: str) -> Noodles:
        pass

    @abstractmethod
    def create_cutlet(self, price: int, calories: int, description: str) -> Cutlet:
        pass



class VegProductFactory(ProductFactory):
    def create_burger(self, price: int, calories: int, description: str) -> Burger:
        return VegBurger(price, calories, description)

    def create_pizza(self, price: int, calories: int, description: str, size: str) -> Pizza:
        return VegPizza(price, calories, description, size)

    def create_noodles(self, price: int, calories: int, description: str) -> Noodles:
        return VegNoodles(price, calories, description)

    def create_cutlet(self, price: int, calories: int, description: str) -> Cutlet:
        raise ValueError("No such thing as veg cutlet")

class NonVegProductFactory(ProductFactory):
    def create_burger(self, price: int, calories: int, description: str) -> Burger:
        return NonVegBurger(price, calories, description)

    def create_pizza(self, price: int, calories: int, description: str, size: str) -> Pizza:
        return NonVegPizza(price, calories, description, size)

    def create_noodles(self, price: int, calories: int, description: str) -> Noodles:
        return NonVegNoodles(price, calories, description)

    def create_cutlet(self, price: int, calories: int, description: str) -> Cutlet:
        return NonVegCutlet(price, calories, description)