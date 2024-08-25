#	main.py

'''
Create an Object-Oriented Python console program which does the following:

https://www.w3schools.com/python/python_lists_methods.asp

1.	Uses one or more lists to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.0)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                     hoursWorked * hourlyRate
		  Employees get overtime (time and one-half) for hours > 40
	g.	Utilize the following Python List Methods to:
		1.	append()		      Adds an employee at the end of the list(s)
		2.	clear()			      Removes all employees from the list(s)
		3.	copy()			      Creates a copy of the employee list(s)
		4.	count()			      Returns the number of employees in the list(s)
		5.	index()			      Returns the index of the employee with that emp number
		6.	insert()		      Adds an employee at the specified position
		7.	pop()			      Removes the employee at the specified position
		8.	remove()		      Removes the employee with the specified employee number
		9.	reverse()		      Reverses the order of the list(s)
		10.	sort()			      Sorts the list(s)

Write each input as its own function. Use object-oriented 
programming in this program
'''

import employee    as emp
import employeeMgr as empMgr

def main():
    mgr = empMgr.EmployeeMgr()
    
    while True:
        print("\nEmployee Management System - Python Lists")
        print("1. Add Employee")
        print("2. Clear Employees")
        print("3. Copy Employees")
        print("4. Count Employees")
        print("5. Get Employee Index")
        print("6. Insert Employee")
        print("7. Pop Employee")
        print("8. Remove Employee")
        print("9. Reverse Employees")
        print("10. Sort Employees")
        print("11. Display Employees")
        print("12. Exit")
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':           #   Add new employee
                empNumber     = int(input("Enter employee number: "))
                firstName     = input("Enter first name: ")
                lastName      = input("Enter last name: ")
                hoursWorked   = float(input("Enter hours worked: "))
                hourlyRate    = float(input("Enter hourly rate: "))
                mgr.addEmployee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
                print(f"\nEmployee added")
            elif choice == '2':         #   Clear employee list
                mgr.clearEmployees()
                print(f"\nEmployee List Has Been Cleared")
            elif choice == '3':         #   Copy names from employee list
                copiedList = mgr.copyEmployees()
                print(f"\nCopied list: {[f'{emp.firstName} {emp.lastName}' for emp in copiedList]}")
            elif choice == '4':         #   Employee list count
                print(f"\nCurrent number of employees: {mgr.countEmployees()}")
            elif choice == '5':         #   Getting an employee index
                empNumber = int(input("\nEnter employee number: "))
                print(f"Employee index: {mgr.getEmployeeIndex(empNumber)}")
            elif choice == '6':         #   Inserting new employee
                position     = int(input("Enter position to insert: "))
                empNumber    = int(input("Enter employee number: "))
                firstName    = input("Enter first name: ")
                lastName     = input("Enter last name: ")
                hoursWorked  = float(input("Enter hours worked: "))
                hourlyRate   = float(input("Enter hourly rate: "))
                mgr.insertEmployee(position, empNumber, firstName, lastName, hoursWorked, hourlyRate)
                print(f"Employee Inserted")
            elif choice == '7':         #   Employee pop
                position = int(input("\nEnter position to pop: "))
                emp = mgr.popEmployee(position)
                print(f"Popped employee: {emp.firstName} {emp.lastName}")
            elif choice == '8':         #   Employee remove
                empNumber = int(input("\nEnter employee number to remove: "))
                mgr.removeEmployee(empNumber)
                print("Employee Removed")
            elif choice == '9':         #   Reverse employee list
                mgr.reverseEmployees()
                print(f"\nReversed Employee List:")
                for emp in mgr.employees:
                    print(f"Emp#: {emp.empNumber}, Name: {emp.firstName} {emp.lastName}, Hours: {emp.hoursWorked}, Rate: {emp.hourlyRate}, Gross Pay: {emp.grossPay}")
            elif choice == '10':        #   Sorting by any field in asc or desc order
                keyChoice = input("\nSort by (1: empNumber, 2: firstName, 3: lastName, 4: hoursWorked, 5: hourlyRate, 6: grossPay): ")
                reverse = input("Sort in descending order? (y/n): ") == 'y'
                keyDict = {
                      '1': lambda emp: emp.empNumber,
                      '2': lambda emp: emp.firstName,
                      '3': lambda emp: emp.lastName,
                      '4': lambda emp: emp.hoursWorked,
                      '5': lambda emp: emp.hourlyRate,
                      '6': lambda emp: emp.grossPay,
                  }
                mgr.sortEmployees(key=keyDict[keyChoice], reverse=reverse)
                print("\nSorted Employee List:")
                for emp in mgr.employees:
                    print(f"Emp#: {emp.empNumber}, Name: {emp.firstName} {emp.lastName}, Hours: {emp.hoursWorked}, Rate: {emp.hourlyRate}, Gross Pay: {emp.grossPay}")
            elif choice == '11':        #   Display employee list
                print("\n")
                for emp in mgr.employees:
                    print(f"Emp#: {emp.empNumber}, Name: {emp.firstName} {emp.lastName}, Hours: {emp.hoursWorked}, Rate: {emp.hourlyRate}, Gross Pay: {emp.grossPay}")
            elif choice == '12':        #   Exiting program normally
                print("\nNormal Program Termination")
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()