# parse file with list comprehension

open = open("data.txt","r")

output = [i for i in open if "file" in i]

print(output)


# calling a list comprehension with a function
def x(a):
    return a*2

y = [x(a) for a in range(10) if a%2==0]
print(y)