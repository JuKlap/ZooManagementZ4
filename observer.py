from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def updateOfFeeding(self):
        pass