'''
11/9/23
This is contunation of my OOP with python learning. This code comes from the Real Python (https://realpython.com/python-suoper/) lesson 
called: "Supercharge Your Classes with Python super()"

In python, super() allows us to use a tehnique called inheritance, which allows to call classes from other classes extending the Super class
into the subclass. This reduces the amount of code we have to write, enabling us to reuse code without repeatedly rewriting the same functions.

Using inheritance also links classes together, like rectangle and square that have a natural link
'''

# The super class Rectangle 
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
# The subclass Square

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length = length, width = length,**kwargs) #calls the __init__ constructor of rectangle, enabling sqaure to inherit recantagle 
        
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
    

# test our code
# print(Square(4).area()) # 16
# print(Cube(3).volume()) # 27

'''
Multiple inheritace

Python supports multiple inheritiance, in which a subclass can inherit frok multiple 
superclasses that don't necessarily inherit from each other. This know as sibling classes 
'''


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)
        
    def tri_area(self):
        return 0.5 * self.base * self.height
    
# in this form, RightPyramid doesn't use the inheritatance from both class.     
# Furthermore, it throws an error when running this line of code # print(RightPyramid(2,4).area()) 
'''
Traceback (most recent call last):
  File "/Users/jasonrich/code/python/oop/using_super.py", line 70, in <module>
    print(RightPyramid(2,4).area()) 
          ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jasonrich/code/python/oop/using_super.py", line 66, in area
    base_area = super().area() #calls the Square constructor, which calls the Rectangle area function
                ^^^^^^^^^^^^^^
  File "/Users/jasonrich/code/python/oop/using_super.py", line 58, in area
    return 0.5 * self.base * self.height
                             ^^^^^^^^^^^
AttributeError: 'RightPyramid' object has no attribute 'height'
'''
class RightPyramid(Square, Triangle): # moved Square into the first arg and Triangle to the 2nd
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base = base, **kwargs) # this line to change the signatre and how MRO searches our classes
        
    def area(self):
        base_area = super().area() #calls the Square constructor, which calls the Rectangle area function
        perimeter = super().perimeter()  #calls the Square constructor, which calls the Rectangle perimeter function
        return 0.5 * perimeter * self.slant_height + base_area
    
    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
    
   
# print(RightPyramid(2,4).area()) 


'''
Method Resolution Order (MRO) is helpful when using super(). MRO tells python how to seach for inherited methods. 
This comes in handy when you're using super() because MRO tell you exactly where python will look for a method you're 
calling with the super() and in the what order

Every class has an .__mro__ attribute that allows us to inspect the order
'''

# MRO is called 
# print(RightPyramid.__mro__)
# (<class '__main__.RightPyramid'>, 
# <class '__main__.Triangle'>, 
# <class '__main__.Square'>, 
# <class '__main__.Rectangle'>, 
# <class 'object'>)

'''
We do have some control over how MRO search our classes, by change the signature of the methods being searched
See above
'''

pyramid = RightPyramid(base = 2,slant_height = 4)
print(pyramid.area()) 
print(pyramid.area_2())

