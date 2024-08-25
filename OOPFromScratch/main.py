'''
	Create a Python Object-Oriented Program representing a payroll
	application for a company.
	
	Each employee has the following data in a parent Employee class:
	
	empNumber	-	Employee Number. Int. Must be unique.
	firstName	-	String. Cannot be empty.
	lastName	-	String. Cannot be empty.
	grossPay	-	Float. Overridden for each employee type below
	
	The company has four types of employees, each of these is a
	subclass of the Employee class:
	
	HourlyWorker		-	Has hoursWorked (range 0.00 - 84.00) and 
							      hourlyRate (range 0.00 - 99.99)

							      if hoursWorked <= 40:
								      grossPay = hoursWorked * hourlyRate

							      elif hoursWorked > 40:
								      grossPay = (hoursWorked * 40)  +
					            ((hoursWorked - 40) * hourlyRate * 1.5)
							  
	PieceWorker			-	Has numberOfPieces (range 0 - 100) and 
							      pricePerPiece (range 0.01 - 1.00)
	
							      grossPay = numberOfPieces * pricePerPiece

	SalariedWorker  -	Has salary, paid per week. Range is 0 - 10000
	
							      grossPay = salary

	CommissionWorker  -	Has sales (range 0.00 - 1000000.00) and 
							        commissionRate (range 0.01 - 0.25)

							        grossPay = sales * commissionRate

	The program may use any combination of Python Lists, Dictionaries,
	Tuples, and/or Sets as necessary.

	Also, keep track of totalHourlyWorkerGrossPay, totalPieceWorkerGrossPay,
	totalSalariedWorkerGrossPay, and totalCommissionWorkerGrossPay.
	
	Explanation:
	============
	Employee: The base class for all employees, with common attributes
	and an abstract method calculate_gross_pay.
	
	HourlyWorker, Pieceworker, SalariedWorker, CommissionWorker:
  These are subclasses of Employee, each implementing the 
  calculateGrossPay method based on their specific rules.
	
	Payroll: This class tracks the total gross pay for each type of 
	employee and processes a list of employees, calculating their 
  gross pay and updating the totals.
'''

import hourlyWorker     as hw
import pieceWorker      as pw
import salariedWorker   as sw
import commissionWorker as cw
import payroll          as pay

def main():
  employees = [
    hw.HourlyWorker(100, "John",  "Doe",   45.00, 20.00),
    hw.HourlyWorker(110, "Nancy", "Kent",  30.00, 30.00),
    hw.HourlyWorker(120, "Mary",  "Jones", 10.00, 10.00),
    hw.HourlyWorker(130, "Kelly", "Jack",  44.00, 33.00),
    hw.HourlyWorker(140, "Mark",  "Clark", 60.00, 50.00),
    hw.HourlyWorker(150, "Ben",   "Bentz", 80.00, 22.00),
    hw.HourlyWorker(160, "Kevin", "Wings", 49.00, 20.00),
    pw.PieceWorker(200, "Jane",   "Smith", 75, 0.50),
    pw.PieceWorker(210, "Mike",   "Print", 25, 0.15),
    pw.PieceWorker(220, "Tony",   "Grand", 75, 0.39),
    pw.PieceWorker(230, "Harry",  "Boyle", 10, 0.76),
    pw.PieceWorker(240, "Kent",   "Lane",  33, 0.9),
    pw.PieceWorker(250, "Marvin", "Lang",  87, 1.00),
    sw.SalariedWorker(300, "Alice",  "Johnson", 5000),
    sw.SalariedWorker(310, "Marty",  "Jackson", 7500),
    sw.SalariedWorker(320, "Brian",  "Fellows", 2500),
    sw.SalariedWorker(330, "Grace",  "Gallows", 800),
    sw.SalariedWorker(340, "Kevin",  "Jackson", 1950),
    sw.SalariedWorker(350, "Claire", "Johnson", 7654),
    cw.CommissionWorker(400, "Bob",  "Brown",   150000,  0.10),
    cw.CommissionWorker(410, "Rob",  "Green",   215000,  0.25),
    cw.CommissionWorker(420, "Dan",  "Black",    50000,  0.13),
    cw.CommissionWorker(430, "Ken",  "White",    34000,  0.08),
    cw.CommissionWorker(440, "Kari", "Jones",    91900,  0.19),
    cw.CommissionWorker(450, "Bob", "Franks",    55551,  0.04)
    ]

  payroll = pay.Payroll()
  payroll.processPayroll(employees)
  payroll.displayTotals()

if (__name__ == "__main__"):
  main()