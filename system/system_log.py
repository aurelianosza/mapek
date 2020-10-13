import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class SystemLog(object):

    def __init__(self):
        Observer.__init__(self)
        self._recorders = {}

    def push(self, info):
        for key, value in self._recorders.items():
            value.execute(info)

    def add_recorder(self, name, recorder):
        self._recorders[name] = recorder


if __name__ == '__main__':

    from datetime import datetime
    from interfaces.strategy import Strategy
    from interfaces.subject import Subject
    class TerminalStrategy(Strategy):

        def __init__(self):
            Strategy.__init__(self)

        def execute(self, subject):
            print("{} Receive {} value".format(datetime.now(), subject.value))

    class FileStrategy(Strategy):
    
        def __init__(self):
            Strategy.__init__(self)

        def execute(self, subject):
            with open('log.txt', 'a') as file:
                file.write("{} Receive {} value\n".format(datetime.now(), subject.value))

    class SimpleSubject(Subject):

        def __init__(self):
            Subject.__init__(self)
            self._value = 0

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, value):
            self._value = value
            self.notify()

    log = SystemLog()

    log.add_recorder('terminal', TerminalStrategy())
    log.add_recorder('file', FileStrategy())

    subject = SimpleSubject()

    subject.attach(log)

    for i in range(99):
        subject.value = i
