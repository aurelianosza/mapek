import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.listener import Listener
from multiprocessing import Lock
class Knowledge(Listener):

    def __init__(self, creator, reader, updater, deletor):
        self._lock = Lock()

        self.creator = creator
        self.reader = reader
        self.updater = updater
        self.deletor = deletor

    def listen(self, data):
        self.create(data)
        
    def create(self, data):
        if self.creator is None:
            return
        with self._lock:
            self.creator.execute(data)

    def read(self, data):
        if data is None:
            return None
        with self._lock:
            return self.reader.execute(data)

    def update(self, data):
        if data is None:
            return None
        with self._lock:
            self.updater.execute(data)

    def delete(self, data):
        if data is None:
            return None
        with self._lock:
            self.deletor.execute(data)
