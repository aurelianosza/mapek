import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

import mysql.connector
from interfaces.strategy import Strategy

class MysqlStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self._connection = mysql.connector.connect(
            host="127.0.0.1",
            port=6603,
            user="root",
            password="toor",
            db="mapek"
        )
        
    def __close(self):
        self._connection.close()

    def execute(self, message):
        cursor = self._connection.cursor()
        sql_raw = 'INSERT INTO logs VALUES (%s, %s)'
        cursor.execute(sql_raw, (None, message))
        self._connection.commit()
        
if __name__ == '__main__':
    
    r = MysqlStrategy()

    r.execute('aqui')

    