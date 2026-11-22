"""
Add error handling for type mismatch and division by zero.
If the number is outside the given range, tell the user to try again

"""

number=input("Divide 100 by (a number between 1 and 100): ")
number=int(number)
result=100/number
print(result)
