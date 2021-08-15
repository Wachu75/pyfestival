from datetime import datetime

class Application:
    @staticmethod
    def main():
        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_start = datetime.strptime(input("date of employment(2021-01-01): "), '%Y.%m.%d')
        if not Application.check_date_of_employment(datetime.today(), date_start):
            raise InvalidDateOfEmployment()

        employee = BaseEmployee(first_name, last_name, date_start)

    @staticmethod
    def check_date_of_employment(today: datetime, date: datetime):
        difference = today - date
        difference_in_years = round(difference.days / 365)
        return 50 > difference_in_years > 0

class InvalidDateOfEmployment(Exception):
    pass

class BaseEmployee:
    def __init__(self, name, surname, date_start: datetime):
        self.date_start = date_start
        self.surname = surname
        self.name = name

    @property
    def employment_time(self):
        today = datetime.today()
        difference = today - self.date_start
        return difference.days

    def __lt__(self, other):
        return self.employment_time < other.employment_time

    def __repr__(self):
        return self.name

    # try:
    # if dateToday > date_start or dateToday - date_start > 50*365
    # InvalidDateOfImployment

    def sortTimeEmployment(self):
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


if __name__ == '__main__':
    Application.main()

def test_sort_employee():
    a = BaseEmployee('a','a',datetime(2020,10,10))
    b = BaseEmployee('b','b',datetime(2020,8,10))
    employees = [a, b]

    sorted_employees = sorted(employees)

    assert sorted_employees[0] == a