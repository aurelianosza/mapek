import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from interfaces.subject import Subject
from system.system_log_singleton import SystemLogSingleton as SystemLog
from system.system_state_singleton import SystemStateSingleton as SystemState

class Monitor(Observer, Subject):

    def __init__(self):
        Observer.__init__(self)
        Subject.__init__(self)

        log = SystemLog()
        state = SystemState()

        self._system_log = log.get_instance()
        self._system_state = state.get_instance()
        self._sensors = {}

    def add_sensor(self, sensor):
        sensor.attach(self)
        self._sensors[sensor.name] = sensor

    def remove_sensor(self, name):
        self._sensors.pop(name)

    def update(self, subject):
        print("Receive value {} from {}.".format(subject.value, subject.name))
        self._system_state.set_property(subject.name, subject.value)
        self.notify()


