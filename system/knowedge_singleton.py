import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.knowedge import Knowedge
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager
from system.strategies.knowedge_creator_strategy import KnowedgeCreatorStrategy
from system.strategies.knowedge_deletor_strategy import KnowedgeDeletorStrategy
from system.strategies.knowedge_reader_strategy import KnowedgeReaderStrategy
from system.strategies.knowedge_updater_strategy import KnowedgeUpdaterStrategy

class KnowedgeSingleton(object):

    _knowedge = None
    _mutex = Lock()

    def get_instance(self):
            
        if type(self)._knowedge is None:

            BaseManager.register('Knowedge', Knowedge)
            manager = BaseManager()
            manager.start()

            type(self)._knowedge = manager.Knowedge(KnowedgeCreatorStrategy(), KnowedgeReaderStrategy(), KnowedgeUpdaterStrategy(), KnowedgeDeletorStrategy())
        
        with type(self)._mutex:
            return type(self)._knowedge
