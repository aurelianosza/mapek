from datetime import datetime

class SystemState(object):

    def __init__(self):
        self._properties = {}

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        for key in properties.keys():
            self._properties[key] = {'value': properties[key], 'updated_at' : datetime.now()}




if __name__ == '__main__':
    
    s = SystemState()

    s.properties = {'temperatura': 10, 'presao' : 20}

    print(s.properties)
    