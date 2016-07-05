import math
import pydash

def addition(a, b):
    if isinstance(a, int) is not True or isinstance(b, int) is not True:
        return 'NaN'

    return pydash.pluck([{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}], 'name')
    #return int(a) + int(b)
