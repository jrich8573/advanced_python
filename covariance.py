import pandas as pd
import math
import statistics


housing = pd.DataFrame({'house_price':[2, 4, 6, 12], 'houses_sold':[1000, 800, 600, 400]})


# n = len(housing['house_price'])
# print(n)

# function to calculate a sample convariance

# def sample_convariance(x:pd.DataFrame, N) -> int:
#     for index, data in x.items():
#         data = pd.DataFrame({'x_i': x['house_price'] - statistics.mean( x['house_price']), 'y_i':x['houses_sold']- statistics.mean(x['houses_sold'])})
#         return (data.astype(int).sum()/(N-1))
# 



def purmetation(x, y) -> int:
    tickets_choice = math.factorial(x)/(math.factorial(y) * math.factorial(x-y))
    return tickets_choice



def choice(x,y) -> int:
    p =  math.factorial(x)/math.factorial(x-y)
    return p

# print(sample_convariance(housing,n))
#print(housing.cov())
print(purmetation(10,5))
print(choice(10,5))


text = "WORKPLACE SEXUAL HARASSMENT IN THE “ME TOO” ERA: THE UNFORESEEN CONSEQUENCES OF CONFIDENTIAL SETTLEMENT AGREEMENTS"
print(text.lower())


