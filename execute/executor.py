import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.listener import Listener

class Executor(Listener):

    def __init__(self):
        Listener.__init__(self)
        self._effectors = {}

    def add_effector(self, name, effector):
        self._effectors[name] = effector

    def remove_effector(self, name):
        self._effectors.pop(name)

    def listen(self, data):
        for name, effector in self._effectors.items():
            if not name in data._actions:
                continue
            for action in data._actions[name]:
                effector.run(action)
            


if __name__ == '__main__':
    
    from interfaces.strategy import Strategy
    from interfaces.publisher import Publisher
    from execute.effector import Effector
    from plan.changes_plan import ChangesPlan
    from actions.action import SimpleAction

    class SimplePublisher(Publisher):

        def __init__(self):
            Publisher.__init__(self)

    class PrintDictStrategy(Strategy):

        def __init__(self):
            Strategy.__init__(self)

        def execute(self, action):
            print(action.__dict__)

    class PrintRawStrategy(Strategy):

        def __init__(self):
            Strategy.__init__(self)

        def execute(self, action):
            data = action.command
            for param in action.params.values():
                data = "{},{}".format(data, param)
            print(data)

    
    publisher = SimplePublisher()

    executor = Executor()

    publisher.add_listener(executor)

    executor.add_effector('dict', Effector(PrintDictStrategy()))
    executor.add_effector('raw', Effector(PrintRawStrategy()))

    cp = ChangesPlan()

    cp.add_action('dict', SimpleAction('set_temperatura', {'value': 50, 'time': '10s'}))
    cp.add_action('dict', SimpleAction('set_pressao', {'value': 250, 'time': '30s'}))

    publisher.publish(cp)



