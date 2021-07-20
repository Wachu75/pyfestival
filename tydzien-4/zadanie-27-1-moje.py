def round_values(function):
    def wrapper(*args, **kwargs):
        values = function(*args, **kwargs)
        return f'{values:.2f}'

        return values
    return wrapper


@round_values
def count():
    return 1.234567

print(count())

# how skip decorators and call only function

print(count.__closure__[0].cell_contents())

