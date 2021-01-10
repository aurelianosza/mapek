import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.listener import Listener

class Knowledge(Listener):

    def __init__(self, creator, reader, updater, deletor):
        self.creator = creator
        self.reader = reader
        self.updater = updater
        self.deletor = deletor

    def listen(self, data):
        print(data)
        
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
    
    from system.strategies.knowledge_creator_strategy import KnowledgeCreatorStrategy
    from system.strategies.knowledge_reader_strategy import KnowledgeReaderStrategy
    from system.strategies.knowledge_updater_strategy import KnowledgeUpdaterStrategy
    from system.strategies.knowledge_deletor_strategy import KnowledgeDeletorStrategy

    k = Knowledge(KnowledgeCreatorStrategy(), KnowledgeReaderStrategy(), KnowledgeUpdaterStrategy(), KnowledgeDeletorStrategy())

    k.create({"flow": 'podcast'})
    print('{}'.format(k.read('flow')))
    k.delete('flow')

    
     