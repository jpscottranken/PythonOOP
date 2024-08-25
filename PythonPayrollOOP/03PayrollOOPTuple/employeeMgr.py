import employee as emp

class EmployeeMgr:
    def __init__(self):
        self.employees = []
    
    def addEmployee(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
        if any(emp[0] == empNumber for emp in self.employees):
            raise ValueError("Employee number must be unique.")
        employee = emp.Employee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
        self.employees.append(employee.to_tuple())
    
    def countEmployees(self, empNumber):
        return sum(1 for emp in self.employees if emp[0] == empNumber)
    
    def getEmployeeIndex(self, empNumber):
        for index, emp in enumerate(self.employees):
            if emp[0] == empNumber:
                return index
        raise ValueError("Employee not found.")
    
    def displayEmployees(self):
        for emp in self.employees:
            print(f"\nEmp#: {emp[0]}, Name: {emp[1]} {emp[2]}, Hours: {emp[3]}, Rate: {emp[4]}, Gross Pay: {emp[5]}")
