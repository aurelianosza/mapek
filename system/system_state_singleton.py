import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.system_state import SystemState
from multiprocessing import Value, Lock
from multiprocessing.managers import BaseManager

class SystemStateSingleton(object):

    _system_state = None
    _mutex = Lock()

    def get_instance(self):
        
        if type(self)._system_state is None:

            BaseManager.register('SystemState', SystemState)
            manager = BaseManager()
            manager.start()

            type(self)._system_state = manager.SystemState()

        with type(self)._mutex:
            return type(self)._system_state

if __name__ == '__main__':

    singleton = SystemStateSingleton()

    s1 = singleton.get_instance()

    s1.set_property('temperatura', 50)

    s2 = singleton.get_instance()

    print(s2.get_property('temperatura'))
    