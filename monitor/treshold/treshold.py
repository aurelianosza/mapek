import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from functools import wraps
from exceptions.read_value_exception import ReadValueException

def Treshold(value, min_value, max_value):

    if value < min_value or value > max_value:
        raise ReadValueException(value)

    return value

    

if __name__ == '__main__':
    
    from random import randint

    def valor_leitura(min, max):
        return randint(min, max)

    for i in range(1, 100):
        try:

            aux = Treshold(valor_leitura(0, 400), 20, 100)
            print("Valor lido corretamente {}".format(aux))

        except ReadValueException as ex:
            print("Erro no valor de leitura {}".format(ex.value))

        finally:
            pass


    