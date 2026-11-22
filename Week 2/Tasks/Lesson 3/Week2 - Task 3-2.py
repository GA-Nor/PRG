"""
Task 2 - Login Record Validator

Each record contains a name and a login count, separated by a comma:
"alice,15"

Create a function called process_record(record) that:
1. Splits the record into its name and login count.
2. Removes extra spaces from the name and formats it with a capital
   first letter, such as "alice" becoming "Alice".
3. Converts the login count from text to an integer.
4. Returns the name and login count together as a tuple.

Handle these two errors by returning the indicated message:
- The record has no login count: "ERROR: Missing login count"
- The login count is not a whole number: "ERROR: Login count must be numeric"

Try the function with each record below. Valid records should return a
name and an integer; invalid records should return an error message.
"""

records = ["alice,15", "bob,abc", "charlie", "david,12"]

# TODO: Create process_record(record) and handle IndexError and ValueError.
