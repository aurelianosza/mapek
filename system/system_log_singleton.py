import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.system_log import SystemLog
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager

class SystemLogSingleton(object):

    _system_log = None
    _mutex = Lock()

    def get_instance(self):
            
        if type(self)._system_log is None:

            BaseManager.register('SystemLog', SystemLog)
            manager = BaseManager()
            manager.start()

            type(self)._system_log = manager.SystemLog()

        return type(self)._system_log
