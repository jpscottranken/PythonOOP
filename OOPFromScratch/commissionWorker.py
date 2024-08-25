import constants as c
import employee  as emp

class CommissionWorker(emp.Employee):
  def __init__(self, empNumber, firstName, lastName, sales, commissionRate):
    super().__init__(empNumber, firstName, lastName)

    # Range check on sales
    if not (c.MINSALES <= sales <= c.MAXSALES):
      raise ValueError(f"Sales Must Be Between {c.MINSALES} and {c.MAXSALES}.")
    
    # Range check on commission rate
    if not (c.MINCRATE <= commissionRate <= c.MAXCRATE):
      raise ValueError(f"Commission Rate  Must Be Between {c.MINCRATE} and {c.MAXCRATE}.")
    
    self.sales          = sales
    self.commissionRate = commissionRate

  def calculateGrossPay(self):
    self.grossPay = self.sales * self.commissionRate    
    return self.grossPay
