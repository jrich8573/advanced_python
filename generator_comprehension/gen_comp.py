# the differenc between list comps and generator comps are the generator comps use ()
# major difference is generators, unlike list (that allocate memory for the whole list) allocated memory one-by-one (generates each value)
# for each value within the list


input = [1,2,3,4,4,5,6,7,7,7]
output = (var for var in input if var%2 == 0) 
print("Output values while using generator comprehension: ", end='')
for var in output:
    print(var, end='')
    
# using the for loop prints the answer that we want. Without the for loop in the print statement the interpretor
# only returns the type of output generated. 


    
