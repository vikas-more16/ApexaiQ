"""
Simple BankAccount system with deposit, withdraw, and balance check.

Includes a custom exception InsufficientBalanceError for handling
withdrawals that exceed the account balance.
"""

class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    """
    A simple bank account class that allows deposits, withdrawals,
    and balance inquiries.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): The current balance of the account.
    """

    def __init__(self, owner, balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            owner (str): Name of the account owner.
            balance (float, optional): Initial account balance. Defaults to 0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            InsufficientBalanceError: If the withdrawal amount exceeds the current balance.
        """
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Cannot withdraw {amount}. Insufficient balance: {self.balance}"
            )
        self.balance -= amount
        print(f"Withdrawn {amount}. Remaining balance: {self.balance}")

    def check_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        print(f"{self.owner}'s account balance: {self.balance}")
        return self.balance


# Example Usage
if __name__ == "__main__":
    try:
        account = BankAccount("Vikas", 500)
        account.deposit(200)
        account.withdraw(100)
        account.withdraw(700)  # Will raise InsufficientBalanceError
    except InsufficientBalanceError as e:
        print(e)
    except ValueError as e:
        print(e)
