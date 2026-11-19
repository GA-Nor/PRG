"""
TASK 2 - PASSWORD SECURITY AUDITOR
The CSV (passwords.csv) file contains 100 fictional accounts.

# Part A - Basic task

1. Open `passwords.csv` using `csv.DictReader()`.
2. Read `username` and `password` from each record.
3. Clean each username using `.strip()` and `.title()`.
4. Create a function named `check_password(password)`.
5. Return `True` when a password contains **at least 10 characters**; otherwise return `False`.
6. Use a `for` loop and `if` / `else` to print `STRONG` or `WEAK` for each account.
7. Count how many pass and fail the rule.
8. Print the totals after all 100 records have been processed.

Sample format (the file has many more rows):


PASSWORD SECURITY AUDIT
-----------------------
User042 - STRONG
User003 - WEAK
...
SUMMARY
Strong passwords: 36
Weak passwords: 64


Part B - Optional - advanced password rule

Extend your program to check **all three** of these requirements:

- Password is **more than 16 characters** long (17 or more).
- Password contains **at least one uppercase and at least one lowercase letter**.
- Password contains **at least one special character**, for example `.`, `!`, `-`, `_`, `#`, or `?`.

Create a function named `check_advanced_password(password)` that returns `True` only if **all three** conditions are met. Use a `for` loop to look at characters one by one, and use `if` statements and boolean variables to keep track of what you find.
Add a requirement for at least one digit using `.isdigit()`.

Print `MEETS ADVANCED RULE` or `DOES NOT MEET ADVANCED RULE` for each record, followed by totals. You can start by making the program display only the totals if 100 lines of output feels overwhelming.

"""

import csv


#TODO 1: Write a function named def check_password(password):
#It should return True if the password is at least 10 characters long.
    #init bool vars 
    #is the password long enough 
    #does it have uppercase
    #does it have lowercase
    #does it have a symbol
    
    #create a length criteria variable, where we will assign a minimum length
    
    #create a variable that stores the len(th) of the password passed to this function
    #Condition: if the password length is longer or equal to the length criteria, set the appropriate bool to true
    
    #use a for-loop to go through each character in the password (think of a string as a "list" of characters)
        # if the current character is upper (case), set the appropriate bool to true
        # if the current character is lower (case), set the appropriate bool to true
        
        #if the current character is equal to "." or "!" or "-", set the appropriate bool to true
        #if its instead equal to "_" or "#" or "?", also set the appropriate bool to true
        
    #Condition: if the password is long enough, and has uppercase and has lowercase and has a symbol, return True (this ends the function)
    #if the function has not ended (returned) by now, return false


strong_count = 0
weak_count = 0

print("PASSWORD SECURITY AUDIT")
print("-----------------------")

# TODO 2: Open passwords.csv and create a csv.DictReader.
with open("passwords.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
# TODO 3: Use a for loop to read each record.
# Clean each username and get the password.
# Call check_password(password).
# Print STRONG or WEAK, and update the appropriate counter.

    for row in reader:
        #assign the username value of the current row to a variable
        #string whitespaces, make first character uppercase
        
        #assign the password value of the current row to a variable
        
        #create a passwordIsStrongEnough variable, that will store (a boolean value), the result of our function check_password(). Pass the password we just extracted
        
        #Condition: if the password is strong enough, True
            #print the username and the text "Strong"
            #increase the strong_count by 1
        #if it isnt
            #print the username and the text "Weak"
            #increase the weak_count by 1


print()
print("SUMMARY")
# TODO 4: Print both counters.

