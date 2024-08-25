class Account:
  def __init__(self, accountNumber, firstName, lastName, balance):
    self.accountNumber  = accountNumber
    self.firstName      = firstName
    self.lastName       = lastName
    self.balance        = balance
  
  def deposit(self, amount):
    # You Must Input A Positive Amount For Depositing
    if (amount > 0):
      self.balance += amount    # Add amount to existing balance
      print(f"\nDeposited ${amount:.2f} into account # {self.accountNumber}.")
      print(f"Your Updated Balance Is: {self.balance:.2f}")
    else:
      print(f"\nDeposit Amount Must Be Positive!")

  def withdraw(self, amount):
    # You Must Input A Positive Amount For Withdrawing
    if (amount > 0):
      if (self.balance > amount):
        self.balance -= amount    # Withdraw amount from existing balance
        print(f"\nWithdrew ${amount:.2f} from account # {self.accountNumber}.")
        print(f"Your Updated Balance Is: {self.balance:.2f}")
      # You Cannot Withdraw More Money
      # Than You Have In Your Account
      else:
        print(f"\nInsufficient Funds For This Withdrawal.")
    else:
      print(f"\nWithdrawl Amount Must Be Positive!")

  # Override the __str__ method. This is what will print
  # when the program asks for an account object to print.
  def __str__(self):
    return (f"\nAccount Number: {self.accountNumber}\tName: {self.firstName} {self.lastName}\tBalance: ${self.balance:.2f}")
  