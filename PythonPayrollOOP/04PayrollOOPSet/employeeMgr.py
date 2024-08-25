import employee as emp

class EmployeeMgr:
  def __init__(self):
    self.employees = set()
  
  def addEmployee(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
    employee = emp.Employee(empNumber, firstName, lastName, hoursWorked, hourlyRate)
    self.employees.add(employee)
  
  def clearEmployees(self):
    self.employees.clear()
  
  def copyEmployees(self):
    return self.employees.copy()
  
  def differenceEmployees(self, otherSet):
    return self.employees.difference(otherSet)
  
  def difference_updateEmployees(self, otherSet):
    return self.employees.difference_update(otherSet)
  
  def discardEmployee(self, empNumber):
        employee = emp.Employee(empNumber, "", "", 0, 0)
        self.employees.discard(employee)
    
  def intersectionEmployees(self, otherSet):
      return self.employees.intersection(otherSet)
  
  def intersection_updateEmployees(self, otherSet):
      self.employees.intersection_update(otherSet)
  
  def isdisjointEmployees(self, otherSet):
      return self.employees.isdisjoint(otherSet)
  
  def issubsetEmployees(self, otherSet):
      return self.employees.issubset(otherSet)
  
  def issupersetEmployees(self, otherSet):
      return self.employees.issuperset(otherSet)
  
  def popEmployee(self):
      return self.employees.pop()
  
  def removeEmployee(self, empNumber):
      employee = emp.Employee(empNumber, "", "", 0, 0)
      self.employees.remove(employee)
  
  def symmetric_differenceEmployees(self, otherSet):
      return self.employees.symmetric_difference(otherSet)
  
  def symmetric_difference_updateEmployees(self, otherSet):
      self.employees.symmetric_difference_update(otherSet)
  
  def unionEmployees(self, otherSet):
      return self.employees.union(otherSet)
  
  def updateEmployees(self, otherSet):
      self.employees.update(otherSet)
  
  def displayEmployees(self):
      for emp in self.employees:
          print(emp)
  