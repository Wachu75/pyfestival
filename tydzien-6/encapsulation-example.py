class Student:
    def __init__(self, semestr: int, data):
        self._semestr = semestr
        self._data = data

    def __str__(self):
        return f'{self._data}, semestr: {self._semestr}'

    @property
    def data(self):
        return self._data


student = Student('kowalski', 1)
print(student.data)
print(student._semestr) #pycharm nie podpowiada pól prywatnych ale możemy je wpisać na siłe musimy je znać !
print(student)