import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from system.symptom_manager import SymptomManager
from interfaces.publisher import Publisher
from analyzer.adaptation_request import AdaptationRequest
class Analyser(Observer, Publisher):

    def __init__(self):
        Observer.__init__(self)
        Publisher.__init__(self)
        
        self._symptom_manager = SymptomManager()

    def add_symptom(self, name, symptom, data):
        self._symptom_manager.add_symptom(symptom, name, data)

    def update(self, subject):

        symptoms = list(self._symptom_manager.verify())

        if len(symptoms) == 0:
            return

        self.publish(AdaptationRequest(symptoms))
