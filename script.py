class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
    
    def display_account_info(self):
        display = f"Balance: ${self.balance}-Interest Rate: {self.int_rate}"
        return display

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
            return self
        else:
            print("Negative account balance. No yield")
            return self

    @classmethod
    def print_all_info(cls):
        for account in cls.all_accounts:
            print(account.display_account_info())

martin = BankAccount(balance = 1000)
jessica = BankAccount(balance = 1000)

martin.deposit(100).deposit(150).deposit(50).withdraw(100).display_account_info()

jessica.deposit(700).deposit(800).withdraw(100).withdraw(45).withdraw(14).withdraw(25).yield_interest().display_account_info()

BankAccount.print_all_info()