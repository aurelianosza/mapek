import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.listener import Listener
from multiprocessing import Manager

class Planner(Listener):
    
    def __init__(self):
        manager = Manager()
        self._strategies = manager.dict()

    def add_strategy(self, symptoms, strategy):
        self._strategies[self.__generate_symptoms_name(symptoms)] = strategy

    def remove_strategy(self, symptoms):
        self._strategies.pop(symptoms)

    def __generate_symptoms_name(self, data):
        return '|'.join(sorted(data))

    def listen(self, adaptation_request):
        symptoms_name = list(map(lambda symptom: symptom._name, adaptation_request.symptoms))

        data = self._strategies[self.__generate_symptoms_name(symptoms_name)](adaptation_request).execute()

        print(data)
        
