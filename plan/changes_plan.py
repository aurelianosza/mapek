import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)


class ChangesPlan():

    def __init__(self):
        self._actions = []

    def add_action(self, action):
        self._actions.append(action)
