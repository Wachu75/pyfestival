
class BankAccount:
    def __init__(self):
        self.amount = 0

    def deposit(self, amount: int):
        self.amount += amount
        return self.amount

    def withdraw(self, amount: int):
        if amount < self.amount:
            to_withdraw = self.amount
            self.amount = 0
            return to_withdraw
        self.amount -= amount
        return amount


class SavingAccount(BankAccount):
    def __init__(self, percent: float):
        super().__init__()
        self.percent = percent

    def accumulate(self):
        self.amount += self.amount * self.percent
        return self.amount


def test_saving_account():
    # given
    account = SavingAccount(0.1)
    account.deposit(1000)

    # when
    account.accumulate()

    # then
    assert account.withdraw(1000) == 1100

