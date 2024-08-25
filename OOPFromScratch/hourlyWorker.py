import constants as c
import employee  as emp

class HourlyWorker(emp.Employee):
  def __init__(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
    super().__init__(empNumber, firstName, lastName)

    # Range check on hours worked
    if not (c.MINHOURS <= hoursWorked <= c.MAXHOURS):
      raise ValueError(f"Hours Worked Must Be Between {c.MINHOURS} and {c.MAXHOURS}.")
    
    # Range check on hourly rate
    if not (c.MINHRATE <= hourlyRate <= c.MAXHRATE):
      raise ValueError(f"Hourly Rate  Must Be Between {c.MINHRATE} and {c.MAXHRATE}.")
    
    self.hoursWorked  = hoursWorked
    self.hourlyRate   = hourlyRate

  def calculateGrossPay(self):
    if (self.hoursWorked <= c.MAXNONOT):   # No OT worked
      self.grossPay = self.hoursWorked * self.hourlyRate
    else:
      self.grossPay = (c.MAXNONOT * self.hourlyRate) + \
                      ((self.hoursWorked - c.MAXNONOT) * \
                       self.hourlyRate * c.OVERRATE)
    
    return self.grossPay
