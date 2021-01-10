from abc import ABC, abstractmethod

class Listener(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def listen(self, data):
        raise Exception('Not implemented update method')
