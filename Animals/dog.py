from Animals.animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.feeding = None
    
    def make_sound(self):
        return "Bark bark"

    def eat(self):
        return "A dog is not a vegetarian"
