def dekorator_one(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        if ininstance(value, list):
            return [str(element) for element in value]
        else:
            return str(value)
    return wrapper

