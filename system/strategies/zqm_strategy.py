import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.strategy import Strategy
import zmq

class ZmqStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB)
        self._socket.bind('tcp://127.0.0.1:9888')

    def execute(self, data):
        self._socket.send(data.encode())


if __name__ == '__main__':

    from time import sleep
    from random import randint

    aux = ZmqStrategy()

    while True:
        aux.execute('{}'.format(randint(0, 500)))
        sleep(2)


    