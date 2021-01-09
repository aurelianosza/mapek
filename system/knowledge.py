import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer

class Knowedge(Observer):

    def __init__(self, creator, reader, updater, deletor):
        self.creator = creator
        self.reader = reader
        self.updater = updater
        self.deletor = deletor

    def update(self, subject):
        

    def create(self, data):
        if self.creator is None:
            return
        self.creator.execute(data)

    def read(self, data):
        if data is None:
            return None
        return self.reader.execute(data)

    def update(self, data):
        if data is None:
            return None
        self.updater.execute(data)

    def delete(self, data):
        if data is None:
            return None
        self.deletor.execute(data)


if __name__ == '__main__':
    
    from system.strategies.knowedge_creator_strategy import KnowedgeCreatorStrategy
    from system.strategies.knowedge_deletor_strategy import KnowedgeDeletorStrategy
    from system.strategies.knowedge_reader_strategy import KnowedgeReaderStrategy

    k = Knowedge()

    k.creator = KnowedgeCreatorStrategy()
    k.deletor = KnowedgeDeletorStrategy()
    k.reader = KnowedgeReaderStrategy()

    k.create({"flow": 'podcast'})
    print('{}'.format(k.read('flow')))
    k.delete('flow')

    
     