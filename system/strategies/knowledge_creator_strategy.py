import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.strategy import Strategy
import json

class KnowledgeCreatorStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)

    def execute(self, data):
        pass
