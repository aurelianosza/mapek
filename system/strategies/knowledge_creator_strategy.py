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
        aux = None
        with open('data.json', 'r') as f:
            aux = json.loads(f.read())
        for key, val in data.items():
            aux[key] = val
        with open('data.json', 'w') as f:
            f.write(json.dumps(aux))

if __name__ == '__main__':
    
    k = KnowledgeCreatorStrategy()

    k.execute({"name": 'foo', "alias": 'bar'})
    

