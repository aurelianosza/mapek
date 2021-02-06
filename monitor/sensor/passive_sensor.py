import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from monitor.sensor.sensor import Sensor
from multiprocessing import Process


class PassiveSensor(Sensor):

    def __init__(self, name, strategy):
        Sensor.__init__(self, name, strategy)

        self._process = None

    def start(self):
        self._process = Process(target=self.execute)
        self._process.start()

    def join(self):
        self._process.join()

    def execute(self):
        while True:
            Sensor.execute(self)
