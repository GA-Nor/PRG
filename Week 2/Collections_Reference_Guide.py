"""
COLLECTIONS REFERENCE GUIDE
============================

A comprehensive reference for all methods and operations
for Lists, Tuples, Sets, and Dictionaries in Python.

Use this file as a quick lookup guide while coding!

CONTENT INDEX:
====================
1. LISTS - COMPLETE METHOD REFERENCE - Creating, Accessing, Searching, Modifying, Ordering, Copying

2. TUPLES - COMPLETE METHOD REFERENCE - Creating, Accessing, Searching, Unpacking
   
3. SETS - COMPLETE METHOD REFERENCE - Creating, Searching, Modifying, Set Operations
   
4. DICTIONARIES - COMPLETE METHOD REFERENCE - Creating, Accessing, Searching, Modifying, Copying
   
5. QUICK COMPARISON TABLE - Feature comparison: List vs Tuple vs Set vs Dictionary
   
6. WHEN TO USE WHAT - Decision guide for choosing the right collection type
   
7. CONVERTING BETWEEN TYPES - How to convert from one type to another
"""

# ==================================================
# LISTS - Method Reference
# ==================================================

"""
CREATING LISTS:
  my_list = []                    # Empty list
  my_list = [1, 2, 3]            # List with values
  my_list = list()               # Empty list (alternative)
  my_list = list(range(5))       # [0, 1, 2, 3, 4]

ACCESSING ELEMENTS:
  my_list[0]                     # First element
  my_list[-1]                    # Last element
  my_list[1:3]                   # Slice: elements at index 1, 2

SEARCHING & CHECKING:
  value in my_list               # Check if exists (returns True/False)
  my_list.index(value)           # Return index of first occurrence
  my_list.count(value)           # Count occurrences of value

MODIFYING LISTS:
  my_list.append(value)          # Add single item at end
  my_list.extend([x, y, z])      # Add multiple items at end
  my_list.insert(index, value)   # Insert at specific position
  my_list.remove(value)          # Remove first occurrence (error if not found)
  my_list.pop()                  # Remove & return last item
  my_list.pop(index)             # Remove & return item at index
  my_list.clear()                # Remove all items

ORDERING:
  my_list.sort()                 # Sort in ascending order (modifies list)
  my_list.sort(reverse=True)     # Sort in descending order
  my_list.reverse()              # Reverse order

COPYING:
  new_list = my_list.copy()      # Create a copy
  new_list = my_list[:]          # Create a copy (slice syntax)

LENGTH:
  len(my_list)                   # Return number of items

SEARCHING WITH FILTERING:
  filtered = [x for x in my_list if x > 10]  # List comprehension

EXAMPLES:
"""
print("1. LISTS - METHOD REFERENCE")
print("=" * 70)
fruits = ["apple", "banana", "cherry", "apple", "date"]
print(f"List: {fruits}")
print()

fruits.append("elderberry")
print(f"After .append('elderberry'): {fruits}")

fruits.extend(["fig", "grape"])
print(f"After .extend(['fig', 'grape']): {fruits}")

fruits.insert(2, "blueberry")
print(f"After .insert(2, 'blueberry'): {fruits}")

fruits.remove("apple")
print(f"After .remove('apple'): {fruits}")

removed = fruits.pop()
print(f"After .pop(): {fruits}")
print(f"Removed item: {removed}")

pos = fruits.index("cherry")
print(f"Index of 'cherry': {pos}")

count = fruits.count("apple")
print(f"Count of 'apple': {count}")

test_list = [1, 2, 3, 4, 5]
test_list.reverse()
print(f"[1, 2, 3, 4, 5] reversed: {test_list}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"[3, 1, 4, 1, 5, 9, 2, 6] sorted: {numbers}")

print()
print()


# ==================================================
# TUPLES - Complete Method Reference
# ==================================================

print("2. TUPLES - METHOD REFERENCE")
print("=" * 70)
"""
CREATING TUPLES:
  my_tuple = ()                  # Empty tuple
  my_tuple = (1, 2, 3)           # Tuple with values
  my_tuple = tuple()             # Empty tuple (alternative)
  my_tuple = (1,)                # Single item tuple (note the comma!)
  my_tuple = tuple([1, 2, 3])    # Convert list to tuple

ACCESSING ELEMENTS:
  my_tuple[0]                    # First element
  my_tuple[-1]                   # Last element
  my_tuple[1:3]                  # Slice: elements at index 1, 2

SEARCHING & CHECKING:
  value in my_tuple              # Check if exists (returns True/False)
  my_tuple.index(value)          # Return index of first occurrence
  my_tuple.count(value)          # Count occurrences of value

UNPACKING:
  a, b, c = my_tuple             # Unpack into variables
  x, *y, z = my_tuple            # Unpack with * for multiple items

LENGTH:
  len(my_tuple)                  # Return number of items

CONVERTING:
  my_list = list(my_tuple)       # Convert tuple to list

CHARACTERISTICS:
  - Immutable (cannot change, add, or remove items)
  - Use parentheses: (1, 2, 3)
  - Methods: index(), count() only
  - Faster and use less memory than lists
  - Can be used as dictionary keys
  - Return multiple values from functions

EXAMPLES:
"""

colors = ("red", "green", "blue", "red", "yellow")
print(f"Tuple: {colors}")
print()

pos = colors.index("red")
print(f".index('red'): {pos}")

count = colors.count("red")
print(f".count('red'): {count}")

if "blue" in colors:
    print(f"'blue' is in tuple: True")

person = ("Alice", 28, "Engineer")
name, age, job = person
print(f"Unpacked: name={name}, age={age}, job={job}")

print()
print()


# ==================================================
# SETS - Complete Method Reference
# ==================================================

print("3. SETS - METHOD REFERENCE")
print("=" * 70)
"""
CREATING SETS:
  my_set = set()                 # Empty set
  my_set = {1, 2, 3}             # Set with values
  my_set = {1, 1, 2, 2, 3}       # Duplicates automatically removed -> {1, 2, 3}
  my_set = set([1, 2, 3])        # Convert list to set

SEARCHING & CHECKING:
  value in my_set                # Check if exists (returns True/False)

MODIFYING SETS:
  my_set.add(value)              # Add single item
  my_set.remove(value)           # Remove item (error if not found)
  my_set.discard(value)          # Remove item (no error if not found)
  my_set.pop()                   # Remove & return arbitrary item
  my_set.clear()                 # Remove all items

SET OPERATIONS:
  set1.union(set2)               # All items from both sets
  set1 | set2                    # Same as union (using | operator)
  
  set1.intersection(set2)        # Only items in both sets
  set1 & set2                    # Same as intersection (using & operator)
  
  set1.difference(set2)          # Items in set1 but not in set2
  set1 - set2                    # Same as difference (using - operator)
  
  set1.symmetric_difference(set2) # Items in either set but not both
  set1 ^ set2                    # Same as symmetric_difference
  
  set1.issubset(set2)            # Check if all items in set1 are in set2
  set1 <= set2                   # Same as issubset
  
  set1.issuperset(set2)          # Check if set1 contains all items of set2
  set1 >= set2                   # Same as issuperset

COPYING:
  new_set = my_set.copy()        # Create a copy

LENGTH:
  len(my_set)                    # Return number of items

CHARACTERISTICS:
  - Unordered (no index positions)
  - Unique items only (duplicates removed)
  - Use curly braces: {1, 2, 3}
  - Fast membership testing
  - Use for: Removing duplicates, finding relationships

EXAMPLES:
"""

team_a_skills = {"Python", "JavaScript", "SQL", "Git", "Docker"}
team_b_skills = {"Java", "Python", "Git", "AWS", "Kubernetes"}
team_c_skills = {"Python", "Go", "SQL", "Rust"}

print(f"Team A: {team_a_skills}")
print(f"Team B: {team_b_skills}")
print(f"Team C: {team_c_skills}")
print()

common_ab = team_a_skills.intersection(team_b_skills)
print(f"Common to A & B: {common_ab}")

common_all = team_a_skills.intersection(team_b_skills, team_c_skills)
print(f"Common to all: {common_all}")

unique_to_a = team_a_skills.difference(team_b_skills, team_c_skills)
print(f"Unique to A: {unique_to_a}")

all_unique_skills = team_a_skills.union(team_b_skills, team_c_skills)
print(f"All skills: {all_unique_skills}")

colors = {"red", "green", "blue"}
print(f"'red' in colors: {'red' in colors}")
print(f"'yellow' in colors: {'yellow' in colors}")

colors.add("yellow")
print(f"After .add('yellow'): {colors}")

colors.remove("blue")
print(f"After .remove('blue'): {colors}")

print()
print()


# ==================================================
# DICTIONARIES - Method Reference
# ==================================================

print("4. DICTIONARIES - COMPLETE METHOD REFERENCE")
print("=" * 70)
"""
CREATING DICTIONARIES:
  my_dict = {}                   # Empty dictionary
  my_dict = {"key": value}       # Dictionary with items
  my_dict = dict()               # Empty dictionary (alternative)
  my_dict = dict(key=value)      # Dictionary with keyword arguments

ACCESSING VALUES:
  my_dict["key"]                 # Get value (error if key not found)
  my_dict.get("key")             # Get value (returns None if not found)
  my_dict.get("key", default)    # Get value with default if not found

CHECKING KEYS:
  "key" in my_dict               # Check if key exists (returns True/False)
  "key" not in my_dict           # Check if key doesn't exist

SEARCHING & GETTING INFORMATION:
  my_dict.keys()                 # Return all keys
  my_dict.values()               # Return all values
  my_dict.items()                # Return all key-value pairs as tuples

MODIFYING DICTIONARIES:
  my_dict["key"] = value         # Add or update key-value pair
  my_dict.update({"key": value}) # Add multiple key-value pairs
  my_dict.update(other_dict)     # Merge another dictionary
  my_dict.pop("key")             # Remove & return value (error if not found)
  my_dict.pop("key", default)    # Remove & return value with default
  del my_dict["key"]             # Delete key-value pair (error if not found)
  my_dict.clear()                # Remove all items

COPYING:
  new_dict = my_dict.copy()      # Create a copy (shallow copy)

LENGTH:
  len(my_dict)                   # Return number of key-value pairs

SEARCHING:
  Search by key (fast):          my_dict[key] or my_dict.get(key)
  Search by value (slow):        [k for k, v in my_dict.items() if v == value]
  Find max/min values:           max(my_dict, key=my_dict.get)

CHARACTERISTICS:
  - Mutable (can change, add, remove)
  - Keys must be unique and immutable (strings, numbers, tuples)
  - Values can be any type
  - Ordered (maintains insertion order in Python 3.7+)
  - Fast key-based lookups
  - Use for: Storing structured data, mapping relationships

EXAMPLES:
"""

student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"Dictionary: {student_grades}")
print()

print(f".keys(): {list(student_grades.keys())}")
print(f".values(): {list(student_grades.values())}")
print(f".items(): {list(student_grades.items())}")

grade = student_grades.get("Alice")
print(f".get('Alice'): {grade}")

grade = student_grades.get("David", "Not found")
print(f".get('David', 'Not found'): {grade}")

student_grades["David"] = 90
print(f"After adding David: {student_grades}")

removed = student_grades.pop("Bob")
print(f"After .pop('Bob'): dict = {student_grades}, removed = {removed}")

student_grades.update({"Bob": 87, "Eve": 94})
print(f"After .update(...): {student_grades}")

sales_data = {
    "Monday": 450,
    "Tuesday": 320,
    "Wednesday": 580,
    "Thursday": 420,
    "Friday": 650
}

print(f"\nSales Data: {sales_data}")
print(f"Total: ${sum(sales_data.values())}")
print(f"Highest Day: {max(sales_data, key=sales_data.get)} (${sales_data[max(sales_data, key=sales_data.get)]})")
print(f"Lowest Day: {min(sales_data, key=sales_data.get)} (${sales_data[min(sales_data, key=sales_data.get)]})")

print()
print()


# ==================================================
# QUICK COMPARISON TABLE
# ==================================================

print("5. QUICK COMPARISON TABLE")
print("=" * 70)
print("""
╔════════════╦═══════════════╦════════════╦═══════════╦════════════════╗
║ Feature    ║ List          ║ Tuple      ║ Set       ║ Dictionary     ║
╠════════════╬═══════════════╬════════════╬═══════════╬════════════════╣
║ Syntax     ║ [1, 2, 3]     ║ (1, 2, 3)  ║ {1, 2, 3} ║ {"k": "v"}     ║
║ Mutable    ║ Yes           ║ No         ║ Yes       ║ Yes            ║
║ Ordered    ║ Yes           ║ Yes        ║ No        ║ Yes (3.7+)     ║
║ Duplicates ║ Allowed       ║ Allowed    ║ No        ║ No (keys)      ║
║ Indexing   ║ Yes           ║ Yes        ║ No        ║ No             ║
║ Use Case   ║ Sequences     ║ Fixed data ║ Unique    ║ Key-value      ║
║            ║ that change   ║ returns    ║ items     ║ mapping        ║
║ Speed      ║ Slow          ║ Fast       ║ Fast      ║ Very Fast      ║
╚════════════╩═══════════════╩════════════╩═══════════╩════════════════╝
""")

print()
print()


# ==================================================
# WHEN TO USE WHAT
# ==================================================

print("6. WHEN TO USE WHAT")
print("=" * 70)
print("""
USE LISTS WHEN:
  - You need an ordered collection of items
  - Items will change (add, remove, modify)
  - You need to access items by position (index)
  - Duplicates are allowed or needed
  - Examples: scores, names, to-do lists

USE TUPLES WHEN:
  - Data should not change after creation
  - You need to return multiple values from a function
  - You want to use data as a dictionary key
  - You need better performance (read-only)
  - Examples: coordinates, database records, function returns

USE SETS WHEN:
  - You only care about unique items
  - You need to check membership frequently
  - You need set operations (union, intersection, difference)
  - You want to remove duplicates from a list
  - Performance is important
  - Examples: skills, tags, user IDs

USE DICTIONARIES WHEN:
  - You need to look up values by a key
  - You want to store structured, related data
  - You need key-value associations
  - Performance of lookups is important
  - Examples: user profiles, configuration, inventory
""")

print()
print()


# ==================================================
# CONVERSION BETWEEN TYPES
# ==================================================

print("7. CONVERTING BETWEEN TYPES")
print("=" * 70)
print("""
LIST TO TUPLE:              my_tuple = tuple(my_list)
TUPLE TO LIST:              my_list = list(my_tuple)
LIST TO SET:                my_set = set(my_list)
SET TO LIST:                my_list = list(my_set)
DICT TO LIST (keys):        my_list = list(my_dict.keys())
DICT TO LIST (values):      my_list = list(my_dict.values())
DICT TO LIST (items):       my_list = list(my_dict.items())

EXAMPLES:
""")

print(f"[1, 2, 3] -> tuple: {tuple([1, 2, 3])}")
print(f"(1, 2, 3) -> list: {list((1, 2, 3))}")
print(f"[1, 1, 2, 2, 3] -> set: {set([1, 1, 2, 2, 3])}")
print(f"{{'a': 1, 'b': 2}} -> keys: {list({'a': 1, 'b': 2}.keys())}")


