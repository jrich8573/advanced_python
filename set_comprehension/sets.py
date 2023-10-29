# The difference betweeen list and set comprehension is the set comp uses {} vs []
# the syntax is {expression(varible) for variable in input_set[predicate][,...]}

# Question:
# we want our set comp to output only the even numbers (depuded) that exist within our input list

lst = [1,2,2,2,3,3,4,4,4,5,5,5,6,7,7,8]

# using a for loop
output = set()

for var in lst:
    if var%2 == 0:
        output.add(var)

print(output)
# {8, 2, 4, 6}

# set comprehension
output2 = {var for var in lst if  var%2 == 0}
print(output2)
# {8, 2, 4, 6}