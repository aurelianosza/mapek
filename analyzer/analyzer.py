import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from system.system_log_singleton import SystemLogSingleton as SystemLog
from system.system_state_singleton import SystemStateSingleton as SystemState

class Analyser(Observer):

    def __init__(self):
        Observer.__init__(self)
        self._system_state = SystemState().get_instance()


    def update(self, analyzer):
        print("System state {}".format(self._system_state))



