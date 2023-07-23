from abc import ABC

class DailyRoutine(ABC):
    def daily_routine(self, animal):
        print(f"{animal.__class__.__name__} wakes up.")
        print(animal.make_sound())
        print(animal.eat())
        print(f"{animal.__class__.__name__} goes to sleep.\n")