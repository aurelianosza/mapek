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
