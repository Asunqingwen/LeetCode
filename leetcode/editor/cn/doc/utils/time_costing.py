'''
计算程序运行时间
'''
from time import time


def timeCosting(func):
    def wrapper(*args, **kw):
        local_time = time()
        res = func(*args, **kw)
        print('current Function [%s] run time is %.2f' % (func.__name__, time() - local_time))
        return res

    return wrapper