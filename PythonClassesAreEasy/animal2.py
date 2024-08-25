'''
  Taken from the following article:
  Classes in Python are very easy:
https://medium.com/@ebojacky/classes-in-python-are-very-easy-51c9df53701b
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class's __init__ method
        self.age = age

    def speak(self):
        return f"{self.name} says woof!"

class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)  # Call the parent class's __init__ method
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"

    def speak(self):
        return f"{self.name} says woof woof woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says meow!"

animals = [Dog("Buddy", 3), Cat("Whiskers"), Puppy("Bingo", 1, "Bone")]

for animal in animals:
    print(animal.speak())