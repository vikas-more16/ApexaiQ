"""
Simple BankAccount system with deposit, withdraw, and balance check.

Includes a custom exception InsufficientBalanceError for handling
withdrawals that exceed the account balance.

Classes:
- InsufficientBalanceError: Raised when balance is insufficient.
- BankAccount: Handles deposits, withdrawals, and balance checking.
"""


#  Custom exception for insufficient balance
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Cannot withdraw {amount}. Insufficient balance: {self.balance}")
        self.balance -= amount
        print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")
        return self.balance


# Example Usage
try:
    account = BankAccount("Vikas", 500)
    account.deposit(200)
    account.withdraw(100)
    account.withdraw(700)  # Will raise InsufficientBalanceError
except InsufficientBalanceError as e:
    print(e)
