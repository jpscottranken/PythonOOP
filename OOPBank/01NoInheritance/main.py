'''
	Create an Object-Oriented Python program in which
	Account and Bank classes will be created.
	
	The Account attributes will be:
	===============================
	accountNumber	(key)
	firstName
	lastName
	balance
	
	The Account methods will be:
	============================
	createAccount()
	deposit()
	withdraw()
	displayAccounts()
	__str__() overridden for displayAccounts

	The Bank methods will be:
	=========================
	createAccount()
	getAccount()

	In addition, create a main.py file which does the following:
	
	1.	Instantiates a Bank object
	2.	Instantiates an Account object if necessary
	3.	Sets up and implements a menu structure with:
		a. Create A New Account (assume a minimum balance of $100 always)
		b. Deposit Into  Existing Account
		c. Withdraw From Existing Account
		d. Query A Single Existing Account
		e. Exit
'''

import bank as ba

def main():
  # Instantiate a new Bank object
  bank = ba.Bank()

  while True:
    # Set up program menu
    print(f"\nOOP Banking System Menu:")
    print("1. Create A New Bank Account")
    print("2. Deposit Into An Existing Bank Account")
    print("3. Withdraw From An Existing Bank Account")
    print("4. Query A Single Existing Bank Account")
    print("5. Display All Existing Bank Accounts")
    print("6. Normal Program Termination")

    # Have user make a choice
    choice = input(f"\nPlease Enter A 1 - 6 Now: ")

    if (choice == "1"):     # Create a new bank account
      accountNumber = input(f"\nEnter Account Number: ")
      firstName     = input("Enter First Name: ")
      lastName      = input("Enter Last  Name: ")
      balance       = float(input("Enter Initial Balance: "))
      bank.createAccount(accountNumber, firstName, lastName, balance)
    elif (choice == "2"):   # Deposit into existing bank account
      accountNumber = input(f"\nEnter Account Number: ")
      account       = bank.getAccount(accountNumber)
      if (account):
        amount = float(input(f"\nEnter Amount To Deposit: "))
        account.deposit(amount)
    elif (choice == "3"):   # Withdraw from existing bank account
      accountNumber = input(f"\nEnter Account Number: ")
      account       = bank.getAccount(accountNumber)
      if (account):
        amount = float(input("Enter Amount To Withdraw: "))
        account.withdraw(amount)
    elif (choice == "4"):   # Query a single existing bank account
      accountNumber = input(f"\nEnter Account Number: ")
      account       = bank.getAccount(accountNumber)
      if (account):
        print(account)
      else:
        print(f"\nSorry. That Account Does Not Exist.")
    elif (choice == "5"):   # Query all existing bank accounts
      bank.displayAllAccounts()
    elif (choice == "6"):   # Exit program
      print(f"\nNormal Program Termination. Good Bye.")
      exit()
    else:
      print(f"\nInvalid Choice. Please Try Again.")

if (__name__ == "__main__"):
  main()