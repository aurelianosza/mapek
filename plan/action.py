import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class Action(object):

    def __init__(self, comand, params):
        self.command = comand
        self.params = params
