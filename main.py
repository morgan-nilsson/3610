from FoodApp import FoodApp

food_app = FoodApp()

order = food_app.makeOrder(["veg burger", "non_veg pizza", "veg noodles"])
print(food_app.getOrderDescription(order))