"""
STRING PRACTICE: 53 TASKS

Work through the tasks in difficulty order using the Practice Tasks Guide.
Task numbers are kept stable; do tasks 34-53 before returning to the advanced
formatting tasks 31-33. Write each solution in a separate Python file and
use the starting values given unless input is requested.

Each terminal example shows one complete run. For tasks with input, the text
after a prompt is what the user types, followed by Enter. Use the prompts
shown so that your terminal output matches the example.

For example, input("Word: ") displays "Word: " and waits for the user to
type a word. In the example "Word: cat", the prompt is "Word: " and the
user typed "cat". The quotation marks are not displayed in the terminal.

The four spaces before each example line are only there to indent the example
in this file. Do not print those four spaces. Any additional spaces shown
after them are part of the output. Do not print quotation marks around
strings unless they appear in the expected terminal output.

============================================================
BASIC
============================================================

01. PRINT A STRING
    a. Create a variable containing the string "Python" and print it.
    b. Change the same variable to "Practice" and print it again.

    Expected terminal output:
    Python
    Practice

02. GREET THE USER
    a. Ask the user for their name using input("Name: ").
    b. Use an f-string to print Hello, followed by the name and an
       exclamation mark.

    Example terminal session:
    Name: Sam
    Hello, Sam!

03. JOIN TWO STRINGS
    a. Create first = "Ada" and last = "Lovelace".
    b. Use the + operator to join them with one space between them.
    c. Print the result.

    Expected terminal output:
    Ada Lovelace

04. MAKE A REPORT BORDER
    a. Use the * operator to create a line of exactly 20 hyphens.
    b. Print the border, then REPORT on a new line, then the border again.

    Expected terminal output:
    --------------------
    REPORT
    --------------------

05. COUNT CHARACTERS
    a. Store "workshop" in a variable named word.
    b. Use len() and print the number of characters.
    c. Try another value afterward; remember that spaces also count.

    Expected terminal output for "workshop":
    8

06. FIRST AND LAST CHARACTER
    a. Store "Python" in a variable named word.
    b. Use indexes to print the first character and the last character,
       each on its own line. Assume the string is not empty.

    Expected terminal output:
    P
    n

07. EXTRACT PARTS OF A CODE
    a. Store "ABC-123" in a variable named code.
    b. Use slicing to extract the letters before the hyphen and the digits
       after it. Print the two parts on separate lines, without the hyphen.

    Expected terminal output:
    ABC
    123

08. CHANGE LETTER CASE
    a. Store "good morning" in a variable named message.
    b. Print an uppercase version, then a lowercase version.
    c. Print the original variable to check whether it has changed.

    Expected terminal output:
    GOOD MORNING
    good morning
    good morning

09. CLEAN A NAME
    a. Start with name = "  aLEX smith  ", including the surrounding spaces.
    b. Remove the surrounding whitespace and convert the result to title case.
    c. Print the cleaned name.

    Expected terminal output:
    Alex Smith

10. CHECK FOR AN EMPTY WORD
    a. Ask the user for a word using input("Word: ").
    b. If the user enters an empty string, print "No word entered".
       Otherwise, print the first character. Do not index an empty string.

    Example terminal session with a word:
    Word: cat
    c

    Example terminal session when Enter is pressed without typing a word:
    Word:
    No word entered

============================================================
DEVELOPING
============================================================

11. SPLIT A STRING
    a. Start with text = "red,blue,green".
    b. Split the string at each comma and store the result in a list.
    c. Print the list itself, not each item separately.

    Expected terminal output:
    ['red', 'blue', 'green']

12. JOIN A LIST OF STRINGS
    a. Start with parts = ["red", "blue", "green"].
    b. Join the items into one string, using space, |, space between items.
    c. Print the resulting string.

    Expected terminal output:
    red | blue | green

13. REPLACE TEXT
    a. Start with text = "one-two-two".
    b. Replace every occurrence of "two" with "2".
    c. Print the resulting string. Leave "one" unchanged.

    Expected terminal output:
    one-2-2

14. CHECK A FILE EXTENSION
    a. Ask for a filename using input("Filename: ").
    b. Check whether it ends with ".txt", ignoring uppercase and lowercase.
    c. Print the Boolean result, True or False.

    Example terminal session:
    Filename: notes.TXT
    True

    Another example terminal session:
    Filename: notes.csv
    False

15. LOOK FOR AN URGENT MESSAGE
    a. Ask for a message using input("Message: ").
    b. Check whether the text "urgent" occurs anywhere in the message,
       ignoring uppercase and lowercase.
    c. Print "Urgent" when found; otherwise print "Normal".

    Example terminal session:
    Message: URGENT: call
    Urgent

    Another example terminal session:
    Message: hello
    Normal

16. COUNT AND CHECK CHARACTERS
    a. Start with message = "banana".
    b. Count the occurrences of "a" and print the count.
    c. Use the not in operator to check whether "z" is absent. Print the
       Boolean result on a separate line.

    Expected terminal output:
    3
    True

17. CLEAN A FULL NAME
    a. Ask for a first name using input("First name: "), then ask for a
       last name using input("Last name: ").
    b. Remove surrounding whitespace from each input, join them with one
       space, and convert the full name to title case.
    c. Print the cleaned full name.

    Example terminal session:
    First name:   aNA
    Last name:  lee
    Ana Lee

    In this example the first input starts with two spaces and the second
    input starts with one space. Both may also have trailing spaces.

18. FORMAT A PRICE
    a. Ask for a product name using input("Product: "), then ask for a
       numeric price using input("Price: ").
    b. Convert the price to a number and use an f-string to print the name,
       a colon, a space, and the price with exactly two decimal places.
    c. Assume the entered price is a valid number.

    Example terminal session:
    Product: pen
    Price: 12.5
    pen: 12.50

19. ALIGN TWO COLUMNS
    a. Print "Item" left-aligned in a field 12 characters wide, followed
       immediately by "Price" right-aligned in a field 8 characters wide.
    b. On the next line, use the same widths for "Pen" and "12.50".
    c. Do not print quotation marks or a separator between the fields.

    Expected terminal output:
    Item           Price
    Pen            12.50

20. CHECK FOR NON-BLANK TEXT
    a. Ask for text using input("Text: ").
    b. Remove surrounding whitespace and print whether anything remains
       as a Boolean value.

    Example terminal session when the user enters three spaces:
    Text:
    False

    Example terminal session with a non-blank input:
    Text:  hello
    True

============================================================
INTERMEDIATE
============================================================

21. CLEAN A SEMICOLON-SEPARATED LIST
    a. Start with names = " alice ; BOB ;  charlie ".
    b. Split at semicolons. For each part, strip surrounding whitespace
       and convert the name to title case.
    c. Print each cleaned name on its own line, in the original order.

    Expected terminal output:
    Alice
    Bob
    Charlie

22. REMOVE EXTRA SPACES BETWEEN WORDS
    a. Start with text = "  red   green  blue ".
    b. Remove surrounding whitespace and replace each run of whitespace
       between words with a single space. Split and join the words.
    c. Print the cleaned string. Do not remove the spaces between words.

    Expected terminal output:
    red green blue

23. VALIDATE A SIMPLE CODE
    a. Ask for a code using input("Code: ") and remove surrounding whitespace.
    b. A valid code has exactly six characters: two alphabetic characters,
       then a hyphen, then three digits. For example, AB-123 is valid.
    c. Print "Valid" if all conditions are met; otherwise print "Invalid".

    Example terminal session:
    Code: AB-123
    Valid

    Example terminal sessions for invalid codes:
    Code: A-123
    Invalid

    Code: AB-12x
    Invalid

24. CHECK AN EMAIL-LIKE ADDRESS
    a. Ask for an address using input("Address: ") and remove surrounding
       whitespace.
    b. Check that it contains exactly one "@" and at least one character
       on each side of the "@".
    c. Print "Valid" or "Invalid". This is only a simple check, not full
       email validation.

    Example terminal session:
    Address: ana@example.com
    Valid

    Example terminal sessions for invalid addresses:
    Address: ana@
    Invalid

    Address: a@@b
    Invalid

25. COUNT A WORD
    a. Start with sentence = "The red box is red".
    b. Ask for a word using input("Word: "). Count matching complete
       whitespace-separated words, ignoring uppercase and lowercase.
       Do not count part of a word.
    c. Print the count as a number.

    Example terminal session:
    Word: RED
    2

    Another example terminal session:
    Word: ed
    0

26. CHECK FOR A PALINDROME
    a. Ask for a phrase using input("Phrase: ").
    b. Remove spaces, ignore uppercase and lowercase, and compare the
       resulting text with its reverse. Do not remove punctuation.
    c. Print the Boolean result, True or False.

    Example terminal session:
    Phrase: Never odd or even
    True

    Another example terminal session:
    Phrase: hello
    False

27. CLEAN AND REJOIN ITEMS
    a. Start with raw = "  north ; ; SOUTH; east  ".
    b. Split on semicolons, strip each part, and discard empty parts.
    c. Convert the remaining parts to title case, join them with a comma
       and one space, and print the result.

    Expected terminal output:
    North, South, East

28. MAKE INITIALS
    a. Ask for a full name using input("Full name: "). Strip the input and
       split it into words, treating any run of whitespace as a separator.
    b. Take the first letter of each word, convert it to uppercase, and
       join the letters with periods. Do not add a period at the end.
    c. If there are no words, print "No name" instead.

    Example terminal session:
    Full name:   ada  lovelace
    A.L

    Example terminal session when Enter is pressed without typing a name:
    Full name:
    No name

29. SHORTEN A STRING
    a. Ask for a sentence using input("Sentence: "), then ask for a maximum
       length using input("Maximum length: "). Assume the length is a valid
       non-negative whole number.
    b. If the sentence is longer than the maximum, print only its first
       maximum-length characters followed by three periods.
    c. Otherwise, print the sentence unchanged. The three periods are
       additional to the maximum number of original characters.

    Example terminal session:
    Sentence: Python
    Maximum length: 3
    Pyt...

    Another example terminal session:
    Sentence: Cat
    Maximum length: 3
    Cat

30. CREATE A NAME BADGE
    a. Ask for a name using input("Name: ") and a role using input("Role: ").
       Remove surrounding whitespace from both.
    b. Print a border of exactly 30 asterisks. Below it, print the name
       and role on separate lines, each centered in a field 30 characters
       wide. Finish with another 30-asterisk border.
    c. For this task, assume neither input is longer than 30 characters.
       The spaces at the right of each centered line may not be visible.

    Example terminal session:
    Name: Sam
    Role: Technician
    ******************************
                 Sam
              Technician
    ******************************

============================================================
ADVANCED STRING FORMATTING
============================================================

Return to tasks 31-33 after completing the other string tasks.

For these tasks, construct the lines using strings and print each line.
Use ljust(), rjust() and center() rather than counting spaces by hand.
Each field width includes the characters in that field. Join the fields
directly, without adding extra separators. All sample values fit their
fields; trailing spaces on centered lines may not be visible in the terminal.

31. CLOUD SERVICES INVOICE
    a. Print a border of 62 "=" characters. Center each of these strings in
       a field 62 characters wide, on its own line:
       "ACME CLOUD SERVICES", "INVOICE #INV-00419", "2026-11-24 22:41".
       Print another 62-character "=" border below them. The date and time
       are fixed strings for this exercise.
    b. Create a heading and three rows using four fields, in this order:
       - SKU: width 9, left-aligned.
       - Description: width 28, left-aligned.
       - Qty: width 5, right-aligned.
       - Total: width 20, right-aligned.
       Print a 62-character "-" line between the heading and rows.
    c. Use the data below. The totals are already calculated; display each
       with a dollar sign and exactly two decimal places. Convert quantities
       to strings before aligning them.

       SKU    Description                  Qty   Total
       #0104  Cloud Server Hosting (Pro)     2   $299.98
       #0209  Dedicated SSL Certificate      1   $59.50
       #0088  Enterprise Support & SLA      12   $300.00

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

32. TECHNICIAN WORK ORDER
    a. Print a 50-character "=" border. Center "ACME TECH SERVICES" and
       "WORK ORDER #WO-071" on separate lines, each in a field of width 50.
       Print a second "=" border of the same width.
    b. Print a heading and rows using these field widths and alignments:
       Job 8 left, Service 24 left, Hours 6 right, Charge 12 right.
       Place a 50-character "-" line between the heading and rows.
    c. Format the following values as dollar amounts with two decimals:

       Job   Service              Hours  Charge
       #101  Network diagnosis        2  $180.00
       #102  Router setup             1  $120.00
       #103  Equipment testing        3  $225.00

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

33. STOCK VALUE REPORT
    a. Print a 48-character "=" border, "STOCK VALUE REPORT" centered in
       width 48, and another "=" border.
    b. Print a heading and rows with these widths and alignments:
       Item 20 left, Qty 6 right, Unit price 11 right, Value 11 right.
       Print a 48-character "-" line between the heading and rows.
    c. Use the values below and display every amount with a dollar sign and
       two decimal places. Print another "-" line after the rows. On the last
       line, left-align "Total stock value:" in width 37 and right-align
       "$205.00" in width 11.

       Item              Qty  Unit price  Value
       Ethernet Cable      4      $12.50  $50.00
       Wireless Mouse      3      $25.00  $75.00
       USB Hub             2      $40.00  $80.00

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
MORE STRING PRACTICE
============================================================

34. EXTRACT A DOMAIN
    a. Store "sam@example.com" in address. Split at "@".
    b. Print the part after the "@". Assume exactly one "@" is present.

    Expected terminal output:
    example.com

35. REMOVE A PREFIX
    a. Start with "ID-2048". Remove "ID-" only if it is at the beginning.
    b. Print the remaining text. Do not remove matching text elsewhere.

    Expected terminal output:
    2048

36. COUNT VOWELS
    a. Start with "Automation". Count a, e, i, o and u, ignoring case.
    b. Print the count as shown.

    Expected terminal output:
    Vowels: 6

37. REVERSE A CODE
    a. Store "AB-123". Use slicing to reverse the entire string.
    b. Print the reversed string.

    Expected terminal output:
    321-BA

38. REPLACE A FILE SUFFIX
    a. Start with "report.txt". If it ends in ".txt", replace only that
       suffix with ".csv". Print the result; otherwise print it unchanged.

    Expected terminal output:
    report.csv

39. CLEAN A PHONE NUMBER
    a. Start with "+47 123-45-678". Keep only the digits, in their original
       order, and print them. Treat each character independently.

    Expected terminal output:
    4712345678

40. CHECK A SERIAL NUMBER
    a. Ask for a serial using input("Serial: "). Strip whitespace.
    b. Print "Valid" if it contains exactly four digits, otherwise "Invalid".

    Example terminal session:
    Serial: 0421
    Valid

    Another example terminal session:
    Serial: 04A1
    Invalid

41. HIDE PART OF AN IDENTIFIER
    a. Start with "12345678". Replace every character except the last four
       with "*". Assume the identifier contains at least four characters.
    b. Print the masked result.

    Expected terminal output:
    ****5678

42. NORMALIZE A PRODUCT CODE
    a. Start with "  ab- 123 ". Strip its outer whitespace, remove all
       remaining spaces, and convert the result to uppercase.
    b. Print the cleaned code.

    Expected terminal output:
    AB-123

43. FIND A CHARACTER POSITION
    a. Start with "support@example.com". Find the zero-based index of "@".
    b. Print the index. Assume the character occurs exactly once.

    Expected terminal output:
    7

44. CHECK A PREFIX
    a. Ask for a ticket using input("Ticket: "). Strip surrounding spaces.
    b. Print "Support" when it starts with "SUP-", ignoring case; otherwise
       print "Other". Do not match the prefix in the middle of the string.

    Example terminal session:
    Ticket: sup-103
    Support

    Another example terminal session:
    Ticket: INV-103
    Other

45. COUNT LINES IN TEXT
    a. Create a string with three lines: "red", "blue" and "green".
    b. Split it into lines and print the number of lines.

    Expected terminal output:
    Lines: 3

46. FORMAT A PERCENTAGE
    a. Store 0.875 as a decimal fraction. Convert it to a percentage.
    b. Print it with one decimal place and a percent sign.

    Expected terminal output:
    87.5%

47. PAD A NUMBER WITH ZEROES
    a. Store the integer 42. Convert it to a string and use zfill() to make
       it five characters wide. Print the result.

    Expected terminal output:
    00042

48. CLEAN A DELIMITED LIST
    a. Start with " red, ,BLUE, green ". Split on commas, strip each part,
       skip empty parts, and convert the remaining parts to lowercase.
    b. Join them with " / " and print the result.

    Expected terminal output:
    red / blue / green

49. FIND THE LONGEST WORD
    a. Split "small medium extraordinary" into words. Find the longest.
       If two words tie, keep the first one.
    b. Print the word and its length on separate lines.

    Expected terminal output:
    extraordinary
    13

50. BUILD AN INITIALS LABEL
    a. Start with "  grace   hopper ". Split on whitespace, uppercase the
       first character of each word, and join the initials with "-".
    b. Print the result.

    Expected terminal output:
    G-H

51. FORMAT A PRODUCT LINE
    a. Use name "Cable" and price 12.5. Left-align the name in width 12 and
       right-align the price, formatted as "$12.50", in width 10.
    b. Join the fields directly and print the line.

    Expected terminal output:
    Cable           $12.50

52. REPORT A SEARCH RESULT
    a. Store "Cloud backup complete" as the message. Ask for a search term
       using input("Search: "). Check for it ignoring case.
    b. Print "Found" or "Not found". An empty search term is considered
       invalid: print "Empty search" instead.

    Example terminal session:
    Search: BACKUP
    Found

    Another example terminal session:
    Search: server
    Not found

53. CENTER A SECTION HEADING
    a. Print a 40-character line of "=". Center "SERVICE REPORT" in width 40
       on the next line, then print another 40-character "=" line.
    b. Do not add spaces outside the centered field.

    Expected terminal output:
    ========================================
                 SERVICE REPORT
    ========================================
"""
