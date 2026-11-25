"""
TEXT AND CSV FILE PRACTICE: 50 TASKS

Write a separate program for each task. Run it with the Practice Tasks folder
as the working directory. Several tasks use the provided Sample Data folder;
do not change those original files. For example, pathlib can refer to a file
there with Path("Sample Data") / "names.txt". Use UTF-8 for all text files.

Use built-in open() and, if needed, os or pathlib.Path. Do not use the csv
module or other libraries. These exercises use simple CSV: commas separate
fields, and fields contain no commas, quotes or line breaks. Splitting on
commas is NOT a general CSV parser and does not handle quoted CSV fields.

Each task that creates a new file should use exclusive creation ("x") and
print "File already exists" if the target already exists. This prevents
accidental overwrites. If another file error occurs, print a helpful error
instead of silently failing. Append tasks must modify only the task-specific
file they create, never the provided samples. Before repeating an exercise,
choose a fresh practice directory or remove only your own output file.

Terminal examples assume output files do not already exist. The four spaces
before each example line only indent it here; do not print them. For input
tasks, text after a prompt is what the user types. File-content examples
show actual lines in the file, not additional terminal output.

For example, input("Name: ") displays "Name: " and waits for input. In the
example "Name: Bo", the user typed "Bo"; quotation marks are not printed.

============================================================
TEXT FILES - BASIC
============================================================

01. WRITE AND READ A NOTE
    a. Create task01_note.txt containing "Hello, file!" without a newline.
    b. Read the file and print its contents.

    Expected terminal output:
    Hello, file!

    Expected task01_note.txt contents:
    Hello, file!

02. WRITE SEVERAL LINES
    a. Create task02_colours.txt containing red, blue and green, each on a
       separate line. b. Read it and print each line without extra blank lines.

    Expected terminal output and file contents:
    red
    blue
    green

03. APPEND TEXT
    a. Create task03_greeting.txt containing "Hello", without a newline.
    b. Open that task-specific file in append mode and add " world".
    c. Read and print the final contents.

    Expected terminal output and final file contents:
    Hello world

04. COUNT FILE CHARACTERS
    a. Create task04_sample.txt containing exactly "Python", without a newline.
    b. Read the whole file and print the number of characters.

    Expected terminal output:
    6

05. COUNT LINES IN A SAMPLE FILE
    a. Read the provided names.txt in the Sample Data folder.
    b. Loop through its lines and print the number of lines.

    Expected terminal output:
    Lines: 3

06. STRIP EACH LINE
    a. Create task06_spaces.txt with the lines "  Ana  ", " Bo " and "Kim".
       The quotes show the spaces and are not part of the file.
    b. Strip each line and print it in square brackets, as shown.

    Expected terminal output:
    [Ana]
    [Bo]
    [Kim]

07. SKIP BLANK LINES
    a. Create task07_notes.txt containing "one", an empty line, and "two".
    b. Print only the non-empty lines, without extra blank lines.

    Expected terminal output:
    one
    two

08. CHECK BEFORE READING
    a. Ask for a filename using input("Filename: "). Check whether it is an
       existing file in the current working directory using Path.is_file()
       or os.path.isfile().
    b. If it exists, read and print its contents. Otherwise print "File not
       found". Still handle a read error: a file may become unavailable
       after the check.
    c. Test with task08_missing.txt, making sure no such file exists first.

    Example terminal session:
    Filename: task08_missing.txt
    File not found

09. WRITE A USER'S NOTE
    a. Ask for a new filename using input("Filename: ") and a one-line
       message using input("Message: ").
    b. Create the file with the message, then read it back and print it.
       If it exists, do not overwrite it; print "File already exists".

    Example terminal session:
    Filename: task09_memo.txt
    Message: Remember
    Remember

    Expected task09_memo.txt contents:
    Remember

10. COPY A SAMPLE FILE
    a. Read names.txt from Sample Data. Check whether task10_copy.txt exists.
    b. If it exists, print "File already exists" and leave it unchanged.
       Otherwise create it exclusively with the exact contents of names.txt,
       then print "Copy created". Handle read and write errors as well.

    Expected terminal output:
    Copy created

    Expected task10_copy.txt contents:
    Ana
    Bo
    Kim

============================================================
TEXT FILES - DEVELOPING
============================================================

11. ADD NUMBERS FROM A FILE
    a. Read the provided scores.txt from Sample Data. Each line is an integer.
    b. Convert the lines to numbers, add them, and print the total.

    Expected terminal output:
    Total: 30

12. AVERAGE FILE VALUES
    a. Read the provided scores.txt from Sample Data.
    b. Print the average to one decimal place. If there are no lines,
       print "No scores" rather than dividing by zero.

    Expected terminal output:
    Average: 10.0

13. CLEAN SAMPLE NAMES
    a. Read the provided messy_names.txt from Sample Data.
    b. Strip and title-case each line, skip empty lines, and print the names.

    Expected terminal output:
    Ana
    Bo

14. SEARCH A NAME FILE
    a. Check that the provided names.txt in Sample Data exists as a file.
       If not, print "File not found" and stop.
    b. Ask for a name using input("Name: "). Read the file and search,
       ignoring case and surrounding whitespace. Print "Found" or "Not found".

    Example terminal session:
    Name:  BO
    Found

    Another example terminal session:
    Name: Eve
    Not found

15. NUMBER THE LINES
    a. Read the provided names.txt from Sample Data.
    b. Print each name with its line number, starting at 1.

    Expected terminal output:
    1. Ana
    2. Bo
    3. Kim

16. SAVE CLEAN NAMES
    a. Read messy_names.txt from Sample Data. Strip and title-case each
       non-empty line. b. Write the cleaned names, one per line, to a new
       task16_cleaned.txt. Do not alter the sample file.
    c. Print "Saved" after the file is written.

    Expected terminal output:
    Saved

    Expected task16_cleaned.txt contents:
    Ana
    Bo

17. FIND THE LONGEST WORD
    a. Create task17_words.txt with cat, elephant and dog on separate lines.
    b. Read the file and print the longest word; if tied, use the first.
       If the file is empty, print "No words".

    Expected terminal output:
    elephant

18. COUNT REPEATED ITEMS
    a. Read items.txt from Sample Data and count each item in a dictionary.
    b. Print each item and count in alphabetical order.

    Expected terminal output:
    paper: 1
    pen: 2
    tape: 1

19. APPEND A LOG ENTRY
    a. Create task19_log.txt containing exactly "Start", with no newline.
    b. Append a newline and "Done". Read and print both lines.

    Expected terminal output and final file contents:
    Start
    Done

20. CHECK A PATH AND EXTENSION
    a. Before running the program, create task20_report.txt for the first
       test. Ensure task20_missing.csv does not exist for the second test.
    b. Ask for a filename using input("Filename: "). Use Path or os.path to
       print whether it exists in the current working directory and its
       extension.

    Example terminal session:
    Filename: task20_report.txt
    Exists: True
    Extension: .txt

    Another example terminal session:
    Filename: task20_missing.csv
    Exists: False
    Extension: .csv

============================================================
SIMPLE CSV FILES
============================================================

21. READ A CSV FILE
    a. Read the provided people.csv from Sample Data, including its header.
    b. Print every line without adding extra blank lines.

    Expected terminal output:
    name,role
    Ana,technician
    Bo,trainee

22. SPLIT A CSV ROW
    a. Read people.csv from Sample Data. Skip the header and take the first
       data row. Split it at the comma.
    b. Print the name and role with labels as shown.

    Expected terminal output:
    Name: Ana
    Role: technician

23. PRINT A CSV COLUMN
    a. Read products.csv from Sample Data and skip its header.
    b. Split each data row and print only the product name.

    Expected terminal output:
    pen
    paper

24. TOTAL CSV PRICES
    a. Read products.csv from Sample Data. Skip the header, split each row,
       and convert the price column to an integer.
    b. Add the prices, not the quantities, and print their sum.

    Expected terminal output:
    Total: 17

25. WRITE A CSV FILE
    a. Create task25_team.csv with header name,role and two rows from the
       tuples ("Ana", "technician") and ("Bo", "trainee"). Join the fields
       with commas and write each row on its own line.
    b. Print "Saved" after writing.

    Expected terminal output:
    Saved

    Expected task25_team.csv contents:
    name,role
    Ana,technician
    Bo,trainee

26. APPEND A CSV ROW
    a. Create task26_stock.csv with the header item,quantity and row pen,3.
    b. Append paper,5 on its own line. Add a line break first if needed.
    c. Read and print the resulting file.

    Expected terminal output and final file contents:
    item,quantity
    pen,3
    paper,5

27. FILTER CSV QUANTITIES
    a. Read stock.csv from Sample Data. Skip its header and convert each
       quantity to an integer. b. Print items with quantity at least 3.

    Expected terminal output:
    pen: 3
    paper: 5

28. CALCULATE INVENTORY VALUE
    a. Read products.csv from Sample Data. For each data row, multiply the
       integer price by the integer quantity.
    b. Add the row values and print the overall value.

    Expected terminal output:
    Total value: 39

29. CLEAN A CSV FILE
    a. Read messy_people.csv from Sample Data. Strip both fields of each
       data row and title-case the names.
    b. Write the same header and cleaned rows to a new task29_cleaned.csv.
       Print "Saved". Do not modify the sample.

    Expected terminal output:
    Saved

    Expected task29_cleaned.csv contents:
    name,role
    Ana,trainee
    Bo,technician

30. FIND A STOCK ITEM
    a. Check that stock.csv in Sample Data exists as a file. If it is
       missing, print "File not found" and stop.
    b. Ask for an item using input("Item: ") and search the data rows,
       ignoring case and surrounding whitespace. Print its quantity or
       "Item not found".

    Example terminal session:
    Item:  PEN
    Quantity: 3

    Another example terminal session:
    Item: drill
    Item not found

============================================================
REVIEW AND CONSOLIDATION
============================================================

Tasks 31-50 revisit text and CSV skills at mixed difficulty. Use them to
reinforce earlier tasks; they are not a new advanced section.

31. PRINT THE FIRST NAME
    Read names.txt from Sample Data and print its first line without the
    newline. If the file is empty, print "No names".

    Expected terminal output:
    Ana

32. PRINT NAMES IN UPPERCASE
    Read names.txt from Sample Data. Strip each line and print it in uppercase.

    Expected terminal output:
    ANA
    BO
    KIM

33. COUNT SCORES ABOVE A LIMIT
    Read integer scores from scores.txt in Sample Data. Count and print
    the scores greater than 8.

    Expected terminal output:
    Count: 2

34. FIND THE HIGHEST SCORE
    Read scores.txt from Sample Data and print the highest integer. If the
    file contains no scores, print "No scores".

    Expected terminal output:
    Highest: 15

35. WRITE A TITLE
    Create task35_title.txt with the single line "DAILY REPORT". Print
    "Saved" after writing the file.

    Expected terminal output:
    Saved

    Expected task35_title.txt contents:
    DAILY REPORT

36. COUNT UNIQUE ITEMS
    Read items.txt from Sample Data. Strip each line and use a set to find
    the number of unique items. Print the count.

    Expected terminal output:
    Unique: 3

37. LIST UNIQUE ITEMS
    Read items.txt from Sample Data. Print each distinct item once, in
    alphabetical order.

    Expected terminal output:
    paper
    pen
    tape

38. FIND A NAME PREFIX
    Read names.txt from Sample Data and print names starting with "K".
    Match case exactly.

    Expected terminal output:
    Kim

39. WRITE SCORES TO A NEW FILE
    Read scores.txt from Sample Data. Write scores greater than 8, one per
    line in input order, to task39_high_scores.txt. Print "Saved".

    Expected terminal output:
    Saved

    Expected task39_high_scores.txt contents:
    10
    15

40. CHECK A SAMPLE FILE
    Check whether names.txt in Sample Data is an existing file using Path
    or os.path. Print the Boolean result. Do not modify the sample.

    Expected terminal output:
    Exists: True

41. PRINT PEOPLE'S ROLES
    Read people.csv from Sample Data. Skip the header and print the role
    from each data row, in file order.

    Expected terminal output:
    technician
    trainee

42. COUNT CSV RECORDS
    Read people.csv from Sample Data. Skip the header and count the data
    rows. Print the count.

    Expected terminal output:
    Records: 2

43. FIND A CSV PERSON
    Read people.csv from Sample Data. Print the role for the exact name
    "Bo". If no row matches, print "Not found".

    Expected terminal output:
    trainee

44. PRINT STOCK QUANTITIES
    Read stock.csv from Sample Data. Skip the header and print each quantity
    in file order.

    Expected terminal output:
    3
    5
    2

45. TOTAL STOCK QUANTITIES
    Read stock.csv from Sample Data. Convert each quantity to an integer,
    add them, and print the total.

    Expected terminal output:
    Total: 10

46. WRITE A CSV SUMMARY
    Read stock.csv from Sample Data. Write task46_summary.csv with header
    "item,quantity" and only rows with quantity below 3. Preserve input order.
    Print "Saved" after writing.

    Expected terminal output:
    Saved

    Expected task46_summary.csv contents:
    item,quantity
    tape,2

47. PRINT PRODUCT VALUES
    Read products.csv from Sample Data. For each data row, multiply the
    integer price by the integer quantity and print the product and value.

    Expected terminal output:
    pen: 15
    paper: 24

48. FIND THE MOST EXPENSIVE PRODUCT
    Read products.csv from Sample Data and print the product with the highest
    integer unit price. If tied, keep the first; if there are no data rows,
    print "No products".

    Expected terminal output:
    paper

49. CHECK BEFORE CREATING
    Check whether task49_report.txt exists. If it does, print "File already
    exists" and do not change it. Otherwise create it exclusively with the
    text "Ready" and print "Created". Handle creation errors as described
    at the start of this file.

    Expected terminal output when the file does not exist:
    Created

    Expected task49_report.txt contents:
    Ready

    Expected terminal output on a later run:
    File already exists

50. COPY SELECTED CSV COLUMNS
    Read products.csv from Sample Data. Create task50_names_prices.csv with
    the header "name,price" and the first two fields from each data row.
    Preserve row order and print "Saved".

    Expected terminal output:
    Saved

    Expected task50_names_prices.csv contents:
    name,price
    pen,5
    paper,12
"""
