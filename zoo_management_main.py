from zoo import Zoo
import Animals.dog as Dog
import Animals.rabbit as Rabbit
from zoo_visitor import ZooVisitor
import feeding
import daily_routine
import animal_iterator

def main():
    zoo_1 = Zoo()

    # Add animals to the zoo
    dog_1 = Dog.Dog()
    rabbit_1 = Rabbit.Rabbit()
    zoo_1.add_animal(dog_1)
    zoo_1.add_animal(rabbit_1)

    # Register zoo visitors as observers
    visitor_1 = ZooVisitor("Hannah")
    visitor_2 = ZooVisitor("Leo")

    zoo_1.register_observer(visitor_1)
    zoo_1.register_observer(visitor_2)

    # Set feeding for animals
    dog_1.feeding = feeding.CarnivoreFeeding()
    rabbit_1.feeding = feeding.HerbivoreFeeding()

    # Routine for animals
    print("Animals routine:")
    routine = daily_routine.DailyRoutine()
    for animal in zoo_1.animals:
        routine.daily_routine(animal)

    # Iterate through the animals in the zoo
    print("\nAnimals in the zoo:")
    for animal in animal_iterator.AnimalIterator(zoo_1.animals):
        print(animal.__class__.__name__)

if __name__ == "__main__":
    main()