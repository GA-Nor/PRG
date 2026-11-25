"""
FUNCTION AND MATH OPERATOR PRACTICE: 50 TASKS

Write a separate program for each task. Define the requested function, call
it with the given values, and print its return value unless the task asks the
function itself to print. Assume numeric arguments have the stated types.
The four spaces before each output line only indent it here; do not print them.

============================================================
BASIC FUNCTIONS
============================================================

01. PRINT A GREETING
    a. Define greet() with no parameters. It should print "Hello!".
    b. Call the function once.

    Expected terminal output:
    Hello!

02. GREET A PERSON
    a. Define greet_person(name) to print "Hello, NAME!" with the given name.
    b. Call it with "Sam".

    Expected terminal output:
    Hello, Sam!

03. ADD
    Define add(a, b) to return their sum. Call add(3, 4) and print the result.

    Expected terminal output:
    7

04. SUBTRACT
    Define subtract(a, b) to return a minus b. Print subtract(10, 3).

    Expected terminal output:
    7

05. MULTIPLY
    Define multiply(a, b) to return their product. Print multiply(6, 4).

    Expected terminal output:
    24

06. DIVIDE
    Define divide(a, b) to return a / b. Print divide(9, 2). For this task,
    assume b is nonzero.

    Expected terminal output:
    4.5

07. SQUARE
    Define square(number) using ** to return the square. Print square(5).

    Expected terminal output:
    25

08. REMAINDER
    Define remainder(a, b) using % to return the remainder. Print
    remainder(17, 5). Assume b is nonzero.

    Expected terminal output:
    2

09. COMPLETE GROUPS
    Define whole_groups(items, group_size) using // to count complete groups.
    Print whole_groups(17, 5). Assume group_size is positive.

    Expected terminal output:
    3

10. CLEAN A NAME
    Define clean_name(name) to return the name stripped and title-cased.
    Call it with "  aNA lee " and print the returned string.

    Expected terminal output:
    Ana Lee

============================================================
PARAMETERS, RETURNS AND DECISIONS
============================================================

11. CHECK EVENNESS
    Define is_even(number) to return a Boolean using %. Print the results
    for 4 and 7, in that order.

    Expected terminal output:
    True
    False

12. CHECK AGE
    Define is_adult(age) to return True for age 18 or above, otherwise False.
    Print the results for 17 and 18, in that order.

    Expected terminal output:
    False
    True

13. FIND THE LARGER VALUE
    Define larger(a, b) to return the larger value, or either if equal.
    Print larger(3, 8), then larger(5, 5).

    Expected terminal output:
    8
    5

14. RECTANGLE AREA
    Define rectangle_area(width, height) to return their product.
    Print rectangle_area(4, 3).

    Expected terminal output:
    12

15. RECTANGLE PERIMETER
    Define rectangle_perimeter(width, height) to return 2 * (width + height).
    Print rectangle_perimeter(4, 3).

    Expected terminal output:
    14

16. CONVERT TEMPERATURE
    Define celsius_to_fahrenheit(c) to return c * 9 / 5 + 32.
    Print the result for 20 degrees Celsius.

    Expected terminal output:
    68.0

17. APPLY A DISCOUNT
    a. Define price_after_discount(price, percent). Subtract the percentage
       of price from price and return the result.
    b. Print the result for price 200 and discount 15. Assume percent is
       between 0 and 100.

    Expected terminal output:
    170.0

18. FORMAT A FULL NAME
    Define full_name(first, last). Strip both inputs, join them with one
    space, and return the result in title case. Print full_name("  aNA", "LEE ").

    Expected terminal output:
    Ana Lee

19. DESCRIBE A PRODUCT
    Define describe_product(name, price) to return an f-string with a colon
    and price to two decimal places. Print describe_product("Pen", 5).

    Expected terminal output:
    Pen: 5.00

20. SAFE DIVISION
    Define safe_divide(a, b). Return None if b is zero; otherwise return a / b.
    Print results for (8, 2) and (8, 0), in that order.

    Expected terminal output:
    4.0
    None

============================================================
LOOPS AND COMPOSITION
============================================================

21. SUM A LIST
    Define total(numbers) to use a loop and return the sum. Print its result
    for [2, 4, 6], then for an empty list.

    Expected terminal output:
    12
    0

22. AVERAGE A LIST
    Define average(numbers). Return None if the list is empty; otherwise
    return its sum divided by its length. Print results for [2, 4, 6] and [].

    Expected terminal output:
    4.0
    None

23. COUNT LONG WORDS
    Define count_long_words(words, minimum_length). Return the number of
    words with length at least minimum_length. Test ["cat", "horse", "dog",
    "elephant"] with a minimum of 4 and print the returned count.

    Expected terminal output:
    2

24. FIND THE LARGEST VALUE
    Define largest(numbers) using a loop. Return None if the list is empty.
    Print results for [3, 9, 4], then [].

    Expected terminal output:
    9
    None

25. CALCULATE A BILL
    a. Define calculate_bill(price, quantity, tax_percent). Multiply price
       by quantity and add the given percentage of that amount as tax.
    b. Call it with 10, 3 and 25. Print the result with two decimal places.
       Assume quantity and tax_percent are non-negative.

    Expected terminal output:
    37.50

26. SPLIT A COST
    Define split_cost(total, people) to return each person's share, or None
    when people is 0 or negative. Print results for (100, 4) and (100, 0).

    Expected terminal output:
    25.0
    None

27. CONVERT MINUTES
    Define minutes_to_hours_minutes(minutes). Use // and % to return a tuple
    of complete hours and remaining minutes. Print the result for 135.
    Assume minutes is a non-negative whole number.

    Expected terminal output:
    (2, 15)

28. COUNT EVEN VALUES
    a. Define is_even(number), then define count_even(numbers).
    b. Call is_even for each value and return the count of even numbers.
    c. Print count_even([1, 2, 4, 7, 8]).

    Expected terminal output:
    3

29. CLEAN A LIST OF NAMES
    a. Define clean_name(name), returning a stripped, title-cased name.
    b. Define clean_names(names) to call clean_name for each input, skip
       empty results, and return a new list.
    c. Print the result for ["  ana ", "", "BO "].

    Expected terminal output:
    ['Ana', 'Bo']

30. SUMMARIZE NUMBERS
    a. Define total(numbers) and average(numbers), as in tasks 21 and 22.
    b. Define summary(numbers) to call them and return (total, average).
       For an empty list, return (0, None).
    c. Print summary([2, 4, 6]), then summary([]).

    Expected terminal output:
    (12, 4.0)
    (0, None)

============================================================
MORE FUNCTION PRACTICE
============================================================

31. CALCULATE A CUBE
    Define cube(number) to return the number raised to the third power.
    Print cube(3).

    Expected terminal output:
    27

32. CONVERT METRES TO CENTIMETRES
    Define metres_to_cm(metres) to return metres multiplied by 100.
    Print metres_to_cm(1.5).

    Expected terminal output:
    150.0

33. CALCULATE TRIANGLE AREA
    Define triangle_area(base, height) to return base times height divided
    by 2. Print triangle_area(6, 4).

    Expected terminal output:
    12.0

34. APPLY TAX
    Define add_tax(price, percent) to return price plus that percentage.
    Print add_tax(80, 25). Assume the percentage is non-negative.

    Expected terminal output:
    100.0

35. CHECK A RANGE
    Define in_range(number, low, high) to return whether the number is
    between low and high inclusive. Print results for (5, 1, 5) and (6, 1, 5).

    Expected terminal output:
    True
    False

36. COUNT CHARACTERS
    Define character_count(text) to return its length, including spaces.
    Print character_count("hello world").

    Expected terminal output:
    11

37. CALCULATE CHANGE
    Define change_due(paid, cost) to return paid minus cost. Assume paid is
    at least cost. Print change_due(100, 65).

    Expected terminal output:
    35

38. CLASSIFY A NUMBER
    Define number_sign(number) to return "positive", "negative" or "zero".
    Print results for 4, -2 and 0, in that order.

    Expected terminal output:
    positive
    negative
    zero

39. COMBINE WORDS
    Define join_words(first, second) to return both strings with one space
    between them. Print join_words("cloud", "server").

    Expected terminal output:
    cloud server

40. CHECK A PREFIX
    Define has_prefix(text, prefix) to return whether text starts with prefix,
    ignoring case. Print results for ("Cloud", "cl") and ("Cloud", "ou").

    Expected terminal output:
    True
    False

41. CALCULATE A MULTIPLICATION TABLE
    Define multiples(number, count) to return a list of the first count
    positive multiples, starting with number. Print multiples(3, 4).
    Assume count is non-negative.

    Expected terminal output:
    [3, 6, 9, 12]

42. COUNT POSITIVE VALUES
    Define count_positive(numbers) to return the number of values greater
    than 0. Print count_positive([-2, 0, 3, 4]).

    Expected terminal output:
    2

43. FIND THE SHORTEST WORD
    Define shortest_word(words) to return the shortest string, choosing the
    first if lengths tie. Return None for an empty list. Print results for
    ["cat", "a", "dog"] and [].

    Expected terminal output:
    a
    None

44. CONVERT SECONDS
    Define seconds_to_minutes(seconds) to return a tuple of complete minutes
    and remaining seconds. Assume a non-negative integer. Print the result
    for 125.

    Expected terminal output:
    (2, 5)

45. CALCULATE AVERAGE COST
    Define average_cost(total, quantity) to return total divided by quantity,
    or None if quantity is 0 or negative. Print results for (30, 3) and (30, 0).

    Expected terminal output:
    10.0
    None

46. FORMAT A TOTAL
    Define format_money(amount) to return a string with "$" and two decimal
    places. Print format_money(12.5).

    Expected terminal output:
    $12.50

47. ADD ITEM VALUES
    Define inventory_value(items), where each item is a (price, quantity)
    tuple. Return the sum of price times quantity. Print the result for
    [(5, 3), (12, 2)].

    Expected terminal output:
    39

48. COUNT MATCHES
    Define count_matches(items, target) to count exact matches. Print its
    result for (["pen", "tape", "pen"], "pen").

    Expected terminal output:
    2

49. FILTER SHORT NAMES
    Define short_names(names, limit) to return a new list containing names
    with length at most limit, in their original order. Print the result for
    (["Ana", "Alice", "Bo"], 3).

    Expected terminal output:
    ['Ana', 'Bo']

50. SUMMARIZE STOCK
    a. Define total_units(stock) to return the sum of dictionary quantities.
    b. Define low_stock(stock, limit) to return a sorted list of products
       whose quantities are below limit.
    c. Use {"pen": 5, "paper": 2, "tape": 0} and limit 3. Print the total,
       then the list of low-stock products.

    Expected terminal output:
    7
    ['paper', 'tape']
"""
