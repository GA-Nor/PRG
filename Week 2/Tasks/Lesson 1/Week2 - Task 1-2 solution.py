from pathlib import Path


users = "alice ; BOB ; charlie ; DAVID ; eve"


def clean_name(name):
    return name.strip().title()


def load_users(filename):
    with open(filename, "r") as file:
        user_text = file.read()

    #replace newlines with semicolons, then split on semicolons
    user_names = user_text.replace("\n", ";").split(";")
    loaded_users = []
    for name in user_names:
        if name.strip():
            loaded_users.append(clean_name(name))
    return loaded_users


# Clean the names in the starting string.
cleaned_users = []
for name in users.split(";"):
    cleaned_users.append(clean_name(name))

# Read users.txt from the same folder as this script.
folder = Path(__file__).resolve().parent
file_users = load_users(folder / "users.txt")
for name in file_users:
    if name not in cleaned_users:
        cleaned_users.append(name)

longest_name = cleaned_users[0]
shortest_name = cleaned_users[0]
for name in cleaned_users:
    if len(name) > len(longest_name):
        longest_name = name
    if len(name) < len(shortest_name):
        shortest_name = name

search_name = clean_name(input("Enter a name to search for: "))
found = False
for name in cleaned_users:
    if name == search_name:
        print("Found:", name)
        found = True
        break

if not found:
    print("User not found:", search_name)

print("Users List".center(35))
print("*" * 35)
print("Name".ljust(15) + " | " + "Length".rjust(15))
print("-" * 35)
for name in cleaned_users:
    print(name.ljust(15) + " | " + str(len(name)).rjust(15))

print("Total:", len(cleaned_users))
print("Longest:", longest_name)
print("Shortest:", shortest_name)
