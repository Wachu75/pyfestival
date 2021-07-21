from time import time
from functools import wraps

def counter_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)
        end = time()
        total = end - start
        print(f'time: {total:.4f}')
        return value
    return wrapper

@counter_time
def doItSomething(times):
    for _ in range(times):
        values = sum([i**2 for i in range(1000000)])
    return values

print(doItSomething(3))
print('* ' * 80)
print('example without @decorator ')

print(doItSomething.__wrapped__(3))
