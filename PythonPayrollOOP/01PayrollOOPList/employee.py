#   Program constants
MINHOURS =  0.00
MAXHOURS = 84.00
MINHRATE =  0.00
MAXHRATE = 99.99
MAXNONOT = 40.00
OVERRATE =  1.50

class Employee:
    def __init__(self, empNumber, firstName, lastName, hoursWorked, hourlyRate):
        if not empNumber:
            raise ValueError("Employee Number cannot be empty.")
        if not firstName or not lastName:
            raise ValueError("First name and last name cannot be empty.")
        if not (MINHOURS <= hoursWorked <= MAXHOURS):
            raise ValueError("Hours worked must be between 0.0 and 84.0.")
        if not (MINHRATE <= hourlyRate <= MAXHRATE):
            raise ValueError("Hourly rate must be between 0.0 and 99.99.")
        
        self.empNumber    = empNumber
        self.firstName    = firstName
        self.lastName     = lastName
        self.hoursWorked  = hoursWorked
        self.hourlyRate   = hourlyRate
    
    #   https://www.programiz.com/python-programming/property
    @property
    def grossPay(self):
        if self.hoursWorked <= MAXNONOT:            #   No OT worked
            return self.hoursWorked * self.hourlyRate
        else:                                       #   OT worked
            return (MAXNONOT * self.hourlyRate) + \
                    ((self.hoursWorked - MAXNONOT) * \
                     self.hourlyRate * OVERRATE)
