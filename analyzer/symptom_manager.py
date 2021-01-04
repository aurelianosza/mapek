import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

class SymptomManager(object):

    def __init__(self):
        self._symptoms = {}

        self._symptoms_base = {}

    def verify(self):

        symptoms = filter(lambda symptom: symptom.handle(), self._symptoms.values())

        return symptoms

    def add_symptom(self, symptom, name, data):
        self._symptoms[name] = symptom(name, self, data)


if __name__ == '__main__':

    from random import randint
    from symptom import Symptom

    class SimpleSymptom(Symptom):

        def __init__(self, name, manager, data):

            Symptom.__init__(self, name, manager)

            self.min = data['min']
            self.max = data['max']

        def handle(self):
            return randint(self.min, self.max) % 2 == 0

    
    sm = SymptomManager()

    sm.add_symptom(SimpleSymptom, 'some_name', {'min': 5, 'max': 30})
    sm.add_symptom(SimpleSymptom, 'some_name_2', {'min': 30, 'max': 100})

    for i in sm.verify():
        print(i._name)
