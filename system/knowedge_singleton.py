import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.knowedge import Knowedge
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager

class SystemLogSingleton(object):

    _knowedge = None
    _mutex = Lock()

    def get_instance(self):
            
        if type(self)._knowedge is None:

            BaseManager.register('Knowedge', Knowedge)
            manager = BaseManager()
            manager.start()

            type(self)._knowedge = manager.Knowedge()

        return type(self)._knowedge
