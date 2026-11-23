from pathlib import Path


data = "alice,15;BOB,3;charlie,22;DAVID,8;eve,12"


def process_user(record):
    name, login_count = record.split(",")
    return name.strip().title(), int(login_count.strip())


def calculate_statistics(users):
    highest = users[0][1]
    lowest = users[0][1]
    total_logins = 0

    for user in users:
        login_count = user[1]
        total_logins += login_count

        if login_count > highest:
            highest = login_count
        if login_count < lowest:
            lowest = login_count

    average = total_logins / len(users)
    return highest, lowest, average


def load_login_data(filename):
    loaded_users = []
    with open(filename, "r") as file:
        for line in file:
            for record in line.strip().split(";"):
                if record.strip():
                    name, login_count = process_user(record)
                    loaded_users.append([name, login_count])
    return loaded_users


# Build the nested list from the starting data.
users = []
for record in data.split(";"):
    name, login_count = process_user(record)
    users.append([name, login_count])

# Add records from both files without duplicating the same user record.
folder = Path(__file__).resolve().parent
for filename in ("logins.txt", "logins.csv"):
    for loaded_user in load_login_data(folder / filename):
        if loaded_user not in users:
            users.append(loaded_user)

search_name = input("Enter a username to search for: ").strip().lower()
found_user = None
for user in users:
    if user[0].lower() == search_name:
        found_user = user
        break

if found_user:
    print("Found:", found_user[0], "- Logins:", found_user[1])
else:
    print("User not found:", search_name)

total_logins = 0
for user in users:
    total_logins += user[1]

highest, lowest, average = calculate_statistics(users)

print("Name".ljust(15) + " | " + "Logins".rjust(10))
print("-" * 30)
for user in users:
    print(user[0].ljust(15) + " | " + str(user[1]).rjust(10))

print("Total:", total_logins)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
