from datetime import datetime

class SystemState(object):

    def __init__(self):
        self._properties = {}

    def set_property(self, key, value):
        self._properties[key] = {'value': value, 'updated_at' : datetime.now()}

    def get_property(self, key):
        if not key in self._properties:
            return None
        return self._properties[key]
