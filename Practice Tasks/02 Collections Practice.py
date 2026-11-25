"""
COLLECTIONS PRACTICE: 102 TASKS

Write a separate program for each task. Use the given starting values, then
try your own. The four spaces before each example line only indent it in this
file; do not print them. For input tasks, the text after the prompt is what
the user types. Use the shown prompts and print the results on separate lines.
Python normally displays string items in lists and dictionaries with quotes.

For example, input("Name: ") displays "Name: " and waits for input. In the
example "Name: Bo", the user typed "Bo"; the quotation marks are not printed.

============================================================
LISTS
============================================================

01. CREATE A LIST
    a. Create a list containing "pen", "paper" and "tape", in that order.
    b. Print the list itself. On the next line, print its length.

    Expected terminal output:
    ['pen', 'paper', 'tape']
    3

02. ACCESS LIST ITEMS
    a. Start with ["pen", "paper", "tape"].
    b. Use indexes to print the first item, then the last item.

    Expected terminal output:
    pen
    tape

03. ADD ITEMS
    a. Start with ["pen", "paper"]. Append "tape" to the end.
    b. Insert "pencil" at index 1. Print the final list.

    Expected terminal output:
    ['pen', 'pencil', 'paper', 'tape']

04. CHANGE AN ITEM
    a. Start with ["red", "blue", "green"].
    b. Replace the item at index 1 with "yellow" and print the list.

    Expected terminal output:
    ['red', 'yellow', 'green']

05. REMOVE AN ITEM
    a. Start with ["milk", "bread", "eggs"].
    b. Remove "bread" by value and print the remaining list.

    Expected terminal output:
    ['milk', 'eggs']

06. SLICE A LIST
    a. Start with [10, 20, 30, 40, 50]. Use a slice to select 20, 30 and 40.
    b. Print the slice, then print the original list to check it is unchanged.

    Expected terminal output:
    [20, 30, 40]
    [10, 20, 30, 40, 50]

07. COLLECT FOODS
    a. Start with an empty list. Ask for three foods, using input("Food: ")
       each time.
    b. Append each input, then print the list and its length on separate lines.

    Example terminal session:
    Food: apple
    Food: pear
    Food: rice
    ['apple', 'pear', 'rice']
    3

08. SORT AND REVERSE
    a. Start with [4, 1, 3, 2]. Sort it in ascending order and print it.
    b. Reverse the sorted list and print it again.

    Expected terminal output:
    [1, 2, 3, 4]
    [4, 3, 2, 1]

09. CHECK MEMBERSHIP
    a. Start with ["Ana", "Bo", "Kim"] and ask for a name using input("Name: ").
    b. Print "Found" if the exact name is in the list, otherwise "Not found".
       This search is case-sensitive.

    Example terminal session:
    Name: Bo
    Found

    Another example terminal session:
    Name: bo
    Not found

10. COMBINE LISTS
    a. Create ["hammer", "saw"] and ["drill", "tape"] as separate lists.
    b. Use + to make a new combined list. Print it, then print each original.

    Expected terminal output:
    ['hammer', 'saw', 'drill', 'tape']
    ['hammer', 'saw']
    ['drill', 'tape']

============================================================
TUPLES
============================================================

11. ACCESS A TUPLE
    a. Create the tuple ("pen", 12.5).
    b. Use indexes to print its name and price, each on a separate line.

    Expected terminal output:
    pen
    12.5

12. UNPACK A TUPLE
    a. Unpack ("desk", 120, 4) into product, price and quantity variables.
    b. Print the product, then print price multiplied by quantity.

    Expected terminal output:
    desk
    480

13. COORDINATE PAIRS
    a. Start with points = [(1, 2), (3, 4), (5, 6)].
    b. Loop through the list, unpack each pair, and print it in the format
       shown below, including parentheses and a space after the comma.

    Expected terminal output:
    (1, 2)
    (3, 4)
    (5, 6)

14. COUNT AND FIND
    a. Start with ("red", "blue", "red", "green").
    b. Print the number of occurrences of "red", then the index of "green".

    Expected terminal output:
    2
    3

15. CREATE A NEW TUPLE
    a. Store the location (10, 20) in a tuple.
    b. Create a new tuple with 5 added to the first value and the second
       unchanged. Print the new tuple. Do not assign to an existing element.

    Expected terminal output:
    (15, 20)

============================================================
DICTIONARIES
============================================================

16. CHANGE A VALUE
    a. Create {"name": "Ava", "role": "trainee"}.
    b. Print the name and role on separate lines using their keys.
    c. Change the role to "technician" and print the dictionary.

    Expected terminal output:
    Ava
    trainee
    {'name': 'Ava', 'role': 'technician'}

17. UPDATE STOCK
    a. Start with {"pen": 5, "paper": 2}.
    b. Add "tape" with quantity 3, then increase "pen" by 1. Print the result.

    Expected terminal output:
    {'pen': 6, 'paper': 2, 'tape': 3}

18. LOOK UP A KEY
    a. Start with {"pen": 5, "paper": 2}. Ask for a product using
       input("Product: ").
    b. Print its quantity if it exists; otherwise print "Unknown product".

    Example terminal session:
    Product: pen
    5

    Another example terminal session:
    Product: tape
    Unknown product

19. DISPLAY A DICTIONARY
    a. Start with {"pen": 5, "paper": 2, "tape": 3}.
    b. Loop through the entries and print each key and value as shown.

    Expected terminal output:
    pen: 5
    paper: 2
    tape: 3

20. TOTAL QUANTITIES
    a. Start with {"pen": 5, "paper": 2, "tape": 3}.
    b. Add the quantities together and print the total.

    Expected terminal output:
    10

21. COUNT COLOURS
    a. Start with ["red", "blue", "red", "green", "blue", "red"].
    b. Build a dictionary counting how many times each colour appears.
    c. Print the counts in order of first appearance, as shown.

    Expected terminal output:
    red 3
    blue 2
    green 1

22. A LIST INSIDE A DICTIONARY
    a. Create a dictionary with name "Sam" and skills ["Python", "Excel"].
    b. Append "Safety" to the skills list stored inside the dictionary.
    c. Print the name and then the skills list.

    Expected terminal output:
    Sam
    ['Python', 'Excel', 'Safety']

============================================================
SETS AND COMBINATIONS
============================================================

23. FIND UNIQUE COLOURS
    a. Create a set from ["red", "blue", "red", "green"].
    b. Print its size, then print the colours as a sorted list.

    Expected terminal output:
    3
    ['blue', 'green', 'red']

24. CHANGE A SET
    a. Start with {"pen", "paper"}. Add "tape" and remove "pen".
    b. Print the remaining values as a sorted list.

    Expected terminal output:
    ['paper', 'tape']

25. FIND COMMON NAMES
    a. Create A = {"Ana", "Bo", "Kim"} and B = {"Bo", "Kim", "Leo"}.
    b. Find the names present in both sets and print them as a sorted list.

    Expected terminal output:
    ['Bo', 'Kim']

26. COMBINE TWO SETS
    a. Use A = {"Ana", "Bo", "Kim"} and B = {"Bo", "Kim", "Leo"}.
    b. Find everyone in either set without duplicates. Print a sorted list.

    Expected terminal output:
    ['Ana', 'Bo', 'Kim', 'Leo']

27. COMPARE SETS
    a. Use A = {"Ana", "Bo", "Kim"} and B = {"Bo", "Kim", "Leo"}.
    b. Print a sorted list of names in A but not B, then one for B but not A.

    Expected terminal output:
    ['Ana']
    ['Leo']

28. CLEAN AND REMOVE DUPLICATES
    a. Start with [" Ana ", "BO", "ana", " Kim "].
    b. Strip each name and convert it to title case. Build a new list
       without case-insensitive duplicates, keeping first occurrence order.
    c. Print the new list.

    Expected terminal output:
    ['Ana', 'Bo', 'Kim']

29. SUM REPEATED PRODUCTS
    a. Start with [("pen", 3), ("paper", 2), ("pen", 4)].
    b. Build a dictionary that totals quantities by product. Print it.

    Expected terminal output:
    {'pen': 7, 'paper': 2}

30. AVERAGE SCORES
    a. Start with {"Ana": [4, 5, 3], "Bo": [2, 4]}.
    b. Print each name and the average of their scores as shown.
    c. If you try an empty score list, print "No scores" for that person
       instead of dividing by zero.

    Expected terminal output:
    Ana 4.0
    Bo 3.0

============================================================
MORE LIST TASKS
============================================================

31. TAKE AN ITEM FROM A LIST
    a. Start with tools = ["hammer", "saw", "drill"].
    b. Use pop() to remove the last item and store it in a variable.
    c. Print the removed item, then print the remaining list.

    Expected terminal output:
    drill
    ['hammer', 'saw']

32. REPLACE A SECTION
    a. Start with days = ["Mon", "Tue", "Wed", "Thu", "Fri"].
    b. Replace the second and third items with "Training" using a slice.
       Keep the other items in their original order. Print the final list.

    Expected terminal output:
    ['Mon', 'Training', 'Thu', 'Fri']

33. MAKE AN INDEPENDENT COPY
    a. Start with original = ["pen", "paper"]. Make a separate copy of it.
    b. Append "tape" to the copy only. Print the original and then the copy.

    Expected terminal output:
    ['pen', 'paper']
    ['pen', 'paper', 'tape']

34. ADD SEVERAL ITEMS
    a. Start with tools = ["hammer", "saw"] and extras = ["drill", "tape"].
    b. Use extend() to add each item from extras to tools.
    c. Print tools and then extras. The extras list should remain unchanged.

    Expected terminal output:
    ['hammer', 'saw', 'drill', 'tape']
    ['drill', 'tape']

35. FIND AN ITEM'S POSITION
    a. Start with colours = ["red", "green", "blue"].
    b. Ask for a colour using input("Colour: "). If it is in the list,
       print its zero-based index as shown. Otherwise print "Not found".
       This search is case-sensitive.

    Example terminal session:
    Colour: green
    Index: 1

    Another example terminal session:
    Colour: yellow
    Not found

36. COUNT LOW VALUES
    a. Start with temperatures = [18, 12, 21, 12, 16].
    b. Use a loop to count values below 18. Print the count as shown.

    Expected terminal output:
    Below 18: 3

37. COLLECT POSITIVE NUMBERS
    a. Start with numbers = [-2, 4, 0, 7, -1, 3].
    b. Use a loop to build a new list containing only values greater than 0.
       Preserve their original order, then print the new list.

    Expected terminal output:
    [4, 7, 3]

38. REMOVE A VALUE WITHOUT AN ERROR
    a. Start with items = ["pen", "paper", "tape"].
    b. Ask for an item using input("Remove: "). If the exact item exists,
       remove it once and print the updated list.
    c. If it does not exist, print "Item not found" followed by the unchanged
       list. Do not call remove() on a missing value.

    Example terminal session:
    Remove: paper
    ['pen', 'tape']

    Another example terminal session:
    Remove: drill
    Item not found
    ['pen', 'paper', 'tape']

39. WORK WITH A TWO-DIMENSIONAL LIST
    a. Start with shelves = [["pen", "pencil"], ["paper", "tape"]].
    b. Use indexes to print "tape". Replace "pencil" with "marker".
    c. Print the complete updated list.

    Expected terminal output:
    tape
    [['pen', 'marker'], ['paper', 'tape']]

40. BUILD A SHOPPING LIST
    a. Start with an empty list. Repeatedly ask for an item using
       input("Item: "). Stop when the user enters "done", ignoring case
       and surrounding whitespace when checking the stop word.
    b. Strip each other input. Add non-empty items in the order entered;
       skip blank inputs. Print the final list and its length.

    Example terminal session:
    Item: milk
    Item: bread
    Item: done
    ['milk', 'bread']
    2

============================================================
MORE TUPLE TASKS
============================================================

41. MAKE A SINGLE-ITEM TUPLE
    a. Create a tuple containing only "apple". Remember that a single-item
       tuple needs a trailing comma.
    b. Print the tuple, then print its length.

    Expected terminal output:
    ('apple',)
    1

42. SLICE A TUPLE
    a. Start with levels = ("low", "medium", "high", "critical").
    b. Use a slice to select the second and third values. Print the result.
       Then print the original tuple to show that it has not changed.

    Expected terminal output:
    ('medium', 'high')
    ('low', 'medium', 'high', 'critical')

43. COMBINE TUPLES
    a. Create morning = ("inspection", "repair") and afternoon = ("report",).
    b. Use + to create a new tuple containing all three tasks. Print it.

    Expected terminal output:
    ('inspection', 'repair', 'report')

44. CHECK TUPLE MEMBERSHIP
    a. Start with allowed = ("admin", "editor", "viewer").
    b. Ask for a role using input("Role: "). Print "Allowed" if the exact
       role is in the tuple; otherwise print "Not allowed".

    Example terminal session:
    Role: editor
    Allowed

    Another example terminal session:
    Role: guest
    Not allowed

45. SWAP TWO VALUES
    a. Start with left = "red" and right = "blue".
    b. Use tuple unpacking to swap the values without losing either one.
    c. Print left and then right on separate lines.

    Expected terminal output:
    blue
    red

46. CONVERT BETWEEN LIST AND TUPLE
    a. Start with sizes = ("small", "medium", "large").
    b. Convert it to a list, add "extra large", and convert the result back
       to a new tuple. Print the new tuple, then the original tuple.

    Expected terminal output:
    ('small', 'medium', 'large', 'extra large')
    ('small', 'medium', 'large')

47. SUM TUPLE VALUES
    a. Start with hours = (7, 8, 6, 8, 5).
    b. Use a loop to add the values and print the total as shown.

    Expected terminal output:
    Total hours: 34

48. FIND THE HIGHEST TEMPERATURE
    a. Start with readings = (18, 22, 16, 24, 20).
    b. Use a loop to find the highest value. Print it as shown.
       Assume the tuple contains at least one number.

    Expected terminal output:
    Highest: 24

49. FILTER RECORDS
    a. Start with products = [("pen", 5), ("paper", 12), ("tape", 8)].
       Each tuple contains a product name and price.
    b. Loop through the records, unpack each one, and print the names of
       products costing less than 10, in their original order.

    Expected terminal output:
    pen
    tape

50. COORDINATE TRANSLATION
    a. Start with point = (3, 5) and movement = (2, -1).
    b. Unpack both tuples. Create a new tuple by adding the corresponding
       values: x to x and y to y.
    c. Print the new point, then the original point.

    Expected terminal output:
    (5, 4)
    (3, 5)

============================================================
MORE DICTIONARY TASKS
============================================================

51. REMOVE A KEY
    a. Start with stock = {"pen": 5, "paper": 2, "tape": 3}.
    b. Remove the "paper" entry. Print the remaining dictionary.

    Expected terminal output:
    {'pen': 5, 'tape': 3}

52. USE A DEFAULT VALUE
    a. Start with stock = {"pen": 5, "paper": 2}.
    b. Use get() to look up "pen" and then "tape". Use 0 as the default
       for a missing key. Print each result on its own line.

    Expected terminal output:
    5
    0

53. ADD OR UPDATE STOCK
    a. Start with stock = {"pen": 5, "paper": 2}.
    b. Ask for a product using input("Product: ") and a whole-number amount
       using input("Amount: "). Convert the amount to an integer.
    c. Add the amount to the product's quantity. If the product is new,
       start its quantity at 0. Assume the amount is non-negative.
    d. Print the dictionary.

    Example terminal session:
    Product: pen
    Amount: 3
    {'pen': 8, 'paper': 2}

    Another example terminal session:
    Product: tape
    Amount: 3
    {'pen': 5, 'paper': 2, 'tape': 3}

54. PRINT KEYS IN ORDER
    a. Start with prices = {"tape": 8, "pen": 5, "paper": 12}.
    b. Print each product name in alphabetical order, one per line.
       Do not change the original dictionary.

    Expected terminal output:
    paper
    pen
    tape

55. FIND THE MOST EXPENSIVE PRODUCT
    a. Start with prices = {"pen": 5, "paper": 12, "tape": 8}.
    b. Use a loop to find the product with the highest price and print the
       name and price as shown. Assume all prices are distinct.

    Expected terminal output:
    paper: 12

56. LOOK UP A CONTACT
    a. Start with contacts = {"Ana": "123", "Bo": "456"}.
    b. Ask for a name using input("Name: "). Look it up exactly and print
       the phone number, or "Contact not found" if the key is missing.

    Example terminal session:
    Name: Ana
    123

    Another example terminal session:
    Name: Kim
    Contact not found

57. GROUP STUDENTS BY ROLE
    a. Start with [("Ana", "trainee"), ("Bo", "technician"),
       ("Kim", "trainee")]. Each tuple contains a name and a role.
    b. Build a dictionary whose keys are roles and whose values are lists
       of names. Preserve each name's original order. Print the dictionary.

    Expected terminal output:
    {'trainee': ['Ana', 'Kim'], 'technician': ['Bo']}

58. NESTED PRODUCT INFORMATION
    a. Start with products = {"pen": {"price": 5, "quantity": 3},
       "paper": {"price": 12, "quantity": 2}}.
    b. Use the nested keys to calculate and print the value of the pen
       stock: price multiplied by quantity.

    Expected terminal output:
    Pen value: 15

59. FIND MISSING INFORMATION
    a. Start with person = {"name": "Sam", "role": "trainee"}.
    b. Check whether the key "email" exists. If it does, print its value;
       otherwise print "Email missing". Do not add a new key.

    Expected terminal output:
    Email missing

60. COUNT WORDS IN A SENTENCE
    a. Start with sentence = "Red blue red green BLUE".
    b. Split the sentence into words and count them in a dictionary,
       ignoring case. Print the words and counts in alphabetical order.

    Expected terminal output:
    blue: 2
    green: 1
    red: 2

============================================================
MORE SET TASKS
============================================================

61. TEST MEMBERSHIP
    a. Start with tools = {"hammer", "saw", "drill"}.
    b. Ask for a tool using input("Tool: "). Print "Available" if the exact
       name is in the set; otherwise print "Unavailable".

    Example terminal session:
    Tool: drill
    Available

    Another example terminal session:
    Tool: tape
    Unavailable

62. ADD SEVERAL VALUES
    a. Start with colours = {"red", "blue"}.
    b. Use update() to add "green" and "yellow" from a list. Print the set
       as a sorted list so the output order is predictable.

    Expected terminal output:
    ['blue', 'green', 'red', 'yellow']

63. DISCARD A MISSING VALUE
    a. Start with tools = {"hammer", "saw"}.
    b. Use discard() to remove "drill" if present, without raising an error
       when it is absent. Print the remaining values as a sorted list.

    Expected terminal output:
    ['hammer', 'saw']

64. FIND ITEMS UNIQUE TO EITHER GROUP
    a. Start with A = {"Ana", "Bo", "Kim"} and B = {"Bo", "Kim", "Leo"}.
    b. Find the names that appear in exactly one set, not both.
       Print the result as a sorted list.

    Expected terminal output:
    ['Ana', 'Leo']

65. CHECK A SUBSET
    a. Start with required = {"gloves", "helmet"} and
       supplied = {"boots", "gloves", "helmet"}.
    b. Print whether every required item is in supplied.

    Expected terminal output:
    True

66. CHECK FOR SHARED ITEMS
    a. Start with first = {"pen", "paper"} and second = {"tape", "glue"}.
    b. Use isdisjoint() to print whether the two sets have no shared items.

    Expected terminal output:
    True

67. COUNT UNIQUE WORDS
    a. Start with sentence = "red blue RED green blue".
    b. Split into words, convert each to lowercase, and put them in a set.
    c. Print the number of unique words, then the words as a sorted list.

    Expected terminal output:
    3
    ['blue', 'green', 'red']

68. FIND MISSING EQUIPMENT
    a. Start with required = {"boots", "gloves", "helmet"} and
       packed = {"boots", "helmet"}.
    b. Find required items that are not packed. Print them as a sorted list.
       If none are missing, the printed list should be empty.

    Expected terminal output:
    ['gloves']

69. COMPARE THREE TEAMS
    a. Start with A = {"Ana", "Bo", "Kim"}, B = {"Bo", "Kim", "Leo"},
       and C = {"Bo", "Kim", "Mia"}.
    b. Find the names present in all three sets. Print them as a sorted list.

    Expected terminal output:
    ['Bo', 'Kim']

70. CLEAN AND COMPARE ATTENDANCE
    a. Start with day_one = [" ana ", "BO", "ana"] and
       day_two = ["bo", " Kim ", "BO"].
    b. Strip and title-case each name, then create a set for each day.
    c. Find everyone who attended either day and everyone who attended both.
       Print both results as sorted lists, with the labels shown.

    Expected terminal output:
    Either day: ['Ana', 'Bo', 'Kim']
    Both days: ['Bo']

============================================================
ADDITIONAL LIST TASKS
============================================================

71. EVERY SECOND ITEM
    a. Start with [10, 20, 30, 40, 50, 60].
    b. Use a slice to select every second item starting at index 0. Print it.

    Expected terminal output:
    [10, 30, 50]

72. REVERSE WITHOUT CHANGING THE ORIGINAL
    a. Start with ["first", "second", "third"]. Create a reversed copy.
    b. Print the copy, then the original list.

    Expected terminal output:
    ['third', 'second', 'first']
    ['first', 'second', 'third']

73. COUNT A LIST ITEM
    a. Start with ["pen", "tape", "pen", "paper", "pen"].
    b. Print how many times "pen" appears.

    Expected terminal output:
    3

74. FIND THE FIRST NEGATIVE VALUE
    a. Loop through [4, 2, -3, -1]. Stop at the first negative number.
    b. Print its value. If there are none, print "No negative values".

    Expected terminal output:
    -3

75. COMBINE PAIRED LISTS
    a. Start with names = ["Ana", "Bo"] and scores = [8, 6].
    b. Print each name with the score at the same index, as shown.
       Assume the two lists have equal length.

    Expected terminal output:
    Ana: 8
    Bo: 6

============================================================
ADDITIONAL TUPLE TASKS
============================================================

76. UNPACK A DATE
    a. Start with date = (2026, 11, 24), in year, month, day order.
    b. Unpack it and print the date in day/month/year order.

    Expected terminal output:
    24/11/2026

77. TUPLE LENGTH
    a. Start with ("small", "medium", "large").
    b. Print the number of items and the last item on separate lines.

    Expected terminal output:
    3
    large

78. REPEAT A TUPLE
    a. Start with ("on", "off"). Use * to repeat the tuple twice.
    b. Print the resulting tuple.

    Expected terminal output:
    ('on', 'off', 'on', 'off')

79. TUPLE INSIDE A TUPLE
    a. Start with ("Ava", (4, 5)). Unpack the name and the score tuple.
    b. Print the name, then the sum of the two scores.

    Expected terminal output:
    Ava
    9

80. CHECK A COORDINATE
    a. Start with point = (3, -2). Unpack x and y.
    b. Print "Above" if y is positive, "Below" if negative, or "On axis"
       if zero.

    Expected terminal output:
    Below

============================================================
ADDITIONAL DICTIONARY TASKS
============================================================

81. PRINT VALUES
    a. Start with {"pen": 5, "paper": 2, "tape": 3}.
    b. Loop through its values in insertion order and print each value.

    Expected terminal output:
    5
    2
    3

82. FIND AN EMPTY STOCK ITEM
    a. Start with {"pen": 2, "paper": 0, "tape": 4}.
    b. Print each product whose quantity is zero.

    Expected terminal output:
    paper

83. CHECK TWO REQUIRED KEYS
    a. Start with {"name": "Ana", "role": "trainee"}.
    b. Print whether both "name" and "role" are present as keys.

    Expected terminal output:
    True

84. COPY AND UPDATE
    a. Start with original = {"pen": 5}. Make a separate dictionary copy.
    b. Change the copy's pen quantity to 8. Print original, then copy.

    Expected terminal output:
    {'pen': 5}
    {'pen': 8}

85. TOTAL TWO PRICE VALUES
    a. Start with {"pen": 5, "paper": 12}. Add the two prices by key.
    b. Print the total as shown.

    Expected terminal output:
    Total: 17

============================================================
ADDITIONAL SET TASKS
============================================================

86. NUMBER OF UNIQUE VALUES
    a. Create a set from [1, 2, 2, 3, 3, 3].
    b. Print its length.

    Expected terminal output:
    3

87. CHECK A SUPERSET
    a. Start with available = {"pen", "paper", "tape"} and
       required = {"pen", "paper"}.
    b. Print whether available is a superset of required.

    Expected terminal output:
    True

88. FIND A UNION
    a. Start with A = {1, 2} and B = {2, 3}.
    b. Print their union as a sorted list.

    Expected terminal output:
    [1, 2, 3]

89. FIND AN INTERSECTION
    a. Start with A = {1, 2, 3} and B = {2, 3, 4}.
    b. Print their intersection as a sorted list.

    Expected terminal output:
    [2, 3]

90. MAKE AN EMPTY SET
    a. Create an empty set, then add "pen" and "paper".
    b. Print the values as a sorted list. Do not use {} to create the set.

    Expected terminal output:
    ['paper', 'pen']

============================================================
ADVANCED LIST TASKS
============================================================

91. REMOVE DUPLICATES IN ORDER
    a. Start with [3, 1, 3, 2, 1, 4]. Build a list without duplicates.
    b. Preserve the first occurrence of each number. Print the new list.

    Expected terminal output:
    [3, 1, 2, 4]

92. ROTATE A LIST
    a. Start with [1, 2, 3, 4, 5]. Create a new list with the last two
       values moved to the front, preserving their order.
    b. Print the new list and then the original.

    Expected terminal output:
    [4, 5, 1, 2, 3]
    [1, 2, 3, 4, 5]

93. FLATTEN NON-EMPTY SHELVES
    a. Start with [["pen", "paper"], [], ["tape", "glue"]].
    b. Use nested loops to build and print one list of all items in order.

    Expected terminal output:
    ['pen', 'paper', 'tape', 'glue']

============================================================
ADVANCED TUPLE TASKS
============================================================

94. FIND THE LOWEST PRICE RECORD
    a. Start with [("pen", 5), ("paper", 12), ("tape", 5)].
    b. Find the lowest price and print the first matching tuple in input
       order. Assume the list is not empty.

    Expected terminal output:
    ('pen', 5)

95. PAIR NAMES WITH SCORES
    a. Start with names = ("Ana", "Bo", "Kim") and scores = (8, 6, 9).
    b. Build a list of (name, score) tuples pairing values by position.
       Print the list. Assume the tuples have equal length.

    Expected terminal output:
    [('Ana', 8), ('Bo', 6), ('Kim', 9)]

96. RETURN A RANGE AS A TUPLE
    a. Write score_range(scores) that returns (minimum, maximum), or None
       if scores is empty. Test it with (4, 9, 2, 7) and then ().
    b. Print the results on separate lines.

    Expected terminal output:
    (2, 9)
    None

============================================================
ADVANCED DICTIONARY TASKS
============================================================

97. MERGE QUANTITIES
    a. Start with {"pen": 3, "paper": 2} and {"pen": 4, "tape": 1}.
    b. Create a new dictionary summing matching quantities. Keep keys from
       the first dictionary in order, then new keys from the second. Print it.

    Expected terminal output:
    {'pen': 7, 'paper': 2, 'tape': 1}

98. INVERT A DICTIONARY
    a. Start with {"Ana": "red", "Bo": "blue", "Kim": "red"}.
    b. Build a dictionary from colour to a list of names. Preserve the
       original order of colours and names. Print the result.

    Expected terminal output:
    {'red': ['Ana', 'Kim'], 'blue': ['Bo']}

99. CALCULATE PRODUCT VALUES
    a. Start with {"pen": {"price": 5, "quantity": 3},
       "paper": {"price": 12, "quantity": 2}}.
    b. Calculate each price times quantity and print the overall value.

    Expected terminal output:
    Total: 39

============================================================
ADVANCED SET TASKS
============================================================

100. FIND COMMON SKILLS
    a. Start with A = {"Python", "Excel", "Safety"},
       B = {"Python", "Safety"}, C = {"Python", "Excel"}.
    b. Print the skills common to all three as a sorted list.

    Expected terminal output:
    ['Python']

101. COMPARE REQUIRED SKILLS
    a. Start with required = {"Python", "Safety", "Excel"} and
       actual = {"Python", "Excel", "Linux"}.
    b. Print missing required skills and extra skills as separate sorted lists.

    Expected terminal output:
    Missing: ['Safety']
    Extra: ['Linux']

102. TRACK UNIQUE VISITORS
    a. Start with [" Ana ", "BO", "ana", " Kim ", "bo"].
    b. Strip and title-case names, then use a set to find unique visitors.
    c. Print the count and names as a sorted list.

    Expected terminal output:
    Count: 3
    ['Ana', 'Bo', 'Kim']
"""
