import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.knowledge import Knowledge
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager
from system.strategies.knowledge_creator_strategy import KnowledgeCreatorStrategy
from system.strategies.knowledge_deletor_strategy import KnowledgeDeletorStrategy
from system.strategies.knowledge_reader_strategy import KnowledgeReaderStrategy
from system.strategies.knowledge_updater_strategy import KnowledgeUpdaterStrategy

class KnowledgeSingleton(object):

    _knowledge = None
    _mutex = Lock()

    def get_instance(self):
            
        if type(self)._knowledge is None:

            BaseManager.register('Knowledge', Knowledge)
            manager = BaseManager()
            manager.start()

            type(self)._knowledge = manager.Knowledge(KnowledgeCreatorStrategy(), KnowledgeReaderStrategy(), KnowledgeUpdaterStrategy(), KnowledgeDeletorStrategy())
        
        with type(self)._mutex:
            return type(self)._knowledge
