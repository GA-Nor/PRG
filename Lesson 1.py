"""
This will be about
variables and strings
mostly
"""

#Variables and strings
print("Print dette")

#This is a variable
navn = "Jostein"

#print name
print(navn)

#change name, string
navn = "Sarah"

#print name
print(navn)

#integer, int
tall = 5
#float
flyttall = 5.0

#add int
#combine with string
print(navn + str(tall))

#Casting a string as an int, will fail. 
#nyttTall = int(navn)

#upper, \n, 
storBokstav = navn.lower()
print(storBokstav)

#Concatenation, combine strings

"""
split()	Split a string into a list	"a,b,c".split(",")	['a','b','c']
join()	Join a list into a string	",".join(['a','b','c'])	"a,b,c"
"""
#Create a string to split
#stringToSplit = "Dette er en test"
#Split by space, returns a list
#splitString = stringToSplit.split(" ")
#Print list
#print(splitString)
#Join together the list of strings into a single string, with a space in between each word
#joinedString = " ".join(splitString)
#print the joined string
#print(joinedString)

    #Create a string that we use to repeat X number of times, using the * operator
#tegn = "*"
    # "\n" means new line, so text will continue on a new line.
#print(tegn * 40 +"\n"+tegn * 40)

#add user input
#firstName = input("Please enter your name: ")
#print("Hello " + firstName)
#combine first name and last name
#lastName = input("Please enter your last name: ")
#fullName = firstName + " " + lastName
#print("Hello " + fullName)

#cast numeric input as int
number1 = int(input("Input a length: "))
number2 = int(input("Input a width:"))

print(number1+number2)
#print name, formatting print("{} and {}.format(n,c) or print(f"n: {a}"), also {X.2f}

#operators, + - * / **(power) % remainder
area = number1*number2
#rectangle area
print("Area: ",area,"m2")



# TASK

"""
Create a script that takes the following inputs:
- First name
- Last name
- Annual salary
- tax rate (%)
- Returns the following string with input names (Hi, Fname LName, your annual salary of XXXXX equates to a monthly salary of: XXXXXX)


"""