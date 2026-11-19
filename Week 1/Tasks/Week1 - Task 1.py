# TASK

"""
Create a script that takes the following inputs:
- First name
- Last name
- Annual salary
- tax rate (%)
- print() the following string with input names (Hi, Fname LName, your annual salary of XXXXX equates to a monthly salary of: XXXXXX)

"""



















"""
#Solution
firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
annualSalary = int(input("Annual Salary: "))
taxRate = float(input("Enter Tax rate (%): "))

taxPercent = taxRate/100
netSalary = annualSalary *(1-taxPercent)
monthlySalary = netSalary / 12

print("Hi, "+ firstName+ " " + lastName +", your annual salary of ",netSalary, " equates to a monthly salary of: ", monthlySalary )
"""