from ProductFactory import ProductFactory
from ProductFactory import VegProductFactory
from ProductFactory import NonVegProductFactory
from IProduct import IProduct

class FoodApp:
    def __init__(self) -> None:
        self.availableFood = {"veg": VegProductFactory, "non_veg": NonVegProductFactory}

    def makeOrder(self, product_names: list[str]) -> list[IProduct]:
        prods = []
        for name in product_names:
            activeFactory: ProductFactory = self.availableFood["veg"]
            description_text = "A yummy veg "
            if "non_veg" in name:
                description_text = "A yummy non veg "
                activeFactory = self.availableFood["non_veg"]

            if "burger" in name:
                prods.append(activeFactory.create_burger(activeFactory, 10, 1000, description_text + "burger"))

            elif "pizza" in name:
                prods.append(activeFactory.create_pizza(activeFactory, 10, 1000, description_text + "pizza", "Small"))

            elif "noodles" in name: 
                prods.append(activeFactory.create_noodles(activeFactory, 10, 1000, description_text + "noodles"))

            elif "cutlet" in name:
                prods.append(activeFactory.create_cutlet(activeFactory, 10, 1000, description_text + "cutlet"))

            else:
                raise ValueError("This food is no good")

        return prods

    @staticmethod
    def getOrderDescription(products: list[IProduct]) -> str:
        ret = ""
        for product in products:
            ret += product.get_description() + "\n"

        return ret