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


if __name__ == '__main__':
    
    from system.strategies.knowledge_creator_strategy import KnowledgeCreatorStrategy
    from system.strategies.knowledge_reader_strategy import KnowledgeReaderStrategy
    from system.strategies.knowledge_updater_strategy import KnowledgeUpdaterStrategy
    from system.strategies.knowledge_deletor_strategy import KnowledgeDeletorStrategy
    from interfaces.publisher import Publisher

    class SomePublisher(Publisher):

        def __init__(self):
            Publisher.__init__(self)
            self.data = 0

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data):
            self._data = data
            self.publish(self.data)


    k = Knowledge(KnowledgeCreatorStrategy(), KnowledgeReaderStrategy(), KnowledgeUpdaterStrategy(), KnowledgeDeletorStrategy())

    s = SomePublisher()

    s.add_listener(k)
    s.data = {'pressao': 200}

    
     