'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Person:
    def __init__(self, firstName, lastName, age):
      self.firstName = firstName
      self.lastName  = lastName
      self.age       = age

    def greet(self):  # Method
        print(f"Hello, {self.firstName} {self.lastName}. You are {self.age} years old!")

jeff = Person("Jeff", "Scott", 67)
jeff.greet()          # Output: Hello, Jeff Scott. You are 67 years old!