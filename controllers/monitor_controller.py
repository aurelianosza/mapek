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

class MonitorController(BaseController):

    def __init__(self):
        self.monitor = Monitor()


    def start(self):
        self._sensors = {
            "socket" : SocketStrategy
        }

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


