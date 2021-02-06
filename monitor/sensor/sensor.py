import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.subject import Subject 
from multiprocessing import Process, Value, Lock
from ctypes import c_void_p
from time import sleep
from system.system_log_singleton import SystemLogSingleton as SystemLog
class Sensor(Subject):

    def __init__(self, name, strategy):
        Subject.__init__(self)

        self.name = name
        self._strategy = strategy

        self._value = Value(c_void_p, None)
        self._mutex = Lock()

        self._log = SystemLog().get_instance()  

    @property
    def strategy(self):
        return self._strategy

    @property
    def value(self):
        with self._mutex:
            return self._value.value

    def execute(self):
        with self._mutex:
            self._value.value = self.strategy.execute()
        self.notify()

    def start(self):
        pass
