"""
FOR AND WHILE LOOP PRACTICE: 55 TASKS

Write a separate program for each task. Use the specified type of loop rather
than replacing it with a shortcut. Use the given data before trying your own.
The four spaces before each example line only indent it in this file; do not
print them. For input tasks, text after a prompt is what the user types.
Use the prompts shown so the terminal session matches the example.

For example, input("Number: ") displays "Number: " and waits for input. In
the example "Number: 3", the user typed "3"; quotation marks are not printed.

============================================================
FOR LOOPS - BASIC
============================================================

01. REPEAT A MESSAGE
    Use a for loop to print "Hello" three times, once per line.

    Expected terminal output:
    Hello
    Hello
    Hello

02. COUNT UP
    Use a for loop and range() to print the integers 1 through 5.

    Expected terminal output:
    1
    2
    3
    4
    5

03. COUNT DOWN
    Use a for loop and range() with a negative step to print 5 down to 1.

    Expected terminal output:
    5
    4
    3
    2
    1

04. EVEN NUMBERS
    Use a for loop and range() to print the even numbers from 2 through 10.

    Expected terminal output:
    2
    4
    6
    8
    10

05. PRINT A LIST
    Loop through ["pen", "paper", "tape"] and print each item on its own line.

    Expected terminal output:
    pen
    paper
    tape

06. PRINT CHARACTERS
    Loop through the string "cat" and print each character on its own line.

    Expected terminal output:
    c
    a
    t

07. MULTIPLY EACH NUMBER
    Loop through [2, 4, 6]. Multiply each value by 3 and print each result.

    Expected terminal output:
    6
    12
    18

08. NUMBER A LIST
    Loop through ["Ana", "Bo", "Kim"] and print each name with its position,
    starting the displayed numbering at 1.

    Expected terminal output:
    1. Ana
    2. Bo
    3. Kim

09. FILTER NUMBERS
    Loop through [2, 8, 5, 9] and print only numbers greater than 5.

    Expected terminal output:
    8
    9

10. RUNNING TOTAL
    a. Start with total = 0 and loop through [2, 4, 6].
    b. Add each number to total. Print the total after the loop finishes.

    Expected terminal output:
    12

============================================================
FOR LOOPS - DEVELOPING
============================================================

11. COUNT EVEN NUMBERS
    a. Loop through [1, 2, 4, 7, 8]. Use % to identify even numbers.
    b. Count them and print the count after the loop.

    Expected terminal output:
    3

12. UPPERCASE ITEMS
    Loop through ["pen", "paper", "tape"] and print each item in uppercase.

    Expected terminal output:
    PEN
    PAPER
    TAPE

13. LONGEST WORD
    a. Find the longest word in ["cat", "horse", "dog"] using a loop.
    b. Print it. If two words have the same maximum length, keep the first.

    Expected terminal output:
    horse

14. SMALLEST NUMBER
    Find and print the smallest value in [9, 3, 7, 4] using a loop, not min().

    Expected terminal output:
    3

15. COUNT ZEROS
    Loop through [5, 0, 7, 0], count the zeros, and print the final count.

    Expected terminal output:
    2

16. MULTIPLICATION TABLE
    Use a loop to print 3 multiplied by each number from 1 through 5.
    Include the calculation and result on each line as shown.

    Expected terminal output:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15

17. PRINT A RECTANGLE
    Use a loop to print three rows, each containing exactly four asterisks.

    Expected terminal output:
    ****
    ****
    ****

18. NESTED COORDINATES
    a. Use nested for loops. Both coordinates run from 1 through 3.
    b. The outer loop controls the first coordinate. Print each pair as shown.

    Expected terminal output:
    (1, 1)
    (1, 2)
    (1, 3)
    (2, 1)
    (2, 2)
    (2, 3)
    (3, 1)
    (3, 2)
    (3, 3)

============================================================
WHILE LOOPS
============================================================

19. COUNT UP
    Use a while loop to print 1 through 5. Update the counter inside the loop.

    Expected terminal output:
    1
    2
    3
    4
    5

20. COUNT DOWN
    Use a while loop to print 10, 8, 6, 4 and 2. Then print "Done".

    Expected terminal output:
    10
    8
    6
    4
    2
    Done

21. PASSWORD RETRY
    a. Ask for a password using input("Password: ") until the user enters
       exactly "open".
    b. Print "Try again" after each wrong input and "Welcome" after success.

    Example terminal session:
    Password: no
    Try again
    Password: open
    Welcome

22. ADD UNTIL ZERO
    a. Repeatedly ask for a whole number using input("Number: "). Convert
       each input to an integer; assume every input is valid.
    b. Stop when the user enters 0. Print the sum of the preceding numbers.

    Example terminal session:
    Number: 3
    Number: 5
    Number: 0
    Total: 8

23. COUNT ITEMS
    a. Ask for items using input("Item: ") until the user enters "done",
       ignoring case and surrounding whitespace when checking the stop word.
    b. Print the count of entered items, excluding "done".

    Example terminal session:
    Item: pen
    Item: paper
    Item:  DONE
    Count: 2

24. WITHDRAW FROM A BALANCE
    a. Start with balance = 20. Ask for withdrawals using
       input("Withdrawal: ") until the balance reaches 0. Convert the inputs
       to integers; assume they are whole numbers.
    b. Print "Invalid" for an amount that is not positive or exceeds the
       balance. Otherwise subtract it and print the remaining balance.

    Example terminal session:
    Withdrawal: 25
    Invalid
    Withdrawal: 8
    Balance: 12
    Withdrawal: 12
    Balance: 0

25. DOUBLE UNTIL THE LIMIT
    a. Start at 1 and use a while loop to repeatedly double the value.
    b. Print each value, including the first one that is greater than 20.

    Expected terminal output:
    1
    2
    4
    8
    16
    32

============================================================
INTERMEDIATE
============================================================

26. FIND AN INDEX
    a. Search ["Ana", "Bo", "Kim"] for the exact name "Bo" using a for loop.
    b. Stop once found and print its zero-based index as shown.

    Expected terminal output:
    Found at index 1

27. SKIP NEGATIVE NUMBERS
    a. Loop through [2, -1, 5, -4, 3]. Use continue to skip negative values.
    b. Add the remaining values and print the total.

    Expected terminal output:
    10

28. VALIDATE A NUMBER
    a. Ask for a whole number using input("Number: ") until the user enters
       a positive value. Convert each input to an integer.
    b. Print "Invalid" for each value of 0 or less, then print the accepted
       value. Assume every input is a valid whole number.

    Example terminal session:
    Number: 0
    Invalid
    Number: -2
    Invalid
    Number: 4
    Accepted: 4

29. CLEAN A LIST
    a. Start with ["  ana ", "", "BO", "   "]. Loop through the values.
    b. Strip whitespace, convert to title case, and skip empty results.
    c. Build and print a new list of the remaining cleaned names.

    Expected terminal output:
    ['Ana', 'Bo']

30. PRINT A TRIANGLE
    Use nested loops to print five lines. The first line has one asterisk,
    the second has two, and each following line adds one more.

    Expected terminal output:
    *
    **
    ***
    ****
    *****

============================================================
INTERMEDIATE LOOP PRACTICE
============================================================

31. PRINT MULTIPLES OF FIVE
    Use a for loop to print 5, 10, 15, 20 and 25 on separate lines.

    Expected terminal output:
    5
    10
    15
    20
    25

32. COUNT LETTERS
    Use a for loop to count occurrences of "a" in "banana". Print the count.

    Expected terminal output:
    3

33. SUM ODD NUMBERS
    Use a for loop to add the odd numbers from 1 through 9. Print the total.

    Expected terminal output:
    25

34. PRINT A RANGE BACKWARDS
    Use a for loop and range() to print 6, 4 and 2, one per line.

    Expected terminal output:
    6
    4
    2

35. COUNT LONG NAMES
    Use a for loop to count names longer than 3 characters in
    ["Ana", "Kim", "Alice", "Mo"]. Print the count.

    Expected terminal output:
    1

36. SKIP A VALUE
    Use a for loop to print the integers 1 through 5, skipping 3 with
    continue. Print each remaining number on its own line.

    Expected terminal output:
    1
    2
    4
    5

37. STOP AT A VALUE
    Loop through [2, 4, 0, 6]. Use break when the value is 0; print each
    number before it. Do not print 0 or numbers after it.

    Expected terminal output:
    2
    4

38. TOTAL PRODUCT QUANTITIES
    Use a for loop to sum the quantities in [("pen", 3), ("paper", 2)].
    Print the total as shown.

    Expected terminal output:
    Total: 5

39. PRINT THE FIRST THREE LETTERS
    Use a for loop to print the first three characters of "Python", one
    character per line.

    Expected terminal output:
    P
    y
    t

40. PRINT A COUNTDOWN
    Use a while loop to print 3, 2, 1, then print "Start" after the loop.

    Expected terminal output:
    3
    2
    1
    Start

41. SUM UNTIL A LIMIT
    Use a while loop to add 1, then 2, then 3, and so on until the running
    total first reaches or exceeds 10. Print that total.

    Expected terminal output:
    10

42. VALIDATE A COMMAND
    Ask using input("Command: ") until the user enters exactly "start".
    Print "Invalid" after each other input and "Started" when accepted.

    Example terminal session:
    Command: stop
    Invalid
    Command: start
    Started

43. COUNT POSITIVE INPUTS
    Ask for whole numbers using input("Number: ") until 0 is entered.
    Convert each to an integer and count only values greater than 0.
    Assume all inputs are valid whole numbers. Print the count.

    Example terminal session:
    Number: 2
    Number: -1
    Number: 5
    Number: 0
    Count: 2

44. PRINT TWO ROWS OF NUMBERS
    Use nested for loops. For each of two rows, print the values 1, 2 and 3
    together on one line, separated by one space.

    Expected terminal output:
    1 2 3
    1 2 3

45. FIND A MATCH
    Search ["pen", "paper", "tape"] for "tape" with a for loop. Print
    "Found" once when it is found and stop searching.

    Expected terminal output:
    Found

46. COUNT WORDS STARTING WITH A LETTER
    Use a for loop to count words starting with lowercase "s" in
    ["saw", "drill", "screw", "tape"]. Print the count.

    Expected terminal output:
    2

47. PRINT RUNNING TOTALS
    Loop through [2, 3, 4]. Add each value to a running total and print the
    total immediately after each addition.

    Expected terminal output:
    2
    5
    9

48. BUILD A SQUARE LIST
    Use a for loop to build and print a list containing the squares of
    1, 2, 3 and 4, in that order.

    Expected terminal output:
    [1, 4, 9, 16]

49. FIND AN EMPTY ENTRY
    Use a for loop to count empty strings in ["pen", "", "tape", ""].
    Print the count.

    Expected terminal output:
    2

50. INCREASE A BALANCE
    Start with balance 0. Use a while loop to add 3 until the balance is
    at least 10. Print only the final balance.

    Expected terminal output:
    12

============================================================
ADVANCED LOOP PRACTICE
============================================================

51. FIND ALL MATCHING POSITIONS
    Use a for loop to find the zero-based indexes of "pen" in
    ["pen", "paper", "pen", "tape", "pen"]. Print the indexes as a list.

    Expected terminal output:
    [0, 2, 4]

52. FIND A LONGEST STREAK
    Loop through [1, 1, 0, 1, 1, 1, 0, 1] and find the largest number of
    consecutive 1 values. Print the length. Reset the streak when seeing 0.

    Expected terminal output:
    3

53. FIND THE FIRST REPEATED ITEM
    Loop through ["pen", "tape", "paper", "tape", "pen"]. Print the first
    item encountered for a second time, then stop. If none repeat, print
    "No repeats".

    Expected terminal output:
    tape

54. MULTIPLICATION GRID
    Use nested for loops to print a 3-by-3 multiplication grid. The rows and
    columns both run from 1 to 3; separate values on each row with spaces.

    Expected terminal output:
    1 2 3
    2 4 6
    3 6 9

55. VALIDATE A SEQUENCE
    Use a loop to check whether [2, 4, 4, 7] is in nondecreasing order.
    Equal neighboring values are allowed. Print the Boolean result.

    Expected terminal output:
    True
"""
