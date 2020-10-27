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
class SocketStrategy(Strategy):

    def __init__(self, addr):
        Strategy.__init__(self)
        self._addr = addr

    def execute(self):
        return randint(-20, 240)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self._addr)
        data = sock.recv(1024)
        sock.close()
        return int(data.decode())

class FileStrategy(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)

    def execute(self, message):
        with open('log.txt', 'a') as file:
            file.write("{} Receive {} value\n".format(datetime.now(), message))


class MonitorController(object):

    def __init__(self):
        self.monitor = Monitor()


    def start(self):

        sensorPressao = interval_sensor.IntervalSensor('Pressao', SocketStrategy(('127.0.0.1', 7666)), 10)
        sensorTemperatura = interval_sensor.IntervalSensor('Temperatura', SocketStrategy(('127.0.0.1', 8666)), 10)

        dataInterceptorPressao = DataInterceptor(0, 160)
        dataInterceptorTemperatura = DataInterceptor(0, 160)

        sensorPressao.attach(dataInterceptorPressao)
        sensorTemperatura.attach(dataInterceptorTemperatura)

        self.monitor.add_interceptor('pressao', dataInterceptorPressao)
        self.monitor.add_interceptor('temperatura', dataInterceptorTemperatura)

        sensorPressao.start()
        sleep(5)
        sensorTemperatura.start()

        sensorPressao.join()
        sensorTemperatura.join()

if __name__ == '__main__':

    s = SystemLog().get_instance()

    s.add_recorder('file', FileStrategy())

    
    controller = MonitorController()
    controller.start()


