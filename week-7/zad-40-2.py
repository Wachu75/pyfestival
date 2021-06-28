
class Employee:
    def __init__(self, firt_name, last_name, hourly_rate: float):
        self.hourly_rate = hourly_rate
        self.last_name = last_name
        self.firt_name = firt_name
        self.time_spent = 0

    def add_time(self, time: float):
        self.time_spent += time

    def pay(self):
        return self.time_spent * self.hourly_rate


class Manager(Employee):
    def __init__(self, firt_name, last_name, hourly_rate: float):
        super().__init__(firt_name, last_name, hourly_rate)
        self.bonus = 0

    def add_bonus(self, bonus):
        self.bonus += bonus

    def pay(self):
        return super().pay() * 2 + self.bonus


m1 = Manager('fred', 'flinston', 100)
m1.add_time(3)
m1.add_bonus(100)
print(m1.pay())


