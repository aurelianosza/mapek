import path
import sys

class AnalyzerPublisher(object):
    
    def __init__(self):
        self.registers = {}

    def subscribe(self, name, register):
        self.registers[name] = register


    def publisher(self, data):
        for key, register in self.registers.items():
            register.listen(data)


if __name__ == '__main__':
    
    from random import randint

    class Plan(object):

        def listen(self, data):
            print("printed from plan {}".format(data))

    class OtherClass(object):

        def listen(self, data):
            print("printed from other class {}".format(data))

    
    a = AnalyzerPublisher()

    a.subscribe('plan', Plan())

    a.subscribe('other', OtherClass())

    for i in range(randint(1, 99)):
        a.publisher(randint(1, 9999))



    
