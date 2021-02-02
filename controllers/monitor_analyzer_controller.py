import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from monitor.monitor import Monitor
from monitor.sensor import interval_sensor
from interfaces.strategy import Strategy
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
from random import randint
from exceptions.read_value_exception import ReadValueException
from monitor.treshold.treshold import Treshold
from datetime import datetime
from monitor.data_interceptor import DataInterceptor
from multiprocessing.managers import BaseManager
from controllers.base_controller import BaseController
from analyzer.analyzer import Analyser
from analyzer.symptom import Symptom
from system.knowledge_singleton import KnowledgeSingleton
from system.strategies.zqm_strategy import ZmqStrategy
from plan.planner import Planner
from plan.action import Action
from plan.changes_plan import ChangesPlan
from interfaces.listener import Listener

class SocketStrategy(Strategy):

    def __init__(self, addr, port):
        Strategy.__init__(self)
        self._addr = addr

    def execute(self):
        return randint(20, 240)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self._addr)
        data = sock.recv(1024)
        sock.close()
        return int(data.decode())

class LimitSymptom(Symptom):

    def __init__(self, name, manager, data):

        Symptom.__init__(self, name, manager)

        self.limit =  data['limit']
        self.property = data['property']

    def handle(self):
        aux = self._manager._knowledge.read(self.property)
        return aux and int(aux[self.property]) > int(self.limit)

class AllStrategy(Strategy):

    def __init__(self, data):
        Strategy.__init__(self)

    def execute(self):
        change_plan = ChangesPlan()
        change_plan.add_action(Action('set_temperatura', {'value': randint(20, 240)}))
        change_plan.add_action(Action('set_pressao', {'value': randint(20, 240)}))
        return change_plan

class TemperaturaStrategy(Strategy):
    
    def __init__(self, data):
        Strategy.__init__(self)

    def execute(self):
        change_plan = ChangesPlan()
        change_plan.add_action(Action('set_temperatura', {'value': randint(20, 240)}))
        return change_plan

class PressaoStrategy(Strategy):
    
    def __init__(self, data):
        Strategy.__init__(self)

    def execute(self):
        change_plan = ChangesPlan()
        change_plan.add_action(Action('set_pressao', {'value': randint(20, 240)}))
        return change_plan

class PlannerListener(Listener):

    def __init__(self):
        Listener.__init__(self)

    def listen(self, data):
        for action in data._actions:
            print('command {}, params {}'.format(action.command, action.params))

class MonitorAnalyzerController(BaseController):

    def __init__(self):
        BaseController.__init__(self)
        self.monitor = Monitor()
        self.analyzer = Analyser()
        self.planner = Planner()
        
        knowledge_accessor = KnowledgeSingleton()
        self.knowledge = knowledge_accessor.get_instance()
        
        external_publisher = self.manager.ZmqStrategy()

        self.monitor.add_listener(self.knowledge)
        self.monitor.add_listener(external_publisher)

        self.monitor.attach(self.analyzer)

        self.analyzer.add_listener(self.planner)

        self.planner.add_listener(PlannerListener())

    def start(self):
        self._sensors = {
            "socket" : SocketStrategy
        }

        data = [
            {
                "sensor": 'socket:127.0.0.1,7666',
                "limits": '0,160',
                "interval": 5,
                "property": 'pressao'
            },
            {
                "sensor": 'socket:127.0.0.1,8666',
                "limits": '0,160',
                "interval": 5,
                "property": 'temperatura'
            },
        ]

        self._load_sensors(self.monitor, data)

        self.analyzer.add_symptom('pressao_symptom', LimitSymptom, {'limit': 55, 'property': 'pressao'})
        self.analyzer.add_symptom('temperatura_symptom', LimitSymptom, {'limit': 85, 'property': 'temperatura'})

        self.planner.add_strategy(['pressao_symptom', 'temperatura_symptom'], AllStrategy) 
        self.planner.add_strategy(['pressao_symptom'], PressaoStrategy) 
        self.planner.add_strategy(['temperatura_symptom'], TemperaturaStrategy) 

        while True:
            pass


if __name__ == '__main__':

    controller = MonitorAnalyzerController()
    controller.start()


