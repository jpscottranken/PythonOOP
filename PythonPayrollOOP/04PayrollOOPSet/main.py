# main.py

'''
Create an Object-Oriented Python console program which does the following:

https://www.w3schools.com/python/python_sets_methods.asp

1.	Uses one or more sets to create a payroll program which also demonstrates
		the following Python Set methods:

a.	add()	 							Adds an element to the set (not implemented)
b.	clear()	 						    Removes all the elements from the set
c.	copy()	 						    Returns a copy of the set
d.	difference()				        Returns a set containing the difference between two or more sets
e.	difference_update()	-=		        Removes the items in this set that are also included in another, specified set
f.	discard()	 					    Remove the specified item
g.	intersection()			&	        Returns a set, that is the intersection of two other sets
h.	intersection_update()	&=	        Removes the items in this set that are not present in other, specified set(s)
i.	isdisjoint()	 			        Returns whether two sets have a intersection or not
j.	issubset()					        <=	Returns whether another set contains this set or not
k. 	<				14				    Returns whether all items in this set is present in other, specified set(s)
l.	issuperset()				        >=	Returns whether this set contains another set or not
m. 	>								    Returns whether all items in other, specified set(s) is present in this set
n.	pop()	 							Removes an element from the set
o.	remove()	 					    Removes the specified element
p.	symmetric_difference()	^	        Returns a set with the symmetric differences of two sets
q.	symmetric_difference_update()	    ^=	Inserts the symmetric differences from this set and another
r.	union()							    |	Return a set containing the union of sets
s.	update()						    |=	Update the set with the union of this set and others

Write each input as its own function. USE object-oriented 
programming in this program
'''

import employeeMgr as empMgr

def main():
    mgr = empMgr.EmployeeMgr()
    otherSet = set ()  # Another set for demonstration purposes

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Clear Employees")
        print("3. Copy Employees")
        print("4. Difference Employees")
        print("5. Difference Update Employees")
        print("6. Discard Employee")
        print("7. Intersection Employees")
        print("8. Intersection Update Employees")
        print("9. Is Disjoint Employees")
        print("10. Is Subset Employees")
        print("11. Is Superset Employees")
        print("12. Pop Employee")
        print("13. Remove Employee")
        print("14. Symmetric Difference Employees")
        print("15. Symmetric Difference Update Employees")
        print("16. Union Employees")
        print("17. Update Employees")
        print("18. Display Employees")
        print("19. Exit")
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
                mgr.clearEmployees()
            elif choice == '3':
                copiedEmployees = mgr.copyEmployees()
                print("Copied employees:", copiedEmployees)
            elif choice == '4':
                print("Difference with other set:", mgr.differenceEmployees(otherSet))
            elif choice == '5':
                mgr.difference_updateEmployees(otherSet)
                print("Difference updated with other set.")
            elif choice == '6':
                empNumber = int(input("Enter employee number to discard: "))
                mgr.discardEmployee(empNumber)
            elif choice == '7':
                print("Intersection with other set:", mgr.intersectionEmployees(otherSet))
            elif choice == '8':
                mgr.intersection_updateEmployees(otherSet)
                print("Intersection updated with other set.")
            elif choice == '9':
                print("Is disjoint with other set:", mgr.isdisjointEmployees(otherSet))
            elif choice == '10':
                print("Is subset of other set:", mgr.issubsetEmployees(otherSet))
            elif choice == '11':
                print("Is superset of other set:", mgr.issupersetEmployees(otherSet))
            elif choice == '12':
                poppedEmployee = mgr.popEmployee()
                print("Popped employee:", poppedEmployee)
            elif choice == '13':
                empNumber = int(input("Enter employee number to remove: "))
                mgr.removeEmployee(empNumber)
            elif choice == '14':
                print("Symmetric difference with other set:", mgr.symmetric_differenceEemployees(otherSet))
            elif choice == '15':
                mgr.symmetric_difference_updateEmployees(otherSet)
                print("Symmetric difference updated with other set.")
            elif choice == '16':
                print("Union with other set:", mgr.unionEmployees(otherSet))
            elif choice == '17':
                mgr.updateEmployees(otherSet)
                print("Updated with union of other set.")
            elif choice == '18':
                mgr.displayEmployees()
            elif choice == '19':
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
