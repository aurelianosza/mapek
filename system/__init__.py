import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent)

from system.strategies.mysql_strategy import MysqlStrategy
from multiprocessing.managers import BaseManager
from system.system_log_singleton import SystemLogSingleton

BaseManager.register('MysqlStrategy', MysqlStrategy)
manager = BaseManager()
manager.start()

s = SystemLogSingleton().get_instance()

# m = manager.MysqlStrategy()

# s.add_recorder('database', m)
