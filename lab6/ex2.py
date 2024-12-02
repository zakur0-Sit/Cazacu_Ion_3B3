class Account:
    def __init__(self, value=0):
        self.value = value

    def deposit(self, value):
        if value > 0:
            self.value += value
        else:
            return "No money to deposit"

    def withdrawal(self, value):
        if value <= self.value:
            self.value -= value
        else:
            return "Insufficient amount of money on account"

    def balance_check(self):
        return self.value

class SavingAccount(Account):
    def __init__(self, value=0, interest=0.01):
        super().__init__(value)
        self.interest = interest

    def interest_calculation(self):
        self.value += self.value * self.interest


class CheckingAccount(Account):
    def __init__(self, value=0, overdraw=0):
        super().__init__(value)
        self.overdraw = overdraw

    def withdrawal(self, value):
        if value - self.overdraw <= self.value:
            self.value -= value
        else:
            return "Insufficient amount of money on account"

saving_account = SavingAccount(100, 0.02)
checking_account = CheckingAccount(200)

saving_account.deposit(100)
saving_account.interest_calculation()
print("Balance on saving account : " + str(saving_account.balance_check()))

print("Balance on checking account : " + str(checking_account.balance_check()))
checking_account.withdrawal(50)
print("Balance on checking account : "+str(checking_account.balance_check()))