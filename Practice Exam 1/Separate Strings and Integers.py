"""
Write a Python program that separates strings and integers from a list.

Use the predefined list below

Create a function called `separate_items()` that takes the list as a parameter and returns two lists: 
    one containing the type strings  
    one containing the type integers

Call the function and print the two lists in a structured format:

- The lists should be .sorted after separating (alphabetically / ascending)
- Print a header with the name and the number of elements in the list (e.g. `Strings: 25`) followed by a line of dashes.
- Print each element on a new line


Expected output:

Strings: 25
-----------
apple
apricot
banana
...

Integers: 25
------------
3
5
6
...
"""

items = [
    "apple", 12, "banana", 5, 27, "cherry", "grape", 8, "lemon", 41,
    19, "mango", "peach", 3, "plum", 56, "kiwi", 33, 7, "pear",
    "melon", 64, "lime", 21, 90, "fig", "date", 14, "orange", 38,
    "berry", 72, 9, "apricot", "coconut", 45, "papaya", 100, 17, "guava",
    58, "lychee", "nectarine", 29, 81, "olive", "quince", 6, "tomato", 36
]


