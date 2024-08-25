# Program constants
MINHOURS =  0.00
MAXHOURS = 84.00
MINHRATE =  0.00
MAXHRATE = 99.99
MAXNONOT = 40.00
OVERRATE =  1.50

class EmployeeMgr:
  def __init__(self):
    self.employees = {}         # Create empty employees dictionary
  
  def addEmployee(self):        # Add new employee to end of dictionary
    empNumber = int(input("Enter Unique Employee Number: "))
    if (empNumber in self.employees): # Error empNumber already exists
      print("Error: Employee number must be unique.")
      return
    
    # Input firstName
    firstName = input("Enter First Name: ").strip()
    if not (firstName):
      print(f"\nError: First name cannot be empty.")
      return
    
    # Input lastName
    lastName  = input("Enter Last  Name: ").strip()
    if not (lastName):
      print(f"\nError: Last name cannot be empty.")
      return
    
    try:
      # Input hoursWorked
      hoursWorked = float(input(f"Enter Hours Worked (0.00 - 84.00)"))
      if not (MINHOURS <= hoursWorked <= MAXHOURS):
        print(f"\nError: Hours worked must be between {MINHOURS} and {MAXHOURS}")
        return
    except ValueError:
      print(f"Error: Invalid Input For Hours Worked.")
    
    try:
      # Input hourlyRate
      hourlyRate = float(input(f"Enter Hourly Rate (0.00 - 99.99)"))
      if not (MINHRATE <= hourlyRate <= MAXHRATE):
        print(f"\nError: Hourly rate must be between {MINHRATE} and {MAXHRATE}")
        return
    except ValueError:
      print(f"Error: Invalid Input For Hourly Rate.")
    
    # Calculate grossPay
    straightTime = min(hoursWorked, MAXNONOT) * hourlyRate
    overtime     = max(hoursWorked - MAXNONOT, 0) * (hourlyRate * OVERRATE)
    grossPay     = straightTime + overtime

    # Make Dictionary entry
    self.employees[empNumber] = {
      "empNumber":    empNumber,
      "firstName":    firstName,
      "lastName":     lastName,
      "hoursWorked":  hoursWorked,
      "hourlyRate":   hourlyRate,
      "grossPay":     grossPay
    }

    print(f"\nEmployee {firstName} {lastName} added to employee list.")

  def clearEmployees(self):     # Clear employee list
    self.employees.clear()
    print(f"\nThe employee list has been cleared.")

  def copyEmployees(self):      # Copy  employee list
    copiedEmployees = self.employees.copy()
    print("Copied employee records: ", copiedEmployees)
  
  def from_keysEmployees(self): # Allow new entries
    keys    = input("Enter keys separated by commas: ").split(",")
    value   = input("Enter default value: ")
    newDict = dict.fromkeys(keys, value)
    print(f"\nNew Dictionary From Keys: ", newDict)
  
  def getEmployee(self):        # Get an employee
    empNumber = int(input("Enter Employee Number: "))
    empInfo   = self.employees.get(empNumber, "Employee Not Found")
    print("Employee Info: ", empInfo)
  
  def removeEmployee(self):     # Remove desired employee
    empNumber = int(input("Enter Employee Number: "))
    removedEmployee = self.employees.pop(empNumber, None)
    if (removedEmployee):
      print(f"\nEmployee {empNumber} was removed.")
    else:
      print(f"\nEmployee not found")

  def remove_lastEmployee(self):  # Remove last employee
    if (self.employees):
      empNumber, empInfo = self.employees.popitem()
      print(f"\nLast employee {empNumber} was removed.")
    else:
      print(f"\nNo employees found")

  def updateEmployee(self):     # Update an employee
    empNumber = int(input("Enter employee number to update: "))
    if (empNumber not in self.employees):
      print(f"\nEmployee Number Not Found.")
      return
    
    print("\nEnter the fields to update (leave blank to skip field): ")
    firstName = input("Enter new first name or <enter> to skip: ").strip()
    lastName  = input("Enter new last  name or <enter to skip>: ").strip()
    
    try:
      hoursWorked = input("Enter new hours worked  or <enter> to skip: ").strip()
      hoursWorked = float(hoursWorked) if hoursWorked else None
      if not (MINHOURS <= hoursWorked <= MAXHOURS):
        raise ValueError
    except ValueError:
      print(f"\nError. Invalid or out-of-range input for hours worked.")

    try:
      hourlyRate = input("Enter new hourlyRate  or <enter> to skip: ").strip()
      hourlyRate = float(hourlyRate) if hourlyRate else None
      if not (MINHRATE <= hourlyRate <= MAXHRATE):
        raise ValueError
    except ValueError:
      print(f"\nError. Invalid or out-of-range input for hourly rate.")
    
    updatedInfo = {}
    if firstName:                   # Update firstName if warranted
      updatedInfo["firstName"] = firstName
    if lastName:                    # Update lastName  if warranted
      updatedInfo["lastName"]  = lastName
    if hoursWorked is not None:     # Update hoursWorked if warranted
      updatedInfo["hoursWorked"]  = hoursWorked
    if hourlyRate is not None:      # Update hourlyRate  if warranted
      updatedInfo["hourlyRate"]   = hourlyRate

    # If hoursWorked and/or hourlyRate updated, update grossPay
    if "hoursWorked" in updatedInfo or "hourlyRate" in updatedInfo:
      currentInfo   = self.employees[empNumber]
      hoursWorked   = updatedInfo.get("hoursWorked", currentInfo["hoursWorked"])
      hourlyRate    = updatedInfo.get("hourlyRate",  currentInfo["hourlyRate"])
      straightTime  = min(hoursWorked, MAXNONOT) * hourlyRate
      overtime      = max(hoursWorked - MAXNONOT, 0) * (hourlyRate * OVERRATE)
      updatedInfo["grossPay"] = straightTime + overtime
    
    # Update Dictionary entry
    self.employees[empNumber].update(updatedInfo)
    print(f"\nEmployee {empNumber} has been updated.")
  
  def listEmployees(self):      # List all employees
    if self.employees:
      for empNumber, empInfo in self.employees.items():
        print(f"Employee Number: {empNumber}, Info: {empInfo}")
    else:
      print(f"\nNo employee records found.")

  def list_employee_keys(self): # List all keys
    keys = self.employees.keys()
    print("Employee Numbers: ", keys)

  def list_employee_values(self): # List all values
    values = self.employees.values()
    print("Employee Info: ", values)

  def set_defaultEmployee(self):  # Set a default employee
    empNumber = int(input("Enter employee number to set default: "))
    if (empNumber in self.employees):
      print(f"\nEmployee Already Exists.")
      return

    defaultInfo = {
      "firstName":    "UnknownFirst",
      "lastName":     "UnknownLast",
      "hoursWorked":  0.00,
      "hourlyRate":   0.00,
      "grossPay":     0.00
    }

    self.employees.setdefault(empNumber, defaultInfo)
    print("Default employee set for employee number: {empNumber}")
