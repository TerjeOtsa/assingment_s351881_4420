# Base Class: BankAccount
class BankAccount:
    def __init__(self, account_holder):
        """
        Initializes a bank account with the account holder's name and 
        sets the balance to 0 by default.
        """
        self.account_holder = account_holder
        self.balance = 0  # Initial balance is set to zero

    def deposit(self, amount):
        """
        Deposits a amount into the account.
        Only positive amounts are allowed for deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if there are 
        sufficient funds available. If not, an insufficient funds message is printed.

        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds available.")

    def account_info(self):
        """
        Provides the account holder's information including their name and 
        current balance.

        Returns:
            A string containing the account holder's name and current balance.
        """
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


# Derived Class: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate=0.02):
        """
        Initializes a savings account with an interest rate.
        Inherits the basic attributes from BankAccount and adds interest_rate.
        """
        super().__init__(account_holder)  # Initialize using BankAccount constructor
        self.interest_rate = interest_rate  # Default interest rate is 2%

    def apply_interest(self):
        """
        Applies interest to the current balance. The interest is calculated 
        by multiplying the balance by the interest rate and then added to the balance.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ${interest:.2f} applied at a rate of {self.interest_rate * 100}%.")


# Derived Class: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, transaction_fee=1):
        """
        Initializes a checking account with a transaction fee.
        Inherits basic attributes from BankAccount and adds a transaction fee for withdrawals.
        """
        super().__init__(account_holder)  # Initialize using BankAccount constructor
        self.transaction_fee = transaction_fee  # Default transaction fee is $1

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account while considering the 
        transaction fee. If there are sufficient funds, the withdrawal is processed.
        Otherwise, an insufficient funds message is displayed.
        """
        total_amount = amount + self.transaction_fee  # Include the transaction fee in total withdrawal
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"${amount} withdrawn successfully, with a ${self.transaction_fee} fee.")
        else:
            print("Insufficient funds including the transaction fee.")


# Testing the Class Hierarchy

# Testing the base class BankAccount
print("Testing Base Class - BankAccount")
account = BankAccount("John Doe")
account.deposit(500)  # Deposit $500
account.withdraw(200)  # Withdraw $200
print(account.account_info())  # Expected: Account Holder: John Doe, Balance: $300.00
print()

# Testing the derived class SavingsAccount
print("Testing Derived Class - SavingsAccount")
savings = SavingsAccount("Jane Doe", 0.03)  # Create a SavingsAccount with 3% interest
savings.deposit(1000)  # Deposit $1000
savings.apply_interest()  # Apply interest (3%)
print(savings.account_info())  # Expected: Account Holder: Jane Doe, Balance: $1030.00
print()

# Testing the derived class CheckingAccount
print("Testing Derived Class - CheckingAccount")
checking = CheckingAccount("Sam Smith", 1.5)  # Create a CheckingAccount with $1.5 transaction fee
checking.deposit(500)  # Deposit $500
checking.withdraw(100)  # Withdraw $100 with $1.5 fee
print(checking.account_info())  # Expected: Account Holder: Sam Smith, Balance: $398.50
