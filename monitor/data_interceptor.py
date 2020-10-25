import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from exceptions.read_value_exception import ReadValueException

class DataInterceptor(Observer):

    def __init__(self, monitor):
        Observer.__init__(self)
        Subject.__init__(self)

    def dispatch(self, property, value):
        self.monitor.listen()



    

    