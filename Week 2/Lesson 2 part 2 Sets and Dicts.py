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
setA = {"Alice", "Bob", "Charlie", "Alice", "Jensen"}
print("Set 1: ",setA)
setB = {"Bob", "Jensen", "Huang"}
#print the contents of each set.
print("Set 2: ",setB)

# Find element in set, if var in set, print
if "Alice" in setA:
   print("Alice is in: ", setA)


#Set Operations
#intersection example, SetA.intersection(SetB) - overlap
setC = setA.intersection(setB) 
print("Elements that are in both set A and set B: ", setC)

#difference example, SetA.difference(SetB) - unique to A
setD = setA.difference(setB)
print("These elements are unique to A: ", setD)

#union example, SetA.union(SetB) - all items, no duplicates
setE = setA.union(setB)
print("The union of Set A and Set B: ", setE)


#Convert lists or tuples to sets to find overlap, this removes duplicate entries
names = ["Alice", "Alice", "Bob", "Jensen"]
friends = ["Bob", "Charlie", "Charlie"]

print("List Names: ", names)
print("List Friends: ", friends)

set_names = set(names)
set_friends = set(friends)

print("Set Names: ", set_names)
print("Set Friends: ", set_friends)

#add item to set using .add()
set_names.add("Huang")
print("New set values after adding Bob: ", set_names)

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
users = {"user1": "Alice", "user1": "Bob"}
print(users)

#Add new user, cant use duplicate keys
users["user3"] = "Charlie"
print(users)

#print each username and name, for un, n in dict.items()
for k,v in users.items():
   print("Username: ",k, " Name: ",v)


#check if key exists, if user1 in users, print the value of user1
if "user1" in users.keys():
   print(users["user1"])


#Check if value exists, if n in .values()
if "Jensen" in users.values():
   print("Bob is in the dictionary")

"""
# search by value in users, for each, get the key and value in items, if value == string, print Key or Value
# when comparing strings, helpful to use .lower()
for k, v in users:
   if v == "Bob":
      print(k)

#Convert keys and values to list (list(dict.keys()/values()))
listOfKeys = list(users.keys())
listOfvalues = list(users.values())

print("List of keys: ", listOfKeys)
print("List of values: ", listOfvalues)

#add entry to dict, dict[key] = value, {}, can also overwrite existing key

"""

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



