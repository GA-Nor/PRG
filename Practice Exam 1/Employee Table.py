"""
Write a Python program that stores predefined information for three employees in a list. Each employee has three fields: name, department, and salary.

Print all the employees as a table:

- Print a header with the columns `Name`, `Department`, and `Salary`.
- Print one employee per line, with columns separated by ` | `.
- Left-align the first two columns, each in a field of width 12.
- To use strings within a f-string, you can use:  f"Left adjust the string in these curly-brackets: {'Name'.ljust(12)}"

Your program should produce this output:
------------------------------------
Name         | Department   | Salary
------------------------------------
Alice        | Sales        | 32000
Bob          | Engineering  | 45000
Charlie      | Support      | 38000

"""

employees = [
    ["Alice", "Sales", 32000],
    ["Bob", "Engineering", 45000],
    ["Charlie", "Support", 38000]
]



