import constants as c
import employee  as emp

class SalariedWorker(emp.Employee):
  def __init__(self, empNumber, firstName, lastName, salary):
    super().__init__(empNumber, firstName, lastName)

    # Range check on salary
    if not (c.MINSALARY <= salary <= c.MAXSALARY):
      raise ValueError(f"Salary Must Be Between {c.MINSALARY} And {c.MAXSALARY}")
    
    self.salary = salary

  def calculateGrossPay(self):
    self.grossPay = self.salary
    return self.grossPay