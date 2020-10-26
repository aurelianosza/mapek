import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from interfaces.observer import Observer
from exceptions.read_value_exception import ReadValueException
from system.system_log_singleton import SystemLogSingleton as SystemLog
from monitor.treshold import Treshold

class DataInterceptor(Observer):

    def __init__(self, monitor, min_value, max_value):
        Observer.__init__(self)
        Subject.__init__(self)
        self._system_log = SystemLog().get_instance()
        self._min_value = min_value
        self._max_value = max_value

    def dispatch(self, property, value):
        self.monitor.listen(property, value)

    def update(self, sensor):
        try:
            value = Treshold(sensor.value, self._min_value, self._max_value)
        except ReadValueException as e:
            self._system_log.write('Erro na leitura de {}, valor lido {}'.format(self.sensor.name, e.value))
        finally:
            pass



    

    