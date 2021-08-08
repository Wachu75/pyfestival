
class Employee:
    def __init__(self, name, sure_name, salary):
        self.salary = salary
        self.name = name
        self.sure_name = sure_name

    def get_salary(self):
        return self.salary

    def show_yourself(self):
        return f'{self.sure_name}, {self.name} -> {self.salary}'

class Manager(Employee):
    def __init__(self, name, sure_name, salary):
        super().__init__(name, sure_name, salary)

    def add_bonus(self, amount: int):
        self.amount = amount
        bonus = (self.salary * self.amount) / 100
        return bonus

    def total_salary(self):
        self.salary += self.add_bonus
        return self.salary

jon = Employee('Jon', 'Smith', 10)

print(jon.show_yourself())

jan = Manager('Jan', 'Nowak', 10)

print(jan.show_yourself())
print(jan.add_bonus(10))
print(jan.total_salary())
