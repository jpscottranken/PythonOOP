#   Program constants
MINHOURS =  0.00
MAXHOURS = 84.00
MINHRATE =  0.00
MAXHRATE = 99.99
MAXNONOT = 40.00
OVERRATE =  1.50

class Employee:
    def __init__(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
        if not firstName or not lastName:
            raise ValueError("First name and last name cannot be empty.")
        if not (MINHOURS <= hoursWorked <= MAXHOURS):
            raise ValueError(f"Hours worked must be between {MINHOURS} and {MAXHOURS}.")
        if not (MINHRATE <= hourlyRate <= MAXHRATE):
            raise ValueError(f"Hourly rate must be between {MINHRATE} and {MAXHRATE}.")
        
        self.empNumber    = empNumber
        self.firstName    = firstName
        self.lastName     = lastName
        self.hoursWorked  = hoursWorked
        self.hourlyRate   = hourlyRate
    
    @property
    def grossPay(self):
        if self.hoursWorked <= MAXNONOT:
            return self.hoursWorked * self.hourlyRate
        else:
            return (MAXNONOT * self.hourlyRate) + ((self.hoursWorked - MAXNONOT) * self.hourlyRate * OVERRATE)
    
    def to_tuple(self):
        return (self.empNumber, self.firstName, self.lastName, self.hoursWorked, self.hourlyRate, self.grossPay)
