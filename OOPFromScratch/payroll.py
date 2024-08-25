import employee         as emp
import hourlyWorker     as hw
import pieceWorker      as pw
import salariedWorker   as sw
import commissionWorker as cw

class Payroll:
  def __init__(self):
    # Initialize each final gross pay counter to 0.00
    self.totalHourlyWorkerGrossPay      = 0.00
    self.totalPieceWorkerGrossPay       = 0.00
    self.totalSalariedWorkerGrossPay    = 0.00
    self.totalCommissionWorkerGrossPay  = 0.00

  def processPayroll(self, employees):
    for employee in employees:
      # Calculate the gross pay
      grossPay = employee.calculateGrossPay()

      # Increment the appropriate total counter
      # with the just calculated gross pay.
      if isinstance(employee, hw.HourlyWorker):
        self.totalHourlyWorkerGrossPay     += grossPay
      elif isinstance(employee, pw.PieceWorker):
        self.totalPieceWorkerGrossPay      += grossPay
      elif isinstance(employee, sw.SalariedWorker):
        self.totalSalariedWorkerGrossPay   += grossPay
      elif isinstance(employee, cw.CommissionWorker):
        self.totalCommissionWorkerGrossPay += grossPay
  
  def displayTotals(self):
    totalPayroll = 0.0

    print(f"Total HourlyWorker     Gross Pay: ${self.totalHourlyWorkerGrossPay: .2f}")
    print(f"Total PieceWorker      Gross Pay: ${self.totalPieceWorkerGrossPay: .2f}")
    print(f"Total SalariedWorker   Gross Pay: ${self.totalSalariedWorkerGrossPay: .2f}")
    print(f"Total CommissionWorker Gross Pay: ${self.totalCommissionWorkerGrossPay: .2f}")
    
    totalPayroll = self.totalHourlyWorkerGrossPay + \
                   self.totalPieceWorkerGrossPay  + \
                   self.totalSalariedWorkerGrossPay + \
                   self.totalCommissionWorkerGrossPay
    print(f"Total Payroll: ${totalPayroll: .2f}")
    