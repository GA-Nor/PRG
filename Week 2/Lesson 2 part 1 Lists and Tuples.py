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
scores = [95, 87, 92, 88, 95, 76, 90]
#print the scores
print(f"Scores: {scores}\n")

#Find specific item
#if specific score in listOfScores, print index(), print number of occurrences (count)


#Get highest (numerical) score, max(list), get lowest score, min(list)

# filter high scores, go through each score and add the the ones >= 90 to a new list, print, get those below 40

#append new item to list, print before and after, sort

#remove an item from the list

#combining find and remove, if x in list, remove it, print result



#insert new score at index 2 (index, value)

#return and remove last item .pop

#return and remove element "4",.pop

#extend list with new scores[x,x]


# ==================================================
# 2. TUPLES - Immutable Collections, Faster than lists
# ==================================================

#Tuples, people

# Unpack into vars, print list, print vars

#return .index of value

#.count occurrences of 28

#go through tuple, for i in tuple, print

#return function returning tuple, like yesterday



# ==================================================
# 3. Combining lists and tuples
# ==================================================

students = [("Alice", 95, 92, 88), ("Bob", 78, 85, 82)]

#print each students name and scores, for tuple in list, print element 0 and rest





#Task
# Create a list of students(tuples) and scores for 3 tests. Example: students = [("Alice", 95, 92, 88)]
# Create a function that takes a list as a paramenter, and prints each student and the score for each test (Example: Test 1: 95, Test 2: 92, Test 3: 88)
# Create a function to add students, the function should take a Name, and 3 scores, and add it to the list
# Create a function that takes a list, and prints a sorted list based on name
# Create a function that finds a student by name, and returns the name and their grades as a tupple, assigning them to variables (name, g1, g2, g3 = "return value of function). Then print the variables

