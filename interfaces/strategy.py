from abc import ABC, abstractmethod

class Strategy(ABC):

    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def execute(self):
        raise Exception("Method not implemented")
