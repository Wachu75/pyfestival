from abc import ABC, abstractmethod

class Actor(ABC):
    def __init__(self, first_name, Last_name):
        self.first_name = first_name
        self.Last_name = Last_name

    @abstractmethod
    def hello(self):
        return f'Hello my name is {self.first_name} {self.Last_name} and I am'


class Student(Actor):
    def hello(self):
        return Actor.hello(self) + ' a student'


class Employee(Actor):
    def hello(self):
        return Actor.hello(self) + ' an employee'


class Teacher(Actor):
    def hello(self):
        return Actor.hello(self) + ' a Teacher'


class Person:
    @staticmethod
    def create_new(class_name, first_name, last_name):
        try:

            class_ = globals()[class_name]
            return class_(first_name, last_name)
        except KeyError:
            print(f' unknow class name {class_name}')


s = Person.create_new('Teacher','aaaa','bbbbb')
print(s.hello())

