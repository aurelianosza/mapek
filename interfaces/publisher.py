
class Publisher(object):

    def __init__(self):
        #var array
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove[listener]

    def publish(self, data):
        for listener in self._listeners:
            listener.listen(data)
