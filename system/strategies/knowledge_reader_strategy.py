import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from interfaces.strategy import Strategy
import json

class KnowledgeReaderStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)

    def execute(self, data):
        aux = None
        with open('data.json', 'r') as f:
            aux = json.loads(f.read())
            if data in aux:
                return {data: aux[data]}
            return None

if __name__ == '__main__':
    
    k = KnowledgeReaderStrategy()

    print(k.execute('alias'))
    

