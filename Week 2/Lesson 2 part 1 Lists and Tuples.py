"""
COLLECTIONS PART 1
=========================

- Lists: Ordered, mutable collections with duplicates
- Tuples: Ordered, immutable collections with duplicates  

"""

# ==================================================
# 1. LISTS - Mutable, flexible
# ==================================================

#create a list of scores
scores = [95, 87, 92, 88, 95, 76, 90, 87,100, 32, 16]
#print the scores
print(f"Scores: {scores}\n")
print("first element in the list", scores[0])

#Find specific item
#if specific score in the list "scores", print index(), print number of occurrences (count)
v = 10
if v in scores:
    occ = scores.count(v)
    print(f"{v} is in the list")
    print(f"{v} occurs {occ} times")
    idx = scores.index(v)
    print(f"The value {v} appears first at index {idx}")
else:
    print(f"{v} not in list")


#Get highest (numerical) score, max(list), get lowest score, min(list)
maxValue = max(scores)
print(f"The max value in the list is {maxValue}")
occ = scores.count(maxValue)
print(f"The max value {maxValue} occurs {occ} times")

minValue = min(scores)
print(f"The min value in the list is {minValue}")
occ = scores.count(maxValue)
print(f"The min value {minValue} occurs {occ} times")


#filter high scores, go through each score and add the the ones >= 90 to a new list, print, get those below 40

#scores = [95, 87, 92, 88, 95, 76, 90, 87,100]

#We put the code into a function, and take the list of scores, and low/high threshold values as parameter, returning a tupple
def find_highest_and_lowest(listOfScores, low, high):
    hiValues = []
    loValues = []

    hiThreshold = high
    loThreshold = low

    for v in scores:
        if v >= hiThreshold:
            hiValues.append(v)
        elif v <= loThreshold:
            loValues.append(v)

    return hiValues, loValues
        
result = find_highest_and_lowest(scores, 40, 90)

list1, liste2 = result


#append new item to list, print before and after, sort
print("Current List: ",scores)
scores.append(55)
print("List after append: ",scores)

#extend list with new scores[x,x]
scores.extend([105,110])
print("Scores Extended with 105 and 110: ", scores)


#remove an item from the list, first checking if the value is present
if 95 in scores:
    scores.remove(95)
print(scores)


#insert new score at index 2 (index, value)
scores.insert(0,1000)
print(scores)

#return and remove last item .pop
#return and remove element "4",.pop
print("List bfore removing last value: ", scores)

val = scores.pop(4)
print("Value removed: ", val)
print("List after removing last value: ", scores)




# ==================================================
# 2. TUPLES - Immutable Collections, Faster than lists
# ==================================================

#Tuples, people
person = ("Alice", 30, "Student")
#Unpacking
#assign values to variables, first position in the tuple first, then second, third, etc. Order matters
name, age, role = person

#Result when assigning based on position
print("Name: ",person[0])
print("Age: ",person[1])
print("Role: ",person[2])

print("-"*20)

#Same result after assigning values in the tuple to variables
print("Name: ",name)
print("Age: ",age)
print("Role: ",role)



#return .index of value
idx=person.index(30)
print("Index of value: ", idx)


#.count occurrences of 28
print("Number of elements in tuple: ", person.count(30))

#Get length of tuple
print("Length of tuple: ", len(person))

# Demonstrating the 
tomListe = []
print("Length of list: ", len(tomListe))


#go through tuple, for i in tuple, print each element in the tuple
#return function returning tuple, like yesterday



# ==================================================
# 3. Combining lists and tuples
# ==================================================

"""
liste 1[
        (element1, element2, element3),
        (element1, element2, element3),
        (element1, element2, element3),
    ]
"""


students = [("Alice", 95, 92, 88), ("Bob", 78, 85, 82)]
print("Name: ", students[0][3])
#print each students name and scores, for tuple in list, print element 0 and rest





#Task
# Create a list of students(tuples) and scores for 3 tests. Example: students = [("Alice", 95, 92, 88)]
students = [("Alice", 95, 92, 88), ("Bob", 78, 85, 82), ("Charlie", 88, 90, 85)]

# Create a function that takes a list as a paramenter, and prints each student and the score for each test (Example: Test 1: 95, Test 2: 92, Test 3: 88)
def print_students(lst):
    for student in lst:
        print(student)

print_students(students)

# Create a function to add students, the function should take a Name, and 3 scores, and add it to the list
def add_student(lst, name, s1, s2, s3):
    lst.append((name, s1, s2, s3))
    return lst

students= add_student(students, "David", 90, 85, 88)

print_students(students)

# Create a function that takes a list, and prints a sorted list based on name
def sort_by_name(lst):
    return sorted(lst)

students = sort_by_name(students)

print_students(students)


# Create a function that finds a student by name, and returns the name and their grades as a tupple, 
# assigning them to variables (name, g1, g2, g3 = "return value of function). Then print the variables
# Remember that the "nested" list looks like:
#  ---------[0]---------  ---------[1]-------  ---------[2]-----------
#     [0]   [1] [2]  [3]    [0]   [1] [2] [3]     [0]     [1] [2]  [3]
# [("Alice", 95, 92, 88), ("Bob", 78, 85, 82), ("Charlie", 88, 90, 85)]
def find_student(lst, name):
    #s is the current element in the out list, ex: ("Alice", 95, 92, 88)
    for s in lst:
        #[0] is the Name, Ex "Alice"
        if s[0] == name:
            #If the name matches, return the entire object s. (which is: ("Alice", 95, 92, 88))
            return s

name, g1, g2, g3 = find_student(students, "Alice")
print(name, g1, g2, g3)


    
