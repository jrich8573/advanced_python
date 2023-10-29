#comprehensions provide a way to write a small chunk of code to generate a sequence. 
# for types of comprehensions supported by python 
# 1. list: https://www.w3schools.com/python/python_lists_comprehension.asp
# 2. Dictionary
# 3. Set
# 4. Generator

# list comprehension generates a list: 
# syntax: 
"""
new_list = [expression(i) for i in old_list if filter(i)]
"""
# similar to a traditional for loop
"""
for items in list:
    if condition:
        expression
"""

num = [1,2,3,4,5]
squares = []

for n in num:
    #if n != 4:
   squares.append(n**2)
    
print("Squares are:", squares)

new_squares = [n**2 for n in num]

print("New Square(s) is(are):", new_squares)

# be careful to not overwrite functions with variables
list0 = [1,2,3,4,5]
list1 = [2,3,4,5,6]

# for loop version
intersection = []

for x in list0:
    for y in list1:
        if x == y:
            intersection.append(x)

print("print the intersection of lists:", intersection)


# list comperhension instersection
intersection2 = [x for x in list0 for y in list1 if x == y]


print("print the intersection of lists:", intersection2)

# list comprehension to return a tuple
# performs the Cartesian cross products
# nested list comprehension
not_common = [(x,y) for x in list0 for y in list1  if x != y]

print("Elements that not common across the lists:", not_common)

# list comprehension to iterate over string
list2 = ['Hello World', 'Java', 'Pyton', 'C']

x = [str.lower() for str in list2]

print('Print all lowercase:', x)

# squares and cubes as a tuple
multples = [(a**2, a**3) for a in list0]

print(multples)


# List comprehensions vs lamba functions
x = list(map(lambda x:x, 'Hello'))

print(x)

x = list(map(lambda x:x**2, list0))
print(x)