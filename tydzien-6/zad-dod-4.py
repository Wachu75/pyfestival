
class Worker:
    def __init__(self, first_name: str, last_name: str, hourly_rate: int):
        self._hourly_rate = hourly_rate
        self.last_name = last_name
        self.first_name = first_name
        self.time_spent = 0

    def get_brutto(self):
        return self._hourly_rate

    def get_netto(self):
        return self._hourly_rate - (self._hourly_rate * 0.19 )

class Schedule:
    def __init__(self):
        self.workers = []

    def log_time(self, employee: Worker, minutes: int):
        for worker in self.workers:
            if worker == employee:
                worker.time_spent += minutes
                return

        employee.time_spent = minutes
        self.workers.append(employee)
