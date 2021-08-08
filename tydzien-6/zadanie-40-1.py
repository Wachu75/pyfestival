
class BankAccount:
    def __init__(self):
        self._money = 0

    def deposit(self, money_add):
        self._money += money_add

    def withdraw(self, money_out):
        if money_out > self._money:
            to_exit = self._money
            self._money = 0
            return to_exit
        self._money -= money_out
        return self._money

    def get_stan(self):
        return self._money
        #return f'stan konta: {self.money}'

class SavingsAccount(BankAccount):
    def __init__(self): #, percent
        super().__init__()
        #self.percent = percent

    def bonus(self, percent):
        self.percent = percent
        #super()._money += super()._money * self.percent
        self._money += self._money * self.percent
        #return print(f'{self._money}')

    def get_status(self):
        return super().get_stan()

saldo = SavingsAccount()  #0.1
saldo.deposit(1000)

saldo.bonus(0.2)
print(saldo.get_stan())
print(saldo.get_status())
saldo.bonus(0.04)
print(saldo.get_stan())




