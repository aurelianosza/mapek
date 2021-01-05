import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from monitor.monitor import Monitor
from monitor.sensor import interval_sensor
from interfaces.strategy import Strategy
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
from random import randint
from exceptions.read_value_exception import ReadValueException
from monitor.treshold.treshold import Treshold
from datetime import datetime
from system.system_log_singleton import SystemLogSingleton as SystemLog
from monitor.data_interceptor import DataInterceptor
from multiprocessing.managers import BaseManager
from controllers.base_controller import BaseController
from analyzer.analyzer import Analyser
from analyzer.symptom import Symptom
from system.system_state_singleton import SystemStateSingleton as SystemState

class SocketStrategy(Strategy):

    def __init__(self, addr, port):
        Strategy.__init__(self)
        self._addr = addr

    def execute(self):
        return randint(20, 240)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self._addr)
        data = sock.recv(1024)
        sock.close()
        return int(data.decode())

class LimitSymptom(Symptom):

    def __init__(self, name, manager, data):

        Symptom.__init__(self, name, manager)

        self.limit =  data['limit']
        self.property = data['property']

        state = SystemState()

        self.system_state = state.get_instance()

    def handle(self):
        aux = self.system_state.get_property(self.property)
        return aux and int(aux['value']) > int(self.limit)



class MonitorController(BaseController):

    def __init__(self):
        self.monitor = Monitor()
        self.analyzer = Analyser()

        self.monitor.attach(self.analyzer)

    def start(self):
        self._sensors = {
            "socket" : SocketStrategy
        }

        self.analyzer.create_symptom('limit_temperatura', LimitSymptom, {'limit': 50, 'property': 'temperatura'})
        self.analyzer.create_symptom('limit_pressao', LimitSymptom, {'limit': 75, 'property': 'pressao'})

        data = [
            {
                "sensor": 'socket:127.0.0.1,7666',
                "limits": '0,160',
                "interval": 30,
                "property": 'pressao'
            },
            {
                "sensor": 'socket:127.0.0.1,8666',
                "limits": '0,160',
                "interval": 30,
                "property": 'temperatura'
            },
        ]

        self._load_sensors(self.monitor, data)

        while True:
            pass


if __name__ == '__main__':

    s = SystemLog().get_instance()

    controller = MonitorController()
    controller.start()


