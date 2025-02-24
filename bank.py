class Account:
    def __init__(self):
        self._balance = 0
#Global Variable Balance is accesible for all the methods in the class Account
    def __str__(self):
        return f"Account Balance: {self._balance}"
    @property

    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

def main():
    account = Account()
    account.deposit(100)
    account.withdraw(50)
    print(account)
    

if __name__ == "__main__":
    main()