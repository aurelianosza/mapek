import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from monitor.data_interceptor import DataInterceptor
from monitor.sensor.interval_sensor import IntervalSensor
from monitor.sensor.passive_sensor import PassiveSensor

class BaseController(object):

    def __init__(self):
        self._sensors = {}


    """
    [
        {
            sensor: <name:param1,param2,param3...>,
            limits: <value_1>,<value_2>
            interval: <int(for IntervalSensor) or None(PassiveSensor)>,
            property: <identifier>,
            
        }
    ]
    """
    def _load_sensors(self, monitor, data):
        
        sensors = []

        for sensor_data in data:
            sensors.append(self.__separate_sensor_data(sensor_data))
            
        for sensor in sensors:
            self.__set_sensor_observer(sensor)
            self.__bind_data_interceptors(monitor, sensor)
            self.__start_sensor(sensor)


    """
        {
            sensor: <name:param1,param2,param3...>,
            limits: <value_1>,<value_2>
            interval: <int(for IntervalSensor) or None(PassiveSensor)>,
            property: <identifier>,
            
        }
    """
    def __separate_sensor_data(self, data):

        sensor = self.__separate_sensor_strategy(data['sensor'])

        data_interceptor = self.__separate_data_interceptor(data['limits'])

        interval = None
        if 'interval' in data.keys() and data.get('interval') is not None:
            interval = int(data.get('interval'))

        name = data.get('property')

        if interval is None:
            sensor = PassiveSensor(name, sensor)
        else:
            sensor = IntervalSensor(name, sensor, interval)

        return {
            "sensor": sensor,
            "data_interceptor": data_interceptor,
            "name": name              
        }

    """
    string <name:param1,param2,param3...>
    """
    def __separate_sensor_strategy(self, data):
        sensor_ref, *params_raw = data.split(':')

        if len(params_raw) > 0:
            params_raw = params_raw[0].split(',')

        return self._sensors.get(sensor_ref)(*tuple(params_raw))


    """
    string <value_1>,<value_2>
    """
    def __separate_data_interceptor(self, data):
        min, max = data.split(',')

        min = int(min)
        max = int(max)

        return DataInterceptor(min, max)

    def __set_sensor_observer(self, data):
        data['sensor'].attach(data['data_interceptor'])

    def __bind_data_interceptors(self, monitor, data):
        monitor.add_interceptor(data['name'], data['data_interceptor'])

    def __start_sensor(self, data):
        data['sensor'].start()
        

    
    