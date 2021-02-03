import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class ChangesPlan(object):

    counter = 0

    def __init__(self):
        ChangesPlan.counter += 1
        self.id_request = ChangesPlan.counter
        self._actions = {}

    def add_action(self, effector_name, action):

        if not effector_name in self._actions:
            self._actions[effector_name] = []    
        
        self._actions[effector_name].append(action)
