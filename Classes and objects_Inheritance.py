class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением")

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением")

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)

Padaroshnic = Flower("Подарожник")
apple = Fruit("Яблоко")

lion = Predator("Лев")
deer = Mammal("Олень")

lion.eat(Padaroshnic)
deer.eat(apple)

print(f"{lion.name} жив: {lion.alive}, накормлен: {lion.fed}")
print(f"{deer.name} жив: {deer.alive}, накормлен: {deer.fed}")
