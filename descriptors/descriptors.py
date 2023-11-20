# Descriptors are created to manage the attribute of different classes which use the object as reference
# provide a way to write reusable code to share between classes
# Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and super().
# They are used throughout Python itself. 
# Descriptors simplify the underlying C code and offer a flexible set of new tools for everyday Python programs.
# Descriptors are the interface for the __get__(), __set__(), __delete__()
# to intialize a descriptor: decr.__method__(self, obj, type=None)-> value
# https://docs.python.org/3/howto/descriptor.html#:~:text=Descriptors%20are%20a%20powerful%2C%20general,tools%20for%20everyday%20Python%20programs.
# Descriptor having binding behavior. Meaning, and engineer and define behavior and bind that behavior to a given properity
# Can be defined as two types: data (read and write) and non-data (read) 
# Are defined to a class not an instance of the class
# important terminologies 
# self:instance of the decriptor that is created
# object: object the descriptor is attached to
# type: type of the object the descriptor is attached to 
# get: access the attribute returns the value of the attribute. Can raise the attribute error exception if the attribute isn't available
# set: sets a value of the attribute. It doesn't return anything. Can raise the attribute error exception
# delete:delete operation on an attribute
# value: the value of the attribute

# I would more than likely write the getters and setters directly into my class. 
# However, this code is just practice and not meant for production use.  
class Descriptors: 
    def __init__(self):
        self.__bmi = 0
    
    def __get__(self, instance, owner):
        return self.__bmi
    
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else: 
            raise TypeError("BMI can only be an int")
        
        if value < 0:
            raise ValueError("BMI can never be less then 0")
        
        self.__bmi = value
        
    def __delete__(self, instance):
        del self._bmi
        
        
class Person: 
     # contructor function that is called only once when the object is created
     # That means that is we run person1.name = 10, the conditions in the constructor 
     # will not catch the error. That is, if we change any class attribute after it is intially created
     # the type checking in the constructor will not catch the errors. 
    
    bmi = Descriptors() 
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi
        #  if isinstance(self.name, str):
        #      print(self.name)
        #  else:
        #      raise ValueError("Name of the person can never be an integer")
        #  if self.bmi < 0: # to catch negative values
        #      raise ValueError("BMI can not be less than 0")
     
     # string interprelation         
     
    def __str__(self):
         return "{0} age is {1} with bmi of {2}".format(self.name, self.age, self.bmi)
    
 
 
person1 = Person("John", "28", 23)
print(person1)
person2 = Person("James", "25", 48)
print(person2)
print(person1)
'''
23
James age is 25 with bmi of 23
48
James age is 25 with bmi of 48
James age is 25 with bmi of 48

We see this behavior because the descriptor is associated with the class and not the instance.
Therefore, given that we passed a new bmi parameter to the class, in the person2 variable, 
we have simply overwritten our previously passed bmi parameter. 
'''

class Person:
    def __init__(self,name):
        self._name = name
    
    def getName(self):
        print("Getting the name") 
        return self._name
    
    def setName(self, name):
        print("Setting the name: " + name)
        self._name = name

    def delName(self):
        print("Deleting the name" + "\n")
        del self._name
        
    name = property(getName, setName, delName)
    
name = Person("John")
print(name.name) # syntax is variable.property

name.name = "Price"

del name.name
#print(name.name)

# creating descriptors using classes
class descriptors:
    def __init__(self, x = ""):
        self.x = x
        
    def __get__(self, obj, objtype):
        return "{} for {}".format(self.x, self.x)

    def __set__(self, obj, x):
        if isinstance(x, str):
            self.x = x
        else:
            raise TypeError("X should be of type string")
class A(object):
    x = descriptors()

y = A()
y.x = "John"
#y.x = 12 #throws a type error
print(y.x + "\n")

# Creating descriptors using the @ property
# syntax: @property -> getter, @x.setter -> setter, @x.deleter -> delete

class NewPerson:
    def __init__(self, name):
        self._name = name
   
    @property
    def name(self):
        print("Getting the name") 
        return self._name

    @name.setter
    def name(self, name):
        print("Setting the name to: " + name)
        self._name = name
    
    @name.deleter
    def name(self):
        print("Deleting the name" + "\n")
        del self._name
  
x = NewPerson("John") 
print(x.name)
x.name  = "Price"
del x.name

# lazy properties: These are properties whose initial values are not load until they are accessed, 
# then the values are cached for later use
import random
import time

class Lazy:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__
        
    def __get__(self, obj, type = None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value): # causing the lazy property to stop working
        pass
        

class Waiting:
    @Lazy
    def wait(self):
        time.sleep(3)
        
        return 42 # cached values
    
x = Waiting()
# print(x.wait)
# print(x.wait)
# print(x.wait)

class EvenNumbers:
    def __set_value_(self, owner, value):
        self.value = value
    
    def __get__(self, obj, type = None) -> object:
        return obj.__dict__.get(self.value) or 0
    
    def __set__(self, obj, value) -> None:
        obj.__dict__[self.value] = value if value % 2 == 0 else 0
        
    

class Values:
    def __init(self):
        self.value1 = EvenNumbers()
        self.value2 = EvenNumbers()
        self.value3 = EvenNumbers()
            



        

my_values = Values()
my_values.value1 = 1 # should return a 0
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)

