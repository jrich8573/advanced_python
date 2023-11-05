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