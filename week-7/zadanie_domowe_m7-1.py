from datetime import date

class BaseEmployee:
    def __init__(self, name, surname, date_start: date):
        self.date_start = date_start
        self.surname = surname
        self.name = name

    # try:
    # if dateToday > date_start or dateToday - date_start > 50*365
    # InvalidDateOfImployment

    def sortTimeEmployment(self):
        pass

    @property
    def employmentTime(self):
        pass
# ile dni pracuje dany pracownik od początku

class Employee(BaseEmployee):
    pass

# stawka godzinowa
# wymiar etatu
# premia
    def salary(self):
        pass

    def createFullTime(self):
        pass

    def createPartfTime(self):
        pass


