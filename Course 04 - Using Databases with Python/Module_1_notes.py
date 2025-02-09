'''
Video: 13.8
Topic: Unicode Characters and Strings
'''

'''
• The ord() function tells us the numeric value of a simple ASCII character.
'''

print(ord('S'))
# Output: 83
print(ord('e'))
# Output: 101
print(ord('\n'))
# Output: 10

'''
• Unicode is this universal code for hundreds of millions of different characters and hundreds of different character sets.
'''

'''
• In Python 3, all the strings internally are Unicode. Not UTF-8, not UTF-16, not UTF-32.
'''

'''
$ Python Strings to Bytes:
--------------------------
• When we talk to an external resource like a network socket we send bytes, so we need to encode Python 3 strings into a given character encoding.

• When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string.

For example: An HTTP Request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt/1.0\n\n'.encode()

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ):
        break
    mystring = data.decode()
    print(mystring)
mysock.close()
'''





#======================================





'''
Video: 14.2
Topic: Our First Class and Object
'''

'''
The __init__ function is a specially name function.

The double underscore that starts and ends the function name is a way that Python knows that this function has special meaning.

That's a specially named method or you can say it's the constructor method.

** Lastly, self is the alias to the instance itself. 

** Moreover, self in Python are used to refer to the current object instance.

$ Constructor:
==============
• The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created.

• In object oriented programming, a constructor in a class is a special block of statements called when an object is created
'''
'''
# For Example: 
class PartyAnimal:
    def __init__(self):
        self.x = 0
    
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal() # So this is the way you create an object or instance of the class PartyAnimal.

an.party() # Output: So far 1
an.party() # Output: So far 2
an.party() # Output: So far 3

print(dir(an))
'''
'''
Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']

dir() method tells us what capabilities are in the object. 

In this case they are part, and x.
'''





#======================================





'''
Video: 14.3
Topic: Object Life Cycle
'''
'''
$ Many Instances:
=================
• We can create lots of objects- the class is the template for the object
• We can store each distinct object in its own variable
• We call this having multiple instances of the same class
• Each instance has its own copy of the instance variables
'''
# For Example:
class PartyAnimal:
    
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "Constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "Party count", self.x)

s = PartyAnimal("Sally")
# Output: Sally Constructed
s.party()
# Output: Sally Party count 1

j = PartyAnimal("Jim")
# Output: Jim Constructed
j.party()
# Output: Sally Party count 1

s.party()
# Output: Sally Party count 2





#======================================





'''
Video: 14.4
Topic: Object Inheritance
'''
'''
$ Inheritance:
=================
• When we make a new class - we can reuse an existing class and inherit all the capabilities of an existing class and then add our own little bit to make our new class.
• Another form of store and reuse
• Write once - reuse many times
• The new class (child) has all the capabilities of the old class (parent) - and then some more
'''

'''
$ Terminology: Inheritance
==========================
• ‘Subclasses’ are more specialized versions of a class, which inherit attributes and behaviors from their parent classes, and can introduce their own.
'''




class Cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def move(self):
        print('The Cars can move at high speed.')

class EVs(Cars):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
# So this part in the child class is a gesture to let python know that the child class must have access to everything from the parent class. 
    
    def selfdriving(self):
        print('EVs can drive autonomously')

toyota = Cars("Toyota", "Hilux", "2023")
bmw = Cars("BMW", "M4", "2024")
tesla = EVs("Tesla", "Cybertaxi", "2025")

tesla.selfdriving() # Output: EVs can drive autonomously
print(tesla.year) # Output: 2025
tesla.move() # Output: The Cars can move at high speed.
