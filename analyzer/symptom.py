import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from abc import ABC, abstractmethod

class ExampleSymptom(ABC):

    def __init__(self, name, manager):
        
        self._name = name
        self._manager = manager

    @abstractmethod
    def handle(self):
        pass


     