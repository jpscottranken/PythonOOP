class Employee:
  def __init__(self, empNumber, firstName, lastName):
    if not (empNumber):
      raise ValueError("Employee Number Cannot Be Empty!")
    if not (firstName):
      raise ValueError("First Name Cannot Be Empty!")
    if not (lastName):
      raise ValueError("Last  Name Cannot Be Empty!")
    
    self.empNumber  = empNumber
    self.firstName  = firstName
    self.lastName   = lastName
    self.grossPay   = 0.00

  def calculateGrossPay(self):
    raise NotImplementedError("The superclass cannot implement this method.\nRather the method must be implemented by the subclasses.")
    