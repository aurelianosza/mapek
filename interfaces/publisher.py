
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

if __name__ == '__main__':
    
    class SimpleListener(object):

        def listen(self, data):
            print("listen {} form simple listener".format(data))

    class OtherSimpleListener(object):

        def listen(self, data):
            print("listen {} form other simple listener".format(data))

    p = Publisher()
    p2 = Publisher()
    
    p.add_listener(SimpleListener())
    p.add_listener(OtherSimpleListener())

    p2.add_listener(SimpleListener())
    p2.add_listener(OtherSimpleListener())

    p.publish('p1 value')
    
    p2.publish('p2 value')
