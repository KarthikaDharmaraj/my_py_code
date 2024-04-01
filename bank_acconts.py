class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,amount,acc_name) -> None:
        self.balance=amount
        self.name=acc_name
        print(f"\n Account '{self.name}' created.\n Balance = ${self.balance:.2f}")

    def getbalance(self):
        print(f"\n Account '{self.name}' balance= ${self.balance} ")

    def deposite(self,amount):
        self.balance=self.balance+amount
        self.getbalance()

    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n sorry Account '{self.name}' only has a balance of {self.balance} ")
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("\n Withdraw completed")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self,amount,account):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            account.deposite(amount)
            print("Transaction complete")
            self.getbalance()
        except BalanceException as error:
            print(f"\n Transfer interrupted : {error}")

