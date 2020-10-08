from abc import ABC, abstractmethod

class Observer(ABC):

    def __init__(self):
        pass

    def bind(self, subject):
        self._subject = subject

    def unbind(self):
        self._subject = None

    @property
    def subject(self):
        return self._subject

    @abstractmethod
    def update(self, subject):
        raise Exception('Not implemented update method')


if __name__ == '__main__':

    from subject import Subject

    class Sensor(Subject):

        def __init__(self):
            super(Sensor, self).__init__()
            self._integer = 0

        @property
        def integer(self):
            return self._integer

        @integer.setter
        def integer(self, integer):
            self._integer = integer
            self.notify()

        def notify(self):
            for observer in self.observers:
                observer.update(self)

    class Monitor(Observer):
        
        def __init__(self, name):
            super(Monitor, self).__init__()
            self._name = name

        def update(self, subject):
            print('The {} has {} value'.format(self._name, subject.integer))




    subject = Sensor()

    monitor = Monitor("monitor 1")
    monitor2 = Monitor("monitor 2")

    subject.attach(monitor)
    subject.attach(monitor2)

    subject.integer = 100
    subject.integer = 50








