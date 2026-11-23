"""
    Perform basic calculations on two numbers.
    addition +
    subtraction -
    multiplication *
    division /
    Floor division //
    Power-of **
    Return all results
    Assign results to variables (on one line, tuple)
    
    #What datatype are we returning?
"""

#TASK: Let the user specify ONE operation, perform that operation and return the result
def compute_numbers(n1, n2):
    
    #Operations
    addition = n1+n2
    subtraction = n1-n2
    multiplication = n1*n2
    division = n1/n2
    floorDiv = n1//n2
    powerOf = n1**n2
    
    


listOfNumbers = [10,2]
tupleOfNumbers = (10,2)
#add option to select calculation

result = compute_numbers(tupleOfNumbers[0],tupleOfNumbers[1])
print(result)
print(type(result))
add, sub, mult, div, floor, power = result

print(type(add))


#create a list containing two numbers, pass to function

#print the results
