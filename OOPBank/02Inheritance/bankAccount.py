# https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod

class BankAccount:
  # Constructor
  def __init__(self, accountHolder, balance):
    self.accountHolder  = accountHolder
    self.balance        = balance

  @abstractmethod
  def checkBalance(self):
    pass

  @abstractmethod
  def deposit(self):
    pass

  @abstractmethod
  def withdraw(self):
    pass

  def transfer(self, amount, targetAccount):
    # Does this much money exist in the account
    if (self.balance >= amount):
      self.withdraw(amount)
      targetAccount.deposit(amount)
      print(f"\nTransferred ${amount:.2f}")# To {targetAccount}")
    else:
      print(f"\nThe Transfer Failed Due To Insufficient Funds.")