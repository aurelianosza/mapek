import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

class SymptomRepository(object):

    def __init__(self, loadSymptoms=None):
        self._symptoms = {}
        self._loadSymptoms = loadSymptoms 
        self._operators = {}
        self._load()
        self._create_operators()

    def _load(self):
        if self._loadSymptoms is None:
            return

        self._symptoms = self._loadSymptoms.execute()

    def _create_operators(self):
        self._operators['>'] = lambda x, y : x > y
        self._operators['<'] = lambda x, y : x < y
        self._operators['='] = lambda x, y : x == y
        self._operators['>='] = lambda x, y : x >= y
        self._operators['<='] = lambda x, y : x <= y
        self._operators['!='] = lambda x, y : x != y

    def add_operator(self, name, function):
        self._operators[name] = lambda x, y : function(x, y)

    def add_symptom(self, symptom):

        if self._symptoms[symptom.property_name] is None:
            self._symptoms[symptom.property_name] = []

        self._symptoms[symptom.property_name].append(symptom)

    def search(self, state):
        pass

    def _verify_symptom(self, symptom, state):
        return self._operators[symptom.operator](state[symptom.property_name], symptom.base)





    


