from IProduct import IProduct

class Pizza(IProduct):
    def __init__(self) -> None:
        super().__init__()
        self.price = 0
        self.calories = 0
        self.description = ""
        self.size = "Small"

    def get_description(self) -> str:
        return self.description
    
    def get_price(self) -> int:
        return self.price

class VegPizza(Pizza):
    def __init__(self, price: int, calories: int, description: str, size: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description
        self.size = size

    def showVegBurgerAdvert(self) -> str:
        return "This is a veg pizza buy it"

class NonVegPizza(Pizza):
    def __init__(self, price: int, calories: int, description: str, size: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description
        self.size = size