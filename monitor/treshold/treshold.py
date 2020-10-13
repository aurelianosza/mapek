import path
import sys

folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)

from functools import wraps
from exceptions.read_value_exception import ReadValueException

def Treshold(min_value, max_value):

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            aux = function(*args, **kwargs)

            if aux < min_value or aux > max_value:
                raise ReadValueException(aux)

            return aux
        return wrapper
    return inner_function

if __name__ == '__main__':
    
    from random import randint

    @Treshold(20, 50)
    def valor_leitura(min, max):
        return randint(min, max)

    for i in range(1, 100):
        try:

            aux = valor_leitura(0, 400)
            print("Valor lido corretamente {}".format(aux))

        except ReadValueException as ex:
            print("Erro no valor de leitura {}".format(ex.value))

        finally:
            pass


    