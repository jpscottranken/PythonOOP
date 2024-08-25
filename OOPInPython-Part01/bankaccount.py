'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Abstracted data

    def deposit(self, amount):
        self.__balance += amount  # Abstracted control

    def withdrawal(self, amount):
        self.__balance -= amount  # Abstracted control

    def get_balance(self):
        return self.__balance     # Abstracted interface

# Instantiate a BankAccount object
ba1 = BankAccount(1000)

# Print initial balance
print(f"Initial Balance: ${ba1.get_balance()}")

# Deposit 567 into ba1
ba1.deposit(567)

# Print new, updated balance
print(f"Updated Balance After Deposit: ${ba1.get_balance()}")

# Withdraw 800 from ba1
ba1.withdrawal(800)

# Print new, updated balance
print(f"Updated Balance After Withdrawal: ${ba1.get_balance()}")
