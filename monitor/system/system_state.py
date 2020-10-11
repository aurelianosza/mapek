from datetime import datetime

class SystemState(object):

    def __init__(self):
        self._properties = {}

    def set_property(self, key, value):
        self._properties[key] = {'value': value, 'updated_at' : datetime.now()}

    def get_property(self, key):
        return self._properties[key]
