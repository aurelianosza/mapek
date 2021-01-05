import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)


class Symptom(object):

    def __init__(self, name, property_name, operator, base):
        self._name = name
        self._property = property_name
        self._operator = operator
        self.base = base


    