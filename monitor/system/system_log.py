import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.observer import Observer

class SystemLog(Observer):

    def __init__(self):
        Observer.__init__(self)
        self._recorders = {}

    def update(self, subject):
        for key, value in self._recorders.items()
            value.execute(subject)

