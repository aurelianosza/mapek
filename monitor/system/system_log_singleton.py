from system_log import SystemLog
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager

class SystemLogSingleton(object):

    _system_log = None
    _mutex = Lock()

    def get_instance(self):
            
        if type(self)._system_state is None:

            BaseManager.register('SystemLog', SystemLog)
            manager = BaseManager()
            manager.start()

            type(self)._system_state = manager.SystemLog()

        with type(self)._mutex:
            return type(self)._system_log
