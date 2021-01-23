import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)


class ChangePlan():

    self __init__(self, data):
        self._data = data
