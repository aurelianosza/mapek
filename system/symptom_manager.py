import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.knowledge_singleton import KnowledgeSingleton
from multiprocessing import Manager

class SymptomManager(object):

    def __init__(self):
        knowledge_accessor = KnowledgeSingleton()

        self._knowledge = knowledge_accessor.get_instance()
        manager = Manager()
        self._symptoms = manager.dict()

    def verify(self):

        symptoms = filter(lambda symptom: symptom.handle(), self._symptoms.values())

        return symptoms

    def add_symptom(self, symptom, name, data):
        self._symptoms[name] = symptom(name, self, data)
