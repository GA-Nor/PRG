"""
COMBINED CHALLENGES: 40 LARGER TASKS

Write a separate program for each challenge. Complete every step, then try
different data and edge cases. Task IDs are stable; follow the difficulty
levels listed below rather than numerical order. Terminal examples show one
complete run; use the prompts and output format shown. Text after a prompt
is what the user types. The four spaces before each example line only indent
it here; do not print them. File-content examples show lines in the file, not
terminal output.

For example, input("Name: ") displays "Name: " and waits for input. In the
example "Name: Bo", the user typed "Bo"; quotation marks are not printed.

Difficulty levels (existing task numbers are preserved):
Simple:       01-10 and 24-28 (15 tasks).
Intermediate: 11-20 and 29-33 (15 tasks).
Advanced:     21-23 and 34-40 (10 tasks).

FILE RULES
Run file challenges with the Practice Tasks folder as the working directory.
Create stated input files yourself before running each program, except when
a task specifies the provided Sample Data folder. Use UTF-8. Create output
files with mode "x"; if the file exists, print
"File already exists" instead of overwriting it. Report read and write errors.
Only modify files made for these challenges. To repeat a challenge, use a
fresh directory or remove only your own output file.

Use built-in file operations and, if needed, os or pathlib. Do not use the
csv module or other libraries. CSV data in these exercises is deliberately
simple: fields contain no commas, quotes or line breaks. Splitting on commas
is NOT a general CSV parser and does not handle quoted CSV fields.

============================================================
COMBINING STRINGS, COLLECTIONS, LOOPS AND FUNCTIONS
============================================================

01. [SIMPLE] CLEAN A GUEST LIST
    a. Start with "  alice ; BOB ; ; alice ; charlie ". Split it on ";".
    b. Write clean_name(name) to strip and title-case a name. Discard blank
       names and case-insensitive duplicates, preserving first occurrence.
    c. Print a numbered list and total. Ask for a name using
       input("Search name: "), ignoring case and surrounding whitespace
       when searching. Print the result.

    Example terminal session:
    1. Alice
    2. Bob
    3. Charlie
    Total: 3
    Search name:  BOB
    Found: Bob

    For a search for Eve, print "User not found" instead of "Found: Bob".

02. [SIMPLE] SHOPPING RECEIPT
    a. Start with [("pen", 5, 3), ("paper", 12, 2)] where each tuple contains
       name, price and quantity. Write line_total(price, quantity).
    b. Print each product's value, the total, a 10% discount, and the final
       amount. Format all monetary amounts to two decimal places.

    Expected terminal output:
    pen: 15.00
    paper: 24.00
    Total: 39.00
    Discount: 3.90
    Pay: 35.10

03. [SIMPLE] TEMPERATURE REPORT
    a. Start with [18, 22, 16, 24, 20]. Use a loop and functions to find
       the minimum, maximum and average, and count readings at least 20.
    b. Print the results as shown. For an empty list print "No readings".

    Expected terminal output:
    Min: 16
    Max: 24
    Average: 20.0
    At least 20: 3

04. [SIMPLE] STOCK CHECKER
    a. Start with {"pen": 5, "paper": 2, "tape": 0}. Print each product and
       quantity in alphabetical order.
    b. Ask for a product using input("Product: "); strip and lowercase it.
       Print its quantity or "Unknown product". Finally, list products with
       fewer than 3 items alphabetically, separated by a comma and space.

    Example terminal session:
    paper: 2
    pen: 5
    tape: 0
    Product:  PEN
    Quantity: 5
    Low stock: paper, tape

05. [SIMPLE] COURSE SCORE SUMMARY
    a. Start with {"Ana": [40, 60, 80], "Bo": [50, 50], "Kim": []}.
    b. Write average(scores), returning None for an empty list.
    c. Print names in the given order, averages to one decimal, and "Pass"
       for an average of at least 50 or "Retry" otherwise. Print "No scores"
       instead for a student with no scores.

    Expected terminal output:
    Ana: 60.0 Pass
    Bo: 50.0 Pass
    Kim: No scores

06. [SIMPLE] WORD FREQUENCY
    a. Start with "  Red blue RED green blue red  ". Split on whitespace and
       count each word ignoring capitalization.
    b. Print words alphabetically with counts, then the most frequent word.
       If there is a tie, choose the alphabetically first word.
    c. If the string contains no words, print "No words" instead.

    Expected terminal output:
    blue: 2
    green: 1
    red: 3
    Most frequent: red

07. [SIMPLE] SIMPLE MENU AND LIST
    a. Start with an empty list. Repeatedly ask for add, list or quit using
       input("Command (add/list/quit): ").
    b. For add, ask for a name using input("Name: "), strip it, and reject
       blanks with "Invalid name"; otherwise append it and print
       "Added: NAME".
    c. For list, print names in entry order, or "No names" if empty. For an
       unknown command print "Invalid choice". Quit prints "Goodbye".

    Example terminal session:
    Command (add/list/quit): list
    No names
    Command (add/list/quit): add
    Name: Ana
    Added: Ana
    Command (add/list/quit): add
    Name: Bo
    Added: Bo
    Command (add/list/quit): list
    Ana
    Bo
    Command (add/list/quit): quit
    Goodbye

08. [SIMPLE] WORK HOURS
    a. Start with [("Mon", 7.5), ("Tue", 8.0), ("Wed", 6.5)] and hourly
       rate 200. Print each day and its hours to one decimal place.
    b. Calculate total hours and use a function to calculate gross pay.
       Print total hours to one decimal and pay to two decimals.

    Expected terminal output:
    Mon: 7.5
    Tue: 8.0
    Wed: 6.5
    Hours: 22.0
    Pay: 4400.00

09. [SIMPLE] CONTACT LOOKUP
    a. Build a dictionary from [("Ana", "123"), ("Bo", "456"), ("Kim", "789")].
       Keep phone numbers as strings.
    b. Repeatedly ask for a name using input("Name: "), ignoring case and
       surrounding whitespace. Print the stored name and number or
       "Not found". Stop on "quit", ignoring case, and print "Goodbye".

    Example terminal session:
    Name:  BO
    Bo: 456
    Name: Eve
    Not found
    Name: quit
    Goodbye

10. [SIMPLE] TOOL LOANS
    a. Start with available = {"drill", "saw", "hammer"} and
       borrowed = {"saw", "level"}.
    b. Print tools in both sets, available only, and borrowed only. Sort
       each group alphabetically and separate its names with commas and
       spaces. Print "None" for any empty group.

    Expected terminal output:
    Both: saw
    Available only: drill, hammer
    Borrowed only: level

============================================================
COMBINING TEXT FILES AND OTHER TOPICS
============================================================

11. [INTERMEDIATE] CLEAN A TEXT FILE
    a. Create challenge11_names.txt with the five lines shown below. The
       third line is blank; the first and last names have surrounding spaces.
    b. Write a function to strip and title-case each name. Skip blank and
       case-insensitive duplicate names, preserving first occurrence.
    c. Write the cleaned names to challenge11_clean.txt and print the count.

    Input challenge11_names.txt contents:
      ana
    BO

    ana
     Kim

    Expected terminal output:
    Saved: 3

    Expected challenge11_clean.txt contents:
    Ana
    Bo
    Kim

12. [INTERMEDIATE] FILE SCORE REPORT
    a. Create challenge12_scores.txt with one integer per line, as shown.
    b. Read the values into a list. Calculate total, average and highest.
    c. Write the results to challenge12_report.txt, then print "Report saved".
       If there are no scores, print "No scores" and do not create a report.

    Input challenge12_scores.txt contents:
    10
    20
    30

    Expected terminal output:
    Report saved

    Expected challenge12_report.txt contents:
    Total: 60
    Average: 20.0
    Highest: 30

13. [INTERMEDIATE] SEARCH A NAME FILE
    a. Create challenge13_names.txt with the lines shown below.
    b. Ask for a prefix using input("Prefix: "), strip it, and reject an
       empty prefix with "Invalid prefix". Print matching names in file order,
       ignoring case.
    c. Print the count. If none match, print "No matches" before the count.

    Input challenge13_names.txt contents:
    Ana
    Bo
    Kim
    Bob

    Example terminal session:
    Prefix:  b
    Bo
    Bob
    Matches: 2

    Another example terminal session:
    Prefix: z
    No matches
    Matches: 0

============================================================
COMBINING SIMPLE CSV FILES AND OTHER TOPICS
============================================================

14. [INTERMEDIATE] CREATE AN INVENTORY CSV
    a. Start with [("pen", 5, 3), ("paper", 12, 2)] as name, price, quantity.
    b. Write challenge14_inventory.csv with header name,price,quantity.
    c. Read the file back, calculate price * quantity for each row, and
       print their total to two decimal places.

    Expected terminal output:
    Total value: 39.00

    Expected challenge14_inventory.csv contents:
    name,price,quantity
    pen,5,3
    paper,12,2

15. [INTERMEDIATE] LOW-STOCK CSV REPORT
    a. Create challenge15_stock.csv with the data below. Read its data rows
       and convert the quantity field to an integer.
    b. Select quantities below 3 and write them in input order to
       challenge15_low_stock.csv with the same header. Print the count.

    Input challenge15_stock.csv contents:
    item,quantity
    pen,3
    paper,1
    tape,0

    Expected terminal output:
    Low-stock products: 2

    Expected challenge15_low_stock.csv contents:
    item,quantity
    paper,1
    tape,0

16. [INTERMEDIATE] EMPLOYEE HOURS CSV
    a. Create challenge16_hours.csv with the data below. Read its rows and
       sum integer hours per name using a dictionary.
    b. Print names alphabetically with totals, then overall hours and the
       name with the most hours. For a tie, choose the alphabetically first.

    Input challenge16_hours.csv contents:
    name,hours
    Ana,8
    Bo,6
    Ana,7

    Expected terminal output:
    Ana: 15
    Bo: 6
    Overall: 21
    Most: Ana

17. [INTERMEDIATE] CUSTOMER NAME SEARCH
    a. Create challenge17_customers.csv with the data below. Strip both fields
       and title-case names. Remove duplicate name-and-city pairs ignoring
       case, preserving the first occurrence.
    b. Ask for a city using input("City: ") and print matching names in input
       order, ignoring case and surrounding whitespace. Print the count;
       print "No matches" first if the count is zero.

    Input challenge17_customers.csv contents:
    name,city
     ana ,Oslo
    BO,Bergen
    Ana,Oslo

    Example terminal session:
    City:  OSLO
    Ana
    Matches: 1

    Another example terminal session:
    City: Tromso
    No matches
    Matches: 0

18. [INTERMEDIATE] ORDER SUMMARY CSV
    a. Create challenge18_orders.csv with the data below. Calculate the value
       of each row and sum values by product.
    b. Print products alphabetically with totals to two decimal places, then
       the overall total. Write the same lines to challenge18_summary.txt.

    Input challenge18_orders.csv contents:
    product,price,quantity
    pen,5,2
    paper,12,1
    pen,5,3

    Expected terminal output and challenge18_summary.txt contents:
    paper: 12.00
    pen: 25.00
    Total: 37.00

19. [INTERMEDIATE] CLASS ATTENDANCE
    a. Create challenge19_attendance.csv with the data below. Each data row
       is one attendance record. Count present and absent records, not people.
    b. List unique names with at least one present record in alphabetical
       order. Print the percentage of records present to one decimal place.
    c. If there are no records, print "No records" rather than dividing by zero.

    Input challenge19_attendance.csv contents:
    name,status
    Ana,present
    Bo,absent
    Kim,present
    Ana,present

    Expected terminal output:
    Present: 3
    Absent: 1
    Attended: Ana, Kim
    Present: 75.0%

20. [INTERMEDIATE] MINI INVENTORY MANAGER
    a. Create challenge20_inventory.csv with the data below and read products
       into a dictionary. Repeatedly ask for a command using
       input("Command (list/add/quit): ").
    b. list prints products alphabetically. For add, ask for a product using
       input("Product: ") and a quantity using input("Quantity: "). Convert
       the quantity to an integer, then increase stock or create the product.
       Strip and lowercase names. Reject blank names and non-positive
       quantities with "Invalid input"; assume quantity is a whole number.
       Print "Invalid choice" for an unknown command.
    c. On quit, write challenge20_new_inventory.csv with the same header
       and products sorted alphabetically. Do not overwrite the input.
       Print "Saved" after writing.

    Input challenge20_inventory.csv contents:
    item,quantity
    pen,3
    paper,5

    Example terminal session:
    Command (list/add/quit): list
    paper: 5
    pen: 3
    Command (list/add/quit): add
    Product: pen
    Quantity: 2
    Command (list/add/quit): add
    Product: tape
    Quantity: 1
    Command (list/add/quit): quit
    Saved

    Expected challenge20_new_inventory.csv contents:
    item,quantity
    paper,5
    pen,5
    tape,1

============================================================
REUSABLE FORMATTED REPORTS
============================================================

These challenges reproduce tasks 31-33 in String Practice using functions,
collections and loops. Use ljust(), rjust() and center() for alignment.
Join fields directly without extra separators. Field widths include the
characters in the field. The four-space example indentation is not printed;
trailing spaces on centered lines may not be visible in the terminal.

21. [ADVANCED] REUSABLE CLOUD INVOICE
    a. Store the invoice rows as (SKU, description, quantity, unit price):
       ("#0104", "Cloud Server Hosting (Pro)", 2, 149.99)
       ("#0209", "Dedicated SSL Certificate", 1, 59.50)
       ("#0088", "Enterprise Support & SLA", 12, 25.00)
    b. Write a function to print a centered heading between 62-character
       "=" borders. Use the fixed strings "ACME CLOUD SERVICES",
       "INVOICE #INV-00419", and "2026-11-24 22:41", one line each.
    c. Write a reusable row-formatting function. Use fields SKU width 9
       left, Description width 28 left, Qty width 5 right, and Total width
       20 right. Use the same widths for headings and data rows. Print a
       62-character "-" line between the heading and data.
    d. Loop over the rows, calculate quantity times unit price, and use your
       function to print each row. Format totals with "$" and two decimals.

    Expected terminal output:
    ==============================================================
                         ACME CLOUD SERVICES
                          INVOICE #INV-00419
                           2026-11-24 22:41
    ==============================================================
    SKU      Description                   Qty               Total
    --------------------------------------------------------------
    #0104    Cloud Server Hosting (Pro)      2             $299.98
    #0209    Dedicated SSL Certificate       1              $59.50
    #0088    Enterprise Support & SLA       12             $300.00

22. [ADVANCED] REUSABLE WORK ORDER
    a. Store the rows as (job, service, hours, hourly rate):
       ("#101", "Network diagnosis", 2, 90)
       ("#102", "Router setup", 1, 120)
       ("#103", "Equipment testing", 3, 75)
    b. Write a function that prints the centered headings and the
       50-character "=" borders. Use "ACME TECH SERVICES" and
       "WORK ORDER #WO-071", each centered in width 50.
    c. Write a row-formatting function using Job width 8 left, Service width
       24 left, Hours width 6 right, and Charge width 12 right. Use the same
       widths for the heading and data, with a 50-character "-" separator.
    d. Loop through the rows, calculate hours times hourly rate, and print
       each charge with "$" and two decimals.

    Expected terminal output:
    ==================================================
                    ACME TECH SERVICES
                    WORK ORDER #WO-071
    ==================================================
    Job     Service                  Hours      Charge
    --------------------------------------------------
    #101    Network diagnosis            2     $180.00
    #102    Router setup                 1     $120.00
    #103    Equipment testing            3     $225.00

23. [ADVANCED] REUSABLE STOCK REPORT
    a. Store the rows as (item, quantity, unit price):
       ("Ethernet Cable", 4, 12.50)
       ("Wireless Mouse", 3, 25.00)
       ("USB Hub", 2, 40.00)
    b. Write a function for the centered title and 48-character "=" borders.
       Center "STOCK VALUE REPORT" in width 48.
    c. Write a reusable row-formatting function using Item width 20 left,
       Qty width 6 right, Unit price width 11 right, and Value width 11 right.
       Use the same widths for the heading and rows, and print a 48-character
       "-" line between the heading and rows.
    d. Loop through the data, calculate quantity times unit price, and
       accumulate the total stock value. Format all amounts with "$" and
       two decimals. Print another "-" line and a final line with
       "Total stock value:" left-aligned in width 37 and the amount
       right-aligned in width 11.

    Expected terminal output:
    ================================================
                   STOCK VALUE REPORT
    ================================================
    Item                   Qty Unit price      Value
    ------------------------------------------------
    Ethernet Cable           4     $12.50     $50.00
    Wireless Mouse           3     $25.00     $75.00
    USB Hub                  2     $40.00     $80.00
    ------------------------------------------------
    Total stock value:                       $205.00

============================================================
MORE SIMPLE CHALLENGES
============================================================

24. [SIMPLE] CLEAN A SHOPPING LIST
    a. Start with [" milk ", "BREAD", "", " eggs "]. Strip and lowercase
       each value; skip blanks while preserving the original order.
    b. Print each item on its own line, then print the count.

    Expected terminal output:
    milk
    bread
    eggs
    Count: 3

25. [SIMPLE] CHECK WORK TEMPERATURES
    a. Start with [18, 22, 16]. Print each reading as "warm" if it is at
       least 18, otherwise "cool". Include the value as shown.
    b. Count warm readings and print the count.

    Expected terminal output:
    18: warm
    22: warm
    16: cool
    Warm: 2

26. [SIMPLE] SIMPLE ORDER TOTAL
    a. Start with [("pen", 3, 5), ("paper", 2, 8)] as name, quantity and
       price. Use a loop to calculate quantity times price for each row.
    b. Print each name and line total, then print the overall total.

    Expected terminal output:
    pen: 15
    paper: 16
    Total: 31

27. [SIMPLE] GREET A CLEANED NAME
    a. Ask for a name using input("Name: "). Strip whitespace and convert
       it to title case.
    b. If the result is empty, print "No name"; otherwise print the greeting.

    Example terminal session:
    Name:  aNA
    Hello, Ana!

    Example terminal session when Enter is pressed without a name:
    Name:
    No name

28. [SIMPLE] COUNT AVAILABLE TOOLS
    a. Start with {"drill": 2, "saw": 0, "hammer": 1}.
    b. Print products with quantities above zero, alphabetically. Then
       print the number of different available products, not their quantity.

    Expected terminal output:
    drill
    hammer
    Available products: 2

============================================================
MORE INTERMEDIATE CHALLENGES
============================================================

29. [INTERMEDIATE] SCORE CLASSIFICATION
    a. Start with {"Ana": [5, 7], "Bo": [3, 5], "Kim": []}.
    b. Write average(scores), returning None for an empty list. Print each
       name in input order with its average to one decimal place and "Pass"
       for an average of at least 5, otherwise "Retry".
    c. For an empty list print "No scores" rather than calculating an average.

    Expected terminal output:
    Ana: 6.0 Pass
    Bo: 4.0 Retry
    Kim: No scores

30. [INTERMEDIATE] COMPARE TEAM SKILLS
    a. Start with team_a = [" Python ", "Excel", "python"] and
       team_b = ["excel", "Safety"]. Strip and lowercase the skills.
    b. Use sets to find all unique skills and the skills shared by both.
       Print each result as a sorted list.

    Expected terminal output:
    All: ['excel', 'python', 'safety']
    Shared: ['excel']

31. [INTERMEDIATE] PRODUCT REPORT
    a. Start with [("tape", 8, 2), ("pen", 5, 3)] as name, price and
       quantity. Write a function returning price times quantity.
    b. Print rows alphabetically by product, then the overall value.

    Expected terminal output:
    pen: 15
    tape: 16
    Total: 31

32. [INTERMEDIATE] SEARCH REPEATEDLY
    a. Start with ["Ana", "Bo", "Kim"]. Repeatedly ask for a name using
       input("Name: "). Strip whitespace and search ignoring case.
    b. Print "Found" or "Not found". Stop on "quit", ignoring case, and
       print "Goodbye" without searching for that word.

    Example terminal session:
    Name:  BO
    Found
    Name: Eve
    Not found
    Name: quit
    Goodbye

33. [INTERMEDIATE] SAMPLE STOCK REPORT
    a. Read the provided stock.csv from Sample Data. Split each data row
       after skipping the header and convert quantities to integers.
    b. Print each item with quantity below 3, then the total quantity of all
       products. Keep the low-stock rows in file order.

    Expected terminal output:
    tape: 2
    Total units: 10

============================================================
MORE ADVANCED CHALLENGES
============================================================

34. [ADVANCED] VALIDATE STOCK ROWS
    a. Create challenge34_stock.csv with the contents below. Read rows after
       the header. A valid row has exactly two fields, a non-empty item,
       and a non-negative integer quantity.
    b. Write a function to validate a row. Skip invalid rows and count them;
       do not silently treat an invalid quantity as zero.
    c. Print the number of valid rows, the sum of their quantities, and the
       invalid-row count. For this task item names are unique.

    Input challenge34_stock.csv contents:
    item,quantity
    pen,3
    bad,abc
    paper,2
    tape,-1
    broken

    Expected terminal output:
    Valid items: 2
    Total units: 5
    Invalid rows: 3

35. [ADVANCED] SEARCH AND SUM PRODUCT ROWS
    a. Start with [("Pen", 3), ("paper", 2), (" pen ", 4)].
    b. Write a function that strips and lowercases product names and totals
       quantities per product. Preserve product order of first occurrence.
    c. Ask for a product using input("Product: "); search ignoring case and
       surrounding whitespace. Print the total or "Not found".

    Example terminal session:
    Product:  PEN
    Quantity: 7

    Another example terminal session:
    Product: tape
    Not found

36. [ADVANCED] RANK STUDENT SCORES
    a. Start with {"Ana": [5, 7], "Bo": [8, 4], "Kim": [9, 7]}.
    b. Write a function to calculate averages. Sort students by average
       descending, breaking ties alphabetically by name.
    c. Print names and averages to one decimal place.

    Expected terminal output:
    Kim: 8.0
    Ana: 6.0
    Bo: 6.0

37. [ADVANCED] CREATE A LOW-STOCK REPORT
    a. Read stock.csv from the provided Sample Data folder. Write functions
       to parse rows and select items with quantities below 4.
    b. Write the selected rows, in file order, to challenge37_low_stock.csv
       with the original header. Print the number of selected items.

    Expected terminal output:
    Selected: 2

    Expected challenge37_low_stock.csv contents:
    item,quantity
    pen,3
    tape,2

38. [ADVANCED] SUMMARIZE TICKETS
    a. Start with [("Ana", "open"), ("Bo", "closed"), ("Ana", "open"),
       ("Bo", "open")]. Each tuple is a person and ticket status.
    b. Write a function returning a dictionary of open-ticket counts per
       person. Ignore closed tickets.
    c. Print the people with open tickets alphabetically, then the total.

    Expected terminal output:
    Ana: 2
    Bo: 1
    Total open: 3

39. [ADVANCED] FORMAT AN ORDER SUMMARY
    a. Start with [("pen", 2, 5), ("paper", 1, 12)] as name, quantity,
       unit price. Write functions for line values and money formatting.
    b. Print each name left-aligned in width 10 and its line value,
       including "$" and two decimals, right-aligned in width 8.
    c. Print a 18-character "-" line, then "Total" in width 10 and the
       overall value right-aligned in width 8. Join fields without separators.

    Expected terminal output:
    pen         $10.00
    paper       $12.00
    ------------------
    Total       $22.00

40. [ADVANCED] COMPARE STAFF TRAINING
    a. Start with required = {"Safety", "Python", "Excel"} and
       staff = {"Ana": ["Safety", "Python"], "Bo": ["Safety", "Python", "Excel"]}.
    b. Write a function returning the sorted list of skills missing for a
       person. Print staff names alphabetically and their missing skills.
    c. Print the number of people with no missing skills.

    Expected terminal output:
    Ana: ['Excel']
    Bo: []
    Complete: 1
"""
