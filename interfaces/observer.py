from abc import ABC, abstractmethod

class Observer(ABC):

    def __init__(self):
        pass

    def bind(self, subject):
        self._subject = subject

    def unbind(self):
        self._subject = None

    @property
    def subject(self):
        return self._subject

    @abstractmethod
    def update(self, subject):
        raise Exception('Not implemented update method')
