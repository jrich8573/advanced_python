# a dictionary comprehension is a method of transforming one dictionary into another dictionary

dict = {'a':1, 'b':2, 'c':3,'d':4}

x = dict.keys()
print(x)
# dict_keys(['a', 'b', 'c', 'd'])

y = dict.values()
print(y)
# dict_values([1, 2, 3, 4])

z = dict.items()
print(z)
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])


# doubles the value
new_dict_values = {k:v*2 for (k,v) in dict.items()}
print(new_dict_values)
# {'a': 2, 'b': 4, 'c': 6, 'd': 8}

# doubles the key
new_dict_keys = {k*2:v for (k,v) in dict.items()}
print(new_dict_keys)
# {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}



dict1 = {}

# range is does this:
# for(int i = 0; i <10; i++)
# iterates 0 - 9
for i in range(10):
    if i%2==0:
        dict1[i] = i**2
        
print(dict1)
#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#dict comprehensions save a lot of typing and the lines of code
# the code below is the exact same as the for loop above
dict2 = {i:i **2 for i in range(10) if i%2==0}
print(dict2)
#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# lambda function
feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4': 40}

#cast to a list and map the values to the calculation
cel = list(map(lambda x:(float(5)/9)*(x-32), feh.values()))

# cast to a disct and calling zip() to Iterate over several iterables in parallel, producing tuples with an item from each one.
# zip() can be use similar to transpose (https://docs.python.org/3/library/functions.html#zip)
cel_dict = dict(zip(feh.keys(), cel))
# print(cel_dict)
# {'temp1': -12.222222222222223, 'temp2': -6.666666666666667, 'temp3': -1.1111111111111112, 'temp4': 4.444444444444445}

# using dictionary comprehension
cel_dict2 = {k:(float(5)/9)*(v-32) for (k,v) in feh.items()}
# print(cel_dict2)
# {'temp1': -12.222222222222223, 'temp2': -6.666666666666667, 'temp3': -1.1111111111111112, 'temp4': 4.444444444444445}


# using condictional statement in dictionary comprehension
dict3 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

new_dict = {k:v for (k,v) in dict3.items() if v >3}
# print(new_dict)
# {'d': 4}

new_dict2 = {k:('even No' if v%2==0 else 'odd No') for (k,v) in dict3.items()}
# print(new_dict2)
# {'a': 'odd No', 'b': 'even No', 'c': 'odd No', 'd': 'even No', 'e': 'odd No', 'f': 'even No'}
new_dict3 = {k:v for (k,v) in dict3.items() if v > 3 if v%2==0}
# print(new_dict3)
#{'d': 4, 'f': 6} 

# Nested dictionary comprehension
# Should only be used if no other soltion is available

dict4 = {'one':{'a': 10}, 'two':{'b':20}}


def nested_dict(dict) -> dict:
    for (external_key, external_value) in dict.items():
        for (internal_key, internal_value) in external_value.items():
            external_value.update({internal_key: float(internal_value)}) 
       
    dict.update({external_key:external_value})
    return dict

print(nested_dict(dict4))