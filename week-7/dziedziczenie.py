
class Samochody:
    def __init__(self, text):
        self.text = text

    def przedstaw_sie(self):
        return print(self.text)

class Car(Samochody):
    pass

s1 = Samochody('maluch')
s2 = Car('fiat')

print(s1.text)
print(s2.text)
# **********************************

class User:
    def login(self):
        return 'jestem zalogowany'

class Teacher(User):
    def run(self):
        return 'nauczam'

class Student(User):
    def run(self):
        return 'studiuje'

jhon = Teacher()
print(jhon.run())
print(jhon.login())
#*************************************


class Parent:
    def get_type(self):
        return 'parent'

class Child(Parent):
    def get_type(self):      # get_type zasłania get_type z class Parent
        return 'child'

jhon = Child()
print(jhon.get_type())

#*************************************

