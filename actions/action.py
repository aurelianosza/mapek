import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.action import Action

class ExampleUserAction(Action):

    def __init__(self, command, params):
        pass
