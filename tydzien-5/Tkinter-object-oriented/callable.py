'''
4) Classes

All classes are callable. When you call a class, you get a new instance of the class. For example:

class Counter:
    def __init__(self, start=1):
        self.count = start

    def increase(self):
        self.count += 1

    def value(self):
        return self.count
Code language: Python (python)

5) Methods

Methods are functions bound to an object, therefore, they’re also callable. For example:

print(callable(Counter.increase))  # True
Code language: Python (python)

Output:

True
Code language: PHP (php)

6) Instances of a class

If a class implements the __call__ method, all instances of the class are callable:

class Counter:
    def __init__(self, start=1):
        self.count = start

    def increase(self):
        self.count += 1

    def value(self):
        return self.count

    def __call__(self):
        self.increase()


    counter = Counter()
    counter()

    print(callable(counter))  # True
Code language: Python (python)

Output:

True
Code language: PHP (php)

Summary

    An object is callable when it can be called using the () operator.
    Use the Python callable built-in function to check if an object is callable or not.
'''

