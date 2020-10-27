import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from exceptions.read_value_exception import ReadValueException
from system.system_log_singleton import SystemLogSingleton as SystemLog
from monitor.treshold.treshold import Treshold

class DataInterceptor(Observer):

    def __init__(self, min_value, max_value):
        Observer.__init__(self)
        self._system_log = SystemLog().get_instance()
        self._min_value = min_value
        self._max_value = max_value
        self.monitor = None

    def dispatch(self, property, value):
        if self.monitor is None:
            return
        self.monitor.listen(property, value)

    def update(self, sensor):
        try:
            value = Treshold(sensor.value, self._min_value, self._max_value)
            self.dispatch(sensor.name, value)
        except ReadValueException as e:
            self._system_log.write('Erro na leitura de {}, valor lido {}'.format(sensor.name, e.value))
        finally:
            pass



    

    