from time import time, sleep


def round_it(func):
    def wrapper(*args, **kwargs):

        return round(func(*args, **kwargs),2)

    return wrapper

def test_round_it():
    @round_it
    def function(values):
        return values

    assert function(3.567) == 3.57
    assert function(3.5000) == 3.5


def get_execution_details(function):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        start = time()
        output = function(*args, **kwargs)
        end = time()
        print(f'execution time {end-start}')
        return output
    return wrapper

@get_execution_details
def go_to_sleap(time):
    sleep(time)
    print('spie')
    sleep(time)


go_to_sleap(3)
