import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.subject import Subject
from system.system_log_singleton import SystemLogSingleton as SystemLog
from system.system_state_singleton import SystemStateSingleton as SystemState

class Monitor(Subject):

    def __init__(self):
        Subject.__init__(self)

        log = SystemLog()
        state = SystemState()

        self._system_log = log.get_instance()
        self._system_state = state.get_instance()
        self._interceptors = {}

    def add_interceptor(self, name, interceptor):
        interceptor.monitor = self
        self._interceptors[name] = interceptor

    def remove_interceptor(self, name):
        self._interceptors.pop(name)

    def listen(self, property, value):
        print("Receive value {} from {}.".format(value, property))
        self._system_state.set_property(property, value)
        self.notify()


