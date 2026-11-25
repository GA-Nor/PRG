"""
COLLECTIONS PART 2
=========================

- Sets: Unordered, unique collections without duplicates
- Dictionaries: Key-value pairs
"""

# ==================================================
# 1. SETS - Finding Unique Items
# ==================================================


# Skills example, team a+b {Charlie}

#print the contents of each set.

# Find element in set, if var in set, print


#Set Operations
#intersection example, SetA.intersection(SetB) - overlap
#difference example, SetA.difference(SetB) - unique to A
#union example, SetA.union(SetB) - all items, no duplicates


#Convert lists or tuples to sets to find overlap, this removes duplicate entries

#add item to set using .add()

#remove item using .remove()
setA = {"Alice", "Bob"}



#Task: 

#Create a set containing names
#Create another set containing other names, which some names overlap with the first set

#Create  a List or Tuple of names, with duplicate values, and print the list/tuple
# Then convert the list or tuple to a set, and print it. What changed?

#Print the names that exists in both sets
#Print the names that are only in the first set
#print the names only in the second set
#print the names all names present in both sets, without duplicates





# ==================================================
# 2. DICTIONARIES - Key-Value Storage
# ==================================================

# Example, {Username: "Real name",}
users = {"user1": "Alice", "user2": "Bob"}


#print each username and name, for un, n in dict.items()



#check if key exists, if user1 in users, print the value of user1

#Check if value exists, if n in .values()


# search by value in users, for each, get the key and value in items, if value == string, print Key or Value
# when comparing strings, helpful to use .lower()


#Convert keys and values to list (list(dict.keys()/values()))


#add entry to dict, dict[key] = value, {}, can also overwrite existing key


#May be good to check that the Key doesnt exists first..
#if the key is not in dict, add [user3] with value David



#TASK 2

#Create a dictionary for users containing usernames, and their name: for example {Alice3558: "Alice Huang", Bob123: "Bob Lee"}

#Create a function that takes a dictionary as a parameter and lists all the usernames and names

#Create a function that takes a dictionary and a username, and checks if that user exists, if it does print the username and name
# If it doesnt exist, print "not found"

#Create a function that adds a user to the dictionary (the function needs to take in username, name)
#The function must check if the username already exists in the dictionary BEFORE adding it
#If it already exists, print "User exists", and dont add it to the dictionary



