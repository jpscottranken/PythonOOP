#	Python Tuple OOP Program

'''
Create an Object-Oriented Python console program which does the following:

1.	Uses one or more tuples to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.00)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                       hoursWorked * hourlyRate
		  Employees get overtime (time and one-half) for hours > 40
	g.	Utilize the following Python Tuple Methods to:
			1.	count()		       Returns the number of times a specified value 
            				       occurs in a tuple
			2.	index()		       Searches the tuple for a specified value and 
            				       returns the of where it was found

Write each input as its own function. Use object-oriented 
programming in this program
'''

import employeeMgr as empMgr

def main():
    mgr = empMgr.EmployeeMgr()
    
    while True:
        print("\nEmployee Management System - Python Tuples")
        print("1. Add Employee")
        print("2. Count Employees by Number")
        print("3. Get Employee Index")
        print("4. Display Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                empNumber     = int(input("Enter employee number: "))
                firstName     = input("Enter first name: ")
                lastName      = input("Enter last name: ")
                hoursWorked   = float(input("Enter hours worked: "))
                hourlyRate    = float(input("Enter hourly rate: "))
                mgr.addEmployee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
            elif choice == '2':
                empNumber = int(input("Enter employee number to count: "))
                count = mgr.countEmployees(empNumber)
                print(f"\nNumber of employees with number {empNumber}: {count}")
            elif choice == '3':
                empNumber = int(input("Enter employee number to find: "))
                index = mgr.getEmployeeIndex(empNumber)
                print(f"\nEmployee index: {index}")
            elif choice == '4':
                mgr.displayEmployees()
            elif choice == '5':
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
