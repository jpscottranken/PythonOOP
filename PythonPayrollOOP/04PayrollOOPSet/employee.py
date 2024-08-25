# Program Constants
MINHOURS =  0.00
MAXHOURS = 84.00
MINHRATE =  0.00
MAXHRATE = 99.99
MAXNONOT = 40.00
OVERRATE =  1.5

class Employee:
  def __init__(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
    if not(empNumber):
      raise ValueError(f"\nEmployee Number Cannot Be Empty.")
    if not(firstName):
      raise ValueError(f"\nFirst Name Cannot Be Empty.")
    if not(lastName):
      raise ValueError(f"\nLast  Name Cannot Be Empty.")
    if not (MINHOURS <= hoursWorked <= MAXHOURS):
      raise ValueError(f"\nHours Worked Must Be Between {MINHOURS} And {MAXHOURS}")
    if not (MINHRATE <= hourlyRate <= MAXHRATE):
      raise ValueError(f"\nHourly Rate Must Be Between {MINHRATE} And {MAXHRATE}")

    self.empNumber    = empNumber
    self.firstName    = firstName
    self.lastName     = lastName
    self.hoursWorked  = hoursWorked
    self.hourlyRate   = hourlyRate                      

  def __hash__(self):
    return hash(self.empNumber)

  def __eq__(self, other):
    return self.empNumber == other.empNumber

  def __repr__(self):
    return (f"Emp#: {self.empNumber}, Name: {self.firstName} {self.lastName}, "
            f"Hours: {self.hoursWorked}, Rate: {self.hourlyRate}")