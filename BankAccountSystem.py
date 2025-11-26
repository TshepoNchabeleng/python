class Account:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 100
        self.deposit=0
        self.withdraw=0

    def money_deposit(self, deposit):
        if deposit < 0:
            print("can't deposit a negative amount!")

        else:
            self.balance += deposit
            self.deposit = deposit

    def money_withdrawal(self, withdraw):
        if withdraw < 0:
            print("can't withdraw a negative amount!")

        elif withdraw > self.balance :
            print("Insufficient Funds")

        else:
            self.withdraw = withdraw

    def updated_balance(self):
        self.balance = self.balance - self.withdraw

    def banking_details(self):
        print(f"Account Holder: {self.owner}")
        print("Account Number: 610674736783")
        print(f"Balance: R{self.balance}\nDeposit: +R{self.deposit}\nWithdraw: -R{self.withdraw}")
    

my_bank = Account("Tshepo Nchabeleng")
# my_bank.money_deposit()
my_bank.money_withdrawal(100)
my_bank.updated_balance()
my_bank.banking_details()