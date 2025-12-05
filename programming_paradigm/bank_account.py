class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        # print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Withdrawal amount must be positive")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            # print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            # print("Insufficient balance")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")