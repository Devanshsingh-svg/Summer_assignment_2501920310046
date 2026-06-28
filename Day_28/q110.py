class BankAccount:
    def __init__(self, acc_no: str):
        self.acc_no = acc_no
        self.balance = 0.0
    def deposit(self, amt: float):
        self.balance += amt
    def withdraw(self, amt: float):
        if amt <= self.balance: self.balance -= amt

if __name__ == "__main__":
    acc = BankAccount("12345")
    acc.deposit(100)
    acc.withdraw(50)
    print(f"Balance: {acc.balance}")
