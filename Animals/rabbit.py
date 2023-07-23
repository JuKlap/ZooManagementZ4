from Animals.animal import Animal

class Rabbit(Animal):
    def __init__(self):
        super().__init__()
        self.feeding = None

    def make_sound(self):
        return "Cyp cyp"

    def eat(self):
        return "A rabbit is a vegetarian"