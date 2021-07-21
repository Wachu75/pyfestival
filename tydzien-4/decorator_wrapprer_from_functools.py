#  To retrieve it.

#  More generally, it is good practice to use functools.wraps when you create the wrapper,
#  this makes the wrapper function "look like" the original function. Moreover,
#  it adds the original function to a __wrapped__ attribute, so:

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


#In which case, you can use:

printArg.__wrapped__('aaaa')
printArg('bbbbb')
