import employee as emp

class EmployeeMgr:
    def __init__(self):
        self.employees = []             #   Create empty employee list

    def addEmployee(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
        #   Verify that the employee number inputted is unique
        if any(emp.empNumber == empNumber for emp in self.employees):
            raise ValueError("Employee number must be unique.")
        
        #   Create employee object and append it to the end of the list
        employee = emp.Employee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
        self.employees.append(employee)

    def clearEmployees(self):
        self.employees.clear()

    def copyEmployees(self):
        return self.employees.copy()

    def countEmployees(self):
        return len(self.employees)

    def getEmployeeIndex(self, empNumber):
        for index, emp in enumerate(self.employees):
            if emp.empNumber == empNumber:
                return index
        #   Exception for non-existent employee number    
        raise ValueError("Employee not found.")

    def insertEmployee(self, position, empNumber, firstName, lastName, hoursWorked, hourlyRate):
        #   Verify that the employee number inputted is unique
        if any(emp.empNumber == empNumber for emp in self.employees):
            raise ValueError("Employee number must be unique.")
        employee = emp.Employee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
        self.employees.insert(position, employee)

    def popEmployee(self, position):
        return self.employees.pop(position)

    def removeEmployee(self, empNumber):
        index = self.getEmployeeIndex(empNumber)
        self.employees.pop(index)

    def reverseEmployees(self):
        print(self.employees.reverse())

    def sortEmployees(self, key=lambda emp: emp.empNumber, reverse=False):
        print(self.employees.sort(key=key, reverse=reverse))
