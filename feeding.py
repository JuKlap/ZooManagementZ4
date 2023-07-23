from abc import ABC, abstractmethod

class Feeding(ABC):
    @abstractmethod
    def feed(self, animal):
        pass

class HerbivoreFeeding(Feeding):
    def __init__(self):
        pass
    
    def feed(self, animal):
        return(f"{animal.__class__.__name__} eats vegetarian food")

class CarnivoreFeeding(Feeding):
    def __init__(self):
        pass

    def feed(self, animal):
        return (f"{animal.__class__.__name__} eats meat")
