import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class Knowedge(object):

    def __init__(self):
        self.create = None
        self.read = None
        self.update = None
        self.delete = None

    def create(self, data):
        if self.create is None
            return
        self.create(data)

     