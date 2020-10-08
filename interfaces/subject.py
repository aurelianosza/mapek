from abc import ABC, abstractmethod

class Subject(ABC):
    
    def __init__(self):
        # var array
        self._observers = [] 

    @property
    def observers(self):
        return self._observers

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
        observer.unbind()

    def notify(self):
        for observer in self._observers:
            observer.update(self)
