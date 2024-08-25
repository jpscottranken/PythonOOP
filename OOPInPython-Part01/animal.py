'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Animal:
    def sound(self):    # Method
        print('Generic sound')

class Dog(Animal):      # "Inheritance" Dog class inherit from Animal class
    def sound(self):    # overriding the sound method
        print('The Dog Says Bark!')

class Cat(Animal):      # "Inheritance" Cat class inherit from Animal class
    def sound(self):    # overriding the sound method
        print('The Cat Says Meow!')

class Cow(Animal):      # "Inheritance" Cow class inherit from Animal class
    def sound(self):    # overriding the sound method
        print('The Cow Says Moo!')

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()