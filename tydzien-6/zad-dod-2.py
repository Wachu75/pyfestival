from datetime import datetime

class Student:
    def __init__(self, name, birth_year):
        self._birth_year = birth_year
        self.name = name

    def get_birth_year(self):
        return self._birth_year


    def get_age(self):
        today = datetime.today()
        return today.year - self._birth_year

    