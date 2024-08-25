'''
  Taken from the following article:
  Classes in Python are very easy:
https://medium.com/@ebojacky/classes-in-python-are-very-easy-51c9df53701b
'''

class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Instantiating an instance of the dog class
my_dog = Dog("Buddy", 3)

# "Getting" the value of that dog's name
print(my_dog.get_name())  # Output: Buddy

# "Setting" the value of that dog's name
my_dog.set_name("Max")

# "Getting" the value of that dog's name
print(my_dog.get_name())  # Output: Max