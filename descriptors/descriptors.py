# Descriptors are created to manage the attribute of different classes which use the object as reference
# provide a way to write reusable code to share between classes
# Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static methods, class methods, and super() . They are used throughout Python itself. 
# Descriptors simplify the underlying C code and offer a flexible set of new tools for everyday Python programs.
# Descriptors are the interface for the __get__(), __set__(), __delete__()
# to intialize a descriptor: decr.__method__(self, obj, type=None)-> value
# https://docs.python.org/3/howto/descriptor.html#:~:text=Descriptors%20are%20a%20powerful%2C%20general,tools%20for%20everyday%20Python%20programs.
# Descriptor having binding behavior. Meaning, and engineer and define behavior and bind that behavior to a given properity
# Can be defined as two types: data (read and write) and non-data (read) 
# Are defined to a class not an instance of the class
