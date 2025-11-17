from IProduct import IProduct

class Burger(IProduct):
    def __init__(self) -> None:
        self.price = 0
        self.calories = 0
        self.description = ""

    def get_description(self) -> str:
        return self.description
    
    def get_price(self) -> int:
        return self.price

class VegBurger(Burger):
    def __init__(self, price: int, calories: int, description: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description

    def showVegBurgerAdvert(self) -> str:
        return "This is a veg burger buy it"

class NonVegBurger(Burger):
    def __init__(self, price: int, calories: int, description: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description