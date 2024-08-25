'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Animal:
    def sound(self):
        print('Generic sound')

class Dog(Animal):
    def sound(self): # overriding the sound method
        print('Bark')

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
