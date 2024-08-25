'''
	Create a Python Banking System Program From Scratch.
	
	There will be the following classes:

	BankAccount				-	The superclass of all other classes.
								      This will be an abstract class.
	
	CheckingAccount   -	Child of BankAccount.
								      All checking accounts must have a
								      minimum balance of $100.00.
	
	SavingsAccount    -	Child of BankAccount
								      All savings accounts must have a.
								      minimum balance of $25.00.

	ChristmasClubAccount	-	Child of BankAccount
								      All Christmas Club accounts must have a
								      minimum balance of $10.00

	Persons should be able to do the following for any type of account:
	
	1.	Check balance.
	2.	Deposit money  into that account.
	3.	Withdraw money from that account.
	4.	Transfer money between accounts.
	5.	Open any type of new Checking, Savings, or Christmas Club account.

	Create objects of each account class (except for BankAccount).
	
	Show examples of checking balance, depositing, and withdrawing
	with each type of account.
	
Explanation:
============
1.	BankAccount (Abstract Class):

Acts as the base class for all types of bank accounts.
Defines abstract methods (checkBalance, deposit, withdraw) that 
must be implemented by subclasses.

Implements a transfer method to transfer funds between accounts.

2.	CheckingAccount:

Inherits from BankAccount.

Enforces a minimum balance of $100.00.

3.	SavingsAccount:

Inherits from BankAccount.

Enforces a minimum balance of $25.00.

4.	ChristmasClubAccount:

Inherits from BankAccount.

Enforces a minimum balance of $10.00.

Examples:
=========
Objects for each child account type are created/instantiated.

Examples will be provided to check balances, deposit,
withdraw, and transfer money between accounts.	
'''

import bankAccount          as ba
import checkingAccount      as ca
import savingsAccount       as sa
import christmasClubAccount as cca

# Instantiate 3 SavingsAccount Objects
checking1 = ca.CheckingAccount("Mary Smith",    1000.00)
checking2 = ca.CheckingAccount("John Johnson",  3500.00)
checking3 = ca.CheckingAccount("Kate Kramer",  10000.00)

# Instantiate 3 CheckingAccount Objects
savings1 = sa.SavingsAccount("Burt Fleming",   2000.00)
savings2 = sa.SavingsAccount("Kathy Blank",    5555.00)
savings3 = sa.SavingsAccount("Kelly Jones",    8765.00)

# Instantiate 3 ChristmasClubAccount Objects
christmasClub1 = cca.ChristmasClubAccount("Marty Kent",    5600.00)
christmasClub2 = cca.ChristmasClubAccount("Russ Jones",    9800.00)
christmasClub3 = cca.ChristmasClubAccount("Millie Capps", 12345.00)

# Examples of SavingsAccount, CheckingAccount, and
# ChristmasClubAccount checkBalance, deposit, and
# withdraw for each type of account.

print(f"\nCheckingAccount checking1 Example")
print(checking1.checkBalance())
checking1.deposit(1400.00)
print(checking1.checkBalance())
checking1.withdraw(800.00)
print(checking1.checkBalance())

print(f"\nCheckingAccount checking3 Example")
print(checking3.checkBalance())
checking3.deposit(789.00)
print(checking3.checkBalance())
checking3.withdraw(1000.00)
print(checking3.checkBalance())

print(f"\nSavingsAccount savings2 Example")
print(savings2.checkBalance())
savings2.deposit(100.00)
print(savings2.checkBalance())
savings2.withdraw(300.00)
print(savings2.checkBalance())

print(f"\nSavingsAccount savings3 Example")
print(savings3.checkBalance())
savings3.deposit(1987.00)
print(savings3.checkBalance())
savings3.withdraw(3300.00)
print(savings3.checkBalance())

print(f"\nChristmasClubAccount christmasClub1 Example")
print(christmasClub1.checkBalance())
christmasClub1.deposit(1000.00)
print(christmasClub1.checkBalance())
christmasClub1.withdraw(2000.00)
print(christmasClub1.checkBalance())

print(f"\nChristmasClubAccount christmasClub2 Example")
print(christmasClub2.checkBalance())
christmasClub2.deposit(100.00)
print(christmasClub2.checkBalance())
christmasClub2.withdraw(5000.00)
print(christmasClub2.checkBalance())
print(checking1.checkBalance())
print(christmasClub2.checkBalance())
christmasClub2.transfer(1000, checking1)
print(checking1.checkBalance())
print(christmasClub2.checkBalance())
