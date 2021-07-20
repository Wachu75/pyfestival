def repeat(values):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            temp = 0
            value = int(''.join(map(str, args)))

            print(type(value))
            for n in range(values):
                temp += value

            return temp
        return inner_wrapper
    return wrapper

def foo():
    return "bar"

def hello(name):
    return name

def count(a):
    return a

def upercase(func):   #definicja dekoratora
    def wrapper(*args, **kwargs):           # def wrapper jest czyms w rodzaju wydmuszki jegozadanie to odebranie argumentów i przekazanie ich dalej
        return func(*args, **kwargs).upper()
    return wrapper

print(upercase(foo)())
print(upercase(hello)('ktos'))

print(repeat(6)(count)(7))




# def dekorator_one(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)
#         if ininstance(value, list):
#             return [str(element) for element in value]
#         else:
#             return str(value)
#     return wrapper

