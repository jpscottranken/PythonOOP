import account as acct

class Bank:
  def __init__(self):
    self.accounts = {}

  def createAccount(self, accountNumber, firstName, lastName, balance):
    # Check to see if accountNumber currently exists.
    # If it does, print out an error message.
    if (accountNumber in self.accounts):
      print(f"\nSorry. That Account Number Already Exists.")
    else:
      # Create new account using this accountNumber
      account = acct.Account(accountNumber, firstName, lastName, balance)
      self.accounts[accountNumber] = account
      print(f"\nAccount Successfully Created For {firstName} {lastName}")
  
  def getAccount(self, accountNumber):
    # Return the account based off of the accountNumber inputted
    return self.accounts.get(accountNumber)
  
  # Display all accounts
  def displayAllAccounts(self):
    if self.accounts:
      for account in self.accounts.values():
        print(account)
    else:
      print(f"\nNo Accounts Current Exist.")