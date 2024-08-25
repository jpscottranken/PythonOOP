import bankAccount as ba

class ChristmasClubAccount(ba.BankAccount):
  MINIMUMBALANCE = 10.00

  # Constructor
  def __init__(self, accountHolder, balance):
    if (balance < ChristmasClubAccount.MINIMUMBALANCE):
      raise ValueError(f"\nMinimum Balance For A Christmas Club Account Is ${ChristmasClubAccount.MINIMUMBALANCE}")
    
    # Call the __init__ method of the BankAccount class
    super().__init__(accountHolder, balance)

  def checkBalance(self):
    return (f"The Christmas Club Account Balance For {self.accountHolder} is ${self.balance:.2f}")
  
  def deposit(self, amount):
    # Verify that amount to be deposited is positive
    if (amount > 0):
      self.balance += amount
      print(f"Deposited ${amount:.2f} into {self.accountHolder} Christmas Club Account.")
    else:
      print("\nYou Cannot Deposit <= 0")
  
  def withdraw(self, amount):
    tempValue = amount 
    # Verify that amount to be deposited is positive
    if (amount > 0):
      if (self.balance - tempValue < ChristmasClubAccount.MINIMUMBALANCE):
        print(f"\nWithdraw Amount Failed. Would Leave < MINIMUM BALANCE.")
      else:
        self.balance -= amount
        print(f"Withdraw ${amount:.2f} from {self.accountHolder} Christmas Club Account.")
    else:
      print("\nYou Cannot Withdraw <= 0")
