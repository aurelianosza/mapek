import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from system.system_log_singleton import SystemLogSingleton as SystemLog
from system.system_state_singleton import SystemStateSingleton as SystemState
from analyzer.symptom_manager import SymptomManager
class Analyser(Observer):

    def __init__(self):
        Observer.__init__(self)
        self._system_state = SystemState().get_instance()
        self._symptom_manager = SymptomManager()


    def create_symptom(self, name, symptom, data):
        self._symptom_manager.add_symptom(name, symptom, data)

    def update(self):
        symptoms = self._symptom_manager.verify()

        for i in symptoms:
            print(i._name)



