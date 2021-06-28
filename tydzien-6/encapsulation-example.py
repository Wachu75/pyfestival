class Student:
    def __init__(self, semestr: int, data):
        self._semestr = semestr
        self._data = data

    def __str__(self):
        return f'{self._data}, semestr: {self._semestr}'

student = Student('kowalski', 1)
print(student._data)
print(student._semestr)
