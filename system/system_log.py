import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class SystemLog(object):

    def __init__(self):
        self._recorders = {}

    def write(self, info):
        for key, value in self._recorders.items():
            value.execute(info)

    def add_recorder(self, name, recorder):
        self._recorders[name] = recorder
