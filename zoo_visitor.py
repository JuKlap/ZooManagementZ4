from observer import Observer

class ZooVisitor(Observer):
    def __init__(self, name):
        self.name = name

    def updateOfFeeding(self):
        print(f"{self.name} feeding of animals are happening now")
