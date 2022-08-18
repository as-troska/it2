class Account(): 
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorect password!")
            return None
        
        if amountToDeposit < 0:
            print("You can not deposit a negative amount")
            return None

        self.balance = self.balance + amountToDeposit

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry, incorrect password!")
            return None

        if amountToWithdraw < 0:
            print("You can not withdraw a negaitve amount")
            return None

        if amountToWithdraw > self.balance:
            print("You can not withdraw more than you have in your account!")

        self.balance = self.balance - amountToWithdraw

    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password!")
            return None
        
        return self.balance

    def show(self):
        print()
        print('         Name:', self.name)
        print('         Balance: ', self.balance)
        print('         Password: ', self.password)
        print()

trond = Account("Trond", 10000, "abc")
trond.deposit(25250, "abc")
trond.withdraw(250, "abc")

trond.show()