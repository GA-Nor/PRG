"""
LESSON 3 - ERROR HANDLING
=========================

Topics:
- Input validation
- Error handling (Try-Except blocks)
- ValueError
- IndexError
- NameError
- Functions with error handling

"""

# ==================================================
# 1. INPUT VALIDATION - Checking if we're getting proper input
# ==================================================


# Check if input is empty, print an error message, if OK greet user



# Lets say we're taking Age as a variable, check if input is a number, 
# is it a digit, convert to int if valid, if not, print error



"""
Why do we use try-except?
To catch errors and prevent crashes.
It helps in handling unexpected input gracefully.
We can catch specific errors and respond accordingly.
For example, ValueError for wrong type, IndexError for bad index.
NameError for undefined variables.

"""

# ==================================================
# 2. ValueError - Invalid Data Type Conversion, we cant convert this to that
# ==================================================
"""
Use try-except and ValueError to catch errors when converting types, like str to int or float
"""

# ValueError occurs when converting incompatible data types
# Try to convert a string to int, except if we get a ValueError, print error

#Try the same, with a float-to int



# ==================================================
# 3. IndexError - When trying to access invalid list index
# ==================================================

"""
IndexError happens when accessing a list with invalid index, like out of range.
Use try-except to catch invalid index errors when accessing lists
"""

#Create a list of names, print, print the length of the list

#Access list, valid

# Invalid access with error handling, try-except on IndexError


# ==================================================
# 4. NameError - Undefined variable orfunction
# ==================================================

"""
NameError occurs when using undefined variables or functions
Use try-except to catch NameError when there MAY be undefined variables or functions.
For example when trying to use a variable not defined yet, or out of scope
"""

# NameError occurs when referencing undefined variables or functions

#Try to print an undefined variable or function, catch NameError


# ==================================================
# 5. COMBINING VALIDATION WITH TRY-EXCEPT
# ==================================================

#Defined a list of numbers
scores = [95, 87, 92, 88]

#Take an index as input from the user, to access the index in the list
user_index = input("Enter index (0-3) to retrieve score: ")

#try, convert to int, access the list and print the value at index
#then except, valuerrr, indexerr, 


# Can also be used in functions to validate input


# ==================================================
# 6. ZeroDivisionError - Dividing by zero causes error
# ==================================================

#Create a function that takes 2 numbers and divides them safely
#except ZeroDivisionError, print error
"""
Catch ValueError, IndexError, NameError, etc. specifically

Don't use bare 'except:' - it hides bugs

Use Try-Except when converting types or accessing lists/dicts

Return meaningfull error messages (Not just "An Error Occurred - oops")
"""


#TASK
#Ask the user to provide two numbers
#Write a function that takes those two numbers, a and b, divides a with b, and returns the result
# Handle potential errors related to:
    # type conversion (string->int)
    # division by zero


#Create a list of names
#Create a function that takes the list of names and an index, and returns the value at the index
# Handle potential errors related to accessing invalid list index

