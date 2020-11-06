import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)


class BaseController(object):

    def __init__(self):
        self._sendors_strategies = {}

    
if __name__ == '__main__':
    
    def sum(a, b):
        return a + b

    print(sum(*(1, 2)))
    

    