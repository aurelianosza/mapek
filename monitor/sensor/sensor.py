import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.subject import Subject 
from multiprocessing import Process, Value, Lock
from ctypes import c_void_p
from time import sleep

class Sensor(Subject):

    def __init__(self, name, strategy):
        Subject.__init__(self)

        self.name = name
        self._strategy = strategy

        self._value = Value(c_void_p, None)
        self._mutex = Lock()

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


if __name__ == '__main__':

    from interfaces.strategy import Strategy
    from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
    from interfaces.observer import Observer
    from interval_sensor import IntervalSensor
    from passive_sensor import PassiveSensor
    from random import randint

    class TemperaturaStrategy(Strategy):

        def __init__(self, addr):
            super(TemperaturaStrategy, self).__init__()
            self._addr = addr

        def execute(self):
            return randint(1, 99)
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(self._addr)
            data = sock.recv(1024)
            sock.close()
            return int(data.decode())

    class PressaoStrategy(Strategy):
    
        def __init__(self, addr):
            self._sock = socket(AF_INET, SOCK_STREAM)
            # self._sock.connect(addr)

        def execute(self):
            sleep(randint(1, 200))
            return randint(1, 60)
            value = self._sock.recv(1024)
            return int(value.decode())


    class BasicInterface(Observer):

        def __init__(self):
            super(BasicInterface, self).__init__()

        def update(self, subject):
            print("{} send a new value :\t {}".format(subject.name, subject.value))

    b = BasicInterface()

    s1 = IntervalSensor('Temperatura', TemperaturaStrategy(('127.0.0.1', 8666)), 20)
    s2 = PassiveSensor('Pressao', PressaoStrategy(('127.0.0.1', 7555)))

    s1.attach(b)
    s2.attach(b)

    s1.start()
    s2.start()

    s2.join()
    s1.join()

        

    



        




    

    





    

