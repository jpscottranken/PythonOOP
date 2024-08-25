'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Person:
    def __init__(self, name, age):
        self.__name = name      # Private attribute
        self.__age = age        # Private attribute

    def get_name(self):         # Getter method
        return self.__name

    def get_age(self):          # Getter method
        return self.__age
    
    def set_name(self, name):   # Setter method
        return name

    def set_age(self, age):     # Setter method
        return age

# Instantiate a Person object
person = Person("Jeff", 67)

# Invoke the get_name method
print(person.get_name())  # Output: Jeff

# Invoke the get_age  method
print(person.get_age())   # Output: 67

# Invoke the set_name method
print(person.set_name("Jeffrey Paul Scott"))  # Output: Jeffrey Paul Scott

# Invoke the set_age  method
print(person.set_age(68))                     # Output: 68