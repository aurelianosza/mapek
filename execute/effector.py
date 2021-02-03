import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class Effector(object):

    def __init__(self, strategy):
        self._strategy = strategy

    def run(self, action):
        self._strategy.execute(action)
