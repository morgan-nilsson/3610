from Zoos import CalgaryZoo, TorontoZoo

calgary_zoo = CalgaryZoo()
calgary_zoo.start_visit()
calgary_zoo.create_animals()
for animal in calgary_zoo.animals:
    print(animal.say_something())

toronto_zoo = TorontoZoo()
toronto_zoo.start_visit()
toronto_zoo.create_animals()
for animal in toronto_zoo.animals:
    print(animal.say_something())