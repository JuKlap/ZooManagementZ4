class Zoo:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Zoo, cls).__new__(cls)
            cls._instance.animals = []
            cls._instance.observers = []
        return cls._instance
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def remove_animal(self, animal):
        self.animals.remove(animal)

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()
