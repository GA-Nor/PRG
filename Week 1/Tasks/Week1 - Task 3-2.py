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


# TODO 1: Write a function named check_password(password).
# It should return True if the password is at least 10 characters long.


strong_count = 0
weak_count = 0

print("PASSWORD SECURITY AUDIT")
print("-----------------------")

# TODO 2: Open passwords.csv and create a csv.DictReader.

# TODO 3: Use a for loop to read each record.
# Clean each username and get the password.
# Call check_password(password).
# Print STRONG or WEAK, and update the appropriate counter.

print()
print("SUMMARY")
# TODO 4: Print both counters.

# OPTIONAL CHALLENGE
# Write a separate check_advanced_password(password) function.
# Requirements: >16 characters; both upper/lowercase; special character.
# Keep the code simple: use a for loop and explicit if statements.
