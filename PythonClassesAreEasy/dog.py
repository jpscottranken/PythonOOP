'''
  Taken from the following article:
  Classes in Python are very easy:
https://medium.com/@ebojacky/classes-in-python-are-very-easy-51c9df53701b
'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


# Create an instance of the Dog class (called buddy)
buddy = Dog("Buddy", 3)

# Call the bark() method of the Dog class
print(buddy.bark())  # Output: Buddy says woof!

# Print the value of the Dog name (Buddy)
print(buddy.name)    # Output: Buddy

# Print the value of the Dog age (3)
print(buddy.age)     # Output: 3


# Create an instance of the Dog class (called olive)
olive = Dog("Olive", 8)

# Print the value of the Dog's name (Olive)
print("The Name Of The Dog Is: " + olive.name)

# Print the value of the Dog's age (8)
print(f"The Age Of The Dog Is: " + str(olive.age) + " Years")

# Call the bark() method of the Dog class
print(f"The Sound The Dog Makes Is: " + olive.bark())
