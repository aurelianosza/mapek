import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.listener import Listener

class Executor(Listener):

    def __init__(self):
        Listener.__init__(self)
        self._effectors = {}

    def add_effector(self, name, effector):
        self._effectors[name] = effector

    def remove_effector(self, name):
        self._effectors.pop(name)

    def listen(self, data):
        for name, effector in self._effectors.items():
            if not name in data._actions:
                continue
            for action in data._actions[name]:
                effector.run(action)
