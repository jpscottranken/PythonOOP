# main.py

'''
Create an Object-Oriented Python console program which does the following:

https://www.w3schools.com/python/python_dictionaries_methods.asp

1.	Uses one or more dictionaries to get the following information about employees:

	a.	Employee number      (must be unique)
	b.	Employee firstName   (cannot be empty)
	c.	Employee lastName    (cannot be empty)
	d.	Employee hoursWorked (must be >= 0.00 and <= 84.0)
	e.	Employee hourlyRate  (must be >= 0.00 and <= 99.99)
	f.	For each employee,   calculate straight time (Non-OT) Gross Pay as: 
		                       hoursWorked * hourlyRate
		  										 Employees get overtime (time and one-half) for 
													 hours > 40
	g.	Utilize the following Python Dictionary Methods to:
			1.	clear()					Removes all the elements from the dictionary
			2.	copy()					Returns a copy of the dictionary
			3.	fromkeys()			Returns a dictionary with the specified keys and valueS
			4.	get()						Returns the value of the specified key
			5.	items()					Returns a list containing a tuple for each key value pair
			6.	keys()					Returns a list containing the dictionary's keys
			7.	pop()						Removes the element with the specified key
			8.	popitem()				Removes the last inserted key-value pair
			9.	setdefault()		Returns the value of the specified key. 
            							If the key does not exist: insert the key, 
                          with the specified value
			10.	update()				Updates the dictionary with the specified key-value pairs
			11.	values()				Returns a list of all the values in the dictionary

Write each input as its own function. USE object-oriented 
programming in this program
'''

import employeeMgr as empMgr

def main():
	#	Instantiate an EmployeeMgr object
	mgr = empMgr.EmployeeMgr()
  
	#	Set up a menu
	while True:
		print("\nEmployee Management System - Python Dictionaries")
		print("1. Add New Employee")
		print("2. Clear Employee List")
		print("3. Copy Employee List")
		print("4. Create Dictionary from Keys")
		print("5. Get Employee")
		print("6. Remove Employee")
		print("7. Remove Last Employee")
		print("8. Update Employee List")
		print("9. List All Employees")
		print("10. List Employee Keys")
		print("11. List Employee Values")
		print("12. Set Default Employee")
		print("13. Normal Termination Exit")
	
		choice = input("Enter 1 - 13 now please: ")

		if (choice == '1'):						#	Add new employee
			mgr.addEmployee()
		elif (choice == '2'):					#	Clear employee list
			mgr.clearEmployees()
		elif (choice == '3'):					#	Copy  employee list
			mgr.copyEmployees()
		elif (choice == '4'):				 	#	Create Dictionary from keys
			mgr.from_keysEmployees()
		elif (choice == '5'):					#	Get an employee
			mgr.getEmployee()
		elif (choice == '6'):					#	Remove employee
			mgr.removeEmployee()
		elif (choice == '7'):					#	Remove last employee
			mgr.remove_lastEmployee()
		elif (choice == '8'):					#	Update employee
			mgr.updateEmployee()
		elif (choice == '9'):					#	List all employees
			mgr.listEmployees()
		elif (choice == '10'):				#	List employee keys
			mgr.list_employee_keys()
		elif (choice == '11'):				#	List employee values
			mgr.list_employee_values()
		elif (choice == '12'):				#	Set default employee
			mgr.set_defaultEmployee()
		elif (choice == '13'):				#	Normal program termination
			print(f"\nNormal Program Termination.")
			exit()
		else:
			print(f"\nInvalid choice. Please try again.")

if __name__ == "__main__":
	main()
