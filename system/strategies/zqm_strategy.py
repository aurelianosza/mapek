import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.listener import Listener
from json import dumps
import zmq

class ZmqStrategy(Listener):

    def __init__(self):
        Listener.__init__(self)
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.PUB)
        self._socket.bind('tcp://127.0.0.1:9888')

    def listen(self, data):
        self._socket.send(dumps(data).encode())


if __name__ == '__main__':

    from interfaces.publisher import Publisher

    class SomePublisher(Publisher):

        def __init__(self):
            Publisher.__init__(self)
            self._data = 0

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data):
            self._data = data
            self.publish(self.data)

    from time import sleep
    from random import randint

    aux = ZmqStrategy()

    publisher = SomePublisher()
    publisher.add_listener(aux)

    while True:
        publisher.data = '{}'.format(randint(0, 500))
        sleep(2)


    