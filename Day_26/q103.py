class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0: self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance: self.balance -= amount
    def check_balance(self):
        return self.balance

if __name__ == "__main__":
    atm = ATM(1000)
    print(f"Initial balance: {atm.check_balance()}")
    atm.deposit(500)
    print(f"After deposit: {atm.check_balance()}")
    atm.withdraw(200)
    print(f"After withdrawal: {atm.check_balance()}")
