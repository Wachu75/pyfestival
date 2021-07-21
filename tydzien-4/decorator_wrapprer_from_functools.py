#   More generally, it is good practice to use functools .wraps when you create the wrapper,

from datetime import datetime
from functools import wraps


def timeCalled(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{datetime.now()}: Function called {func.__name__}')
        result = func(*args, **kwargs)
        return result
    return wrapper


@timeCalled
def printArg(arg):
    print(f'Your arg is {arg}')


printArg.__wrapped__('aaaa')
print('*' * 50)
printArg('bbbbb')
