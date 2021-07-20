import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

# The following @debug decorator will print the arguments a function
# is called with as well as its return value every time the function is called:
# The signature is created by joining the string representations of all the arguments.
# The numbers in the following list correspond to the numbered comments in the code:
#
#   Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
#   Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r
#   specifier means that repr() is used to represent the value.
#   The lists of positional and keyword arguments is joined together to one signature string with each
#   argument separated by a comma.
#   The return value is printed after the function is executed.
#
# Let’s see how the decorator works in practice by applying it to a simple function with one position
# and one keyword argument:

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

# >>> make_greeting(name="Dorrisile", age=116)
# Calling make_greeting(name='Dorrisile', age=116)
# 'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
# 'Whoa Dorrisile! 116 already, you are growing up!'

# This example might not seem immediately useful since the @debug decorator just repeats what you
# just wrote. It’s more powerful when applied to small convenience functions that you don’t call
# directly yourself.
#
# The following example calculates an approximation to the mathematical constant e:

import math
from decorators import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

# When calling the approximate_e() function, you can see the @debug decorator at work:
#
# >>> approximate_e(5)
# Calling factorial(0)
# 'factorial' returned 1
# Calling factorial(1)
# 'factorial' returned 1
# Calling factorial(2)
# 'factorial' returned 2
# Calling factorial(3)
# 'factorial' returned 6
# Calling factorial(4)
# 'factorial' returned 24
# 2.708333333333333
#
# In this example, you get a decent approximation to the true value e = 2.718281828, adding only 5 terms.