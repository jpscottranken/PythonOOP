'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Person:
    def greet(self, name):  # Method
        print(f"Hello, {name}!")

jeff = Person()
jeff.greet("Jeff Scott")    # Output: Hello, Jeff Scott!