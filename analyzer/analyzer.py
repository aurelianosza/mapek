import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from analyzer.symptom_manager import SymptomManager
from analyzer.analyzer_publisher import AnalyzerPublisher
from analyzer.adaptation_request import AdaptationRequest
class Analyser(Observer):

    def __init__(self):
        Observer.__init__(self)
        self._system_state = SystemState().get_instance()
        self._symptom_manager = SymptomManager()
        self._publisher = AnalyzerPublisher()


    def create_symptom(self, name, symptom, data):
        self._symptom_manager.add_symptom(symptom, name, data)

    def add_listener(self, name, register):
        self._publisher.subscribe(name, register)

    def update(self, subject):
        symptoms = self._symptom_manager.verify()

        self._publisher.publisher(AdaptationRequest(symptoms))



