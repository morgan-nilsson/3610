from IProduct import IProduct

class Noodles(IProduct):
    def __init__(self) -> None:
        super().__init__()
        self.price = 0
        self.calories = 0
        self.description = ""

    def get_description(self) -> str:
        return self.description
    
    def get_price(self) -> int:
        return self.price

class VegNoodles(Noodles):
    def __init__(self, price: int, calories: int, description: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description

    def showVegBurgerAdvert(self) -> str:
        return "This is a veg pizza buy it"

class NonVegNoodles(Noodles):
    def __init__(self, price: int, calories: int, description: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description

class Cutlet(IProduct):
    def __init__(self) -> None:
        super().__init__()
        self.price = 0
        self.calories = 0
        self.description = ""

    def get_description(self) -> str:
        return self.description
    
    def get_price(self) -> int:
        return self.price

class NonVegCutlet(Cutlet):
    def __init__(self, price: int, calories: int, description: str) -> None:
        super().__init__()
        self.price = price
        self.calories = calories
        self.description = description