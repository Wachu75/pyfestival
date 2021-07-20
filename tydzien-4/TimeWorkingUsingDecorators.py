import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# Timing Functions
# This decorator works by storing the time just before the function starts running
# (at the line marked # 1)# and just after the function finishes (at # 2).
# The time the function takes is then the difference
# between the two (at # 3). We use the time.perf_counter() function,
# which does a good job of measuring time intervals. Here are some examples of timings:

# Note: The @timer decorator is great if you just want to get an idea about the runtime
# of your functions. If you want to do more precise measurements of code,
# you should instead consider the timeit module in the standard library.
# It temporarily disables garbage collection and runs multiple trials
# to strip out noise from quick function calls.