class AnimalIterator:
    def __init__(self, animals):
        self._animals = animals
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._animals):
            current_animal = self._animals[self._index]
            self._index += 1
            return current_animal
        else:
            raise StopIteration