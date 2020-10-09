from multiprocessing import Process
from sensor import Sensor

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



if __name__ == "__main__":
    
    import path
    import sys

    folder = path.Path(__file__).abspath()
    sys.path.append(folder.parent.parent.parent)

    from interfaces.strategy import Strategy
    from socket import socket, AF_INET, SOCK_STREAM
    from interfaces.observer import Observer

    class TemperaturaPassiveStrategy(Strategy):

        def __init__(self, addr):
            self._sock = socket(AF_INET, SOCK_STREAM)
            self._sock.connect(addr)

        def execute(self):
            value = self._sock.recv(1024)
            return int(value.decode())

    class BasicInterface(Observer):

        def __init__(self):
            Observer.__init__(self)

        def update(self, subject):
            print("{} send a new value :\t {}".format(subject.name, subject.value))

    b = BasicInterface()

    s = PassiveSensor('Pressao', TemperaturaPassiveStrategy(('127.0.0.1', 7555)))

    s.attach(b)

    s.start()

    s.join()
