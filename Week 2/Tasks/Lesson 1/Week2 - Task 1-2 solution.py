def clean_name(name):
    name = name.strip()
    name = name.title()
    return name

# Read the names from the file and split them at each semicolon.
with open("users.txt", "r") as file:
    user_text = file.read()

user_names = user_text.split(";")
cleaned_names = []

# Clean each name and save it in a new list.
for name in user_names:
    cleaned_name = clean_name(name)
    cleaned_names.append(cleaned_name)

# Start with the first name, then compare the rest.
longest_name = cleaned_names[0]
shortest_name = cleaned_names[0]

for name in cleaned_names:
    if len(name) > len(longest_name):
        longest_name = name
    if len(name) < len(shortest_name):
        shortest_name = name

# Print the names and their lengths in a table.
print("Users List".center(35))
print("*" * 35)
print("Name".ljust(15) + " | " + "Length".rjust(15))
print("-" * 35)
for name in cleaned_names:
    name_length = len(name)
    print(name.ljust(15) + " | " + str(name_length).rjust(15))

print("Total:", len(cleaned_names))
print("Longest:", longest_name)
print("Shortest:", shortest_name)
