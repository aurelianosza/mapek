import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.subject import Subject
from interfaces.publisher import Publisher
from interfaces.listener import Listener
from system.system_log_singleton import SystemLogSingleton as SystemLog
from system.knowedge_singleton import KnowedgeSingleton as Knowedge
from multiprocessing.managers import BaseManager
from system.strategies.zqm_strategy import ZmqStrategy
from json import dumps

class Monitor(Subject, Publisher, Listener):

    def __init__(self):
        Subject.__init__(self)
        Publisher.__init__(self)
        Listener.__init__(self)

        self._interceptors = {}

    def add_interceptor(self, name, interceptor):
        interceptor.monitor = self
        self._interceptors[name] = interceptor

    def remove_interceptor(self, name):
        self._interceptors.pop(name)

    def listen(self, property, value):
        print("Receive value {} from {}.".format(value, property))
        self._publisher.execute(dumps({property:value}))
        self.notify()


