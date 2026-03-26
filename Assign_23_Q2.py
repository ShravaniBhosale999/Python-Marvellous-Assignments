
class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance

    def Display(self):
        print(f"Name:{self.Name}, Balance:{self.Balance}, ROI:{BankAccount.ROI}")

    def Deposit(self, Amount):
        self.Balance += Amount
        print(f"Deposited {Amount}. New Balance: {self.Balance}")

    def Withdraw(self, Amount):
        if Amount > self.Balance:
            print("Insufficient funds")
        else:
            self.Balance -= Amount
            print(f"Withdrew {Amount}. New Balance: {self.Balance}")

    def CalculateInterest(self, Years):
        Interest = (self.Balance * BankAccount.ROI * Years) / 100
        print(f"Interest for {Years} years: {Interest}")

obj1 = BankAccount("Alice", 1000)
obj1.Display()
obj1.Deposit(500)
obj1.Withdraw(200)
obj1.CalculateInterest(2)   



