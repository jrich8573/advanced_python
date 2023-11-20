import pandas as pd
import math
import statistics






def purmetation(x, y):
    tickets_choice = math.factorial(x)/(math.factorial(y) * math.factorial(x-y))
    return tickets_choice



def choice(x,y):
    p =  math.factorial(x)/math.factorial(x-y)
    return p


print(purmetation(10,5))
print(choice(10,5))





