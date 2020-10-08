from sensor import Sensor
from multiprocessing import Process
from time import sleep

class IntervalSensor(Sensor):
    
    def __init__(self, name, strategy, interval):
        Sensor.__init__(self, name, strategy)

        self._interval = interval
        self._process = None

    def start(self):
        self._process = Process(target=self.execute)
        self._process.start()

    def join(self):
        self._process.join()

    def execute(self):
        while True:
            sleep(self._interval)
            super(IntervalSensor, self).execute()
